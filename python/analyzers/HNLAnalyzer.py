'''
This is the base analyzer going through data and trying to identify HNL->3L events.
'''

import ROOT
from itertools import product, combinations
from math import sqrt, pow
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Lepton
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2
from PhysicsTools.Heppy.physicsobjects.GenParticle   import GenParticle
from PhysicsTools.Heppy.physicsobjects.Photon        import Photon
from PhysicsTools.Heppy.physicsobjects.Tau           import Tau
from PhysicsTools.Heppy.physicsobjects.Muon          import Muon
from PhysicsTools.Heppy.physicsobjects.Electron      import Electron
from PhysicsTools.Heppy.physicsobjects.Jet           import Jet
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject
from CMGTools.HNL.utils.utils                        import isAncestor, displacement2D, displacement3D, makeRecoVertex, fitVertex
from CMGTools.HNL.physicsobjects.HN3L                import HN3L
from CMGTools.HNL.physicsobjects.DiLepton            import DiLepton
from CMGTools.HNL.physicsobjects.DisplacedMuon       import DisplacedMuon
from pdb import set_trace

# load custom library to ROOT. This contains the kinematic vertex fitter class
ROOT.gSystem.Load('libCMGToolsHNL')
from ROOT import HNLKinematicVertexFitter as VertexFitter

deadcone_ch = 0.015; deadcone_pu = 0.015; deadcone_ph = 0.08;

class HNLAnalyzer(Analyzer):
    ''' Generic analyzer for HNL -> DiLepton + MET, independent of the final state flavours '''

    def declareHandles(self): 
        super(HNLAnalyzer, self).declareHandles() 

        self.handles['electrons'] = AutoHandle(('slimmedElectrons'             ,'','PAT' ), 'std::vector<pat::Electron>'                    )
        self.handles['muons'    ] = AutoHandle(('slimmedMuons'                 ,'','PAT' ), 'std::vector<pat::Muon>'                        )
        self.handles['dsamuons' ] = AutoHandle(('displacedStandAloneMuons'     ,'','RECO'), 'std::vector<reco::Track>', mayFail=True        )
        self.handles['dgmuons'  ] = AutoHandle(('displacedGlobalMuons'         ,'','RECO'), 'std::vector<reco::Track>', mayFail=True        )
        self.handles['photons'  ] = AutoHandle(('slimmedPhotons'               ,'','PAT' ), 'std::vector<pat::Photon>'                      )
        self.handles['taus'     ] = AutoHandle(('slimmedTaus'                  ,'','PAT' ), 'std::vector<pat::Tau>'                         )
        self.handles['jets'     ] = AutoHandle( 'slimmedJets'                             , 'std::vector<pat::Jet>'                         )
        self.handles['pvs'      ] = AutoHandle(('offlineSlimmedPrimaryVertices','','PAT' ), 'std::vector<reco::Vertex>'                     )
        self.handles['svs'      ] = AutoHandle(('slimmedSecondaryVertices'     ,'','PAT' ), 'std::vector<reco::VertexCompositePtrCandidate>')
        self.handles['beamspot' ] = AutoHandle(('offlineBeamSpot'              ,'','RECO'), 'reco::BeamSpot'                                )
        self.handles['pfmet'    ] = AutoHandle(('slimmedMETs'                  ,'','PAT' ), 'std::vector<pat::MET>'                         )
        self.handles['puppimet' ] = AutoHandle('slimmedMETsPuppi'                         , 'std::vector<pat::MET>'                         )
        self.handles['pfcand'   ] = AutoHandle('packedPFCandidates'                       , 'std::vector<pat::PackedCandidate> '            )

    def assignVtx(self, particles, vtx):
        for ip in particles:
            ip.associatedVertex = vtx

    def beginLoop(self, setup):
        super(HNLAnalyzer, self).beginLoop(setup)
        self.counters.addCounter('HNL')
        count = self.counters.counter('HNL')
        count.register('all events')
        count.register('good pf collections')
        count.register('>0 good vtx')
        count.register('>= 3 leptons')
        count.register('>= 3 leptons with correct flavor combo')
        count.register('enough electrons passing preselection')
        count.register('enough muons passing preselection')
        count.register('>0 prompt lep')
        count.register('>0 trig match prompt lep')
        count.register('> 0 di-lepton')
        count.register('> 0 di-lepton + vtx')
        # count.register('> 0 di-leptons with good vertices')
        # count.register('exactly 1 dilepton with good vertex')
    
    def buildDiLeptons(self, cmgDiLeptons, event):
        return map(self.__class_.DiLeptonClass, cmgDiLeptons) 

    def testLepKin(self, lep, pt, eta):
        #kinematics
        if abs(lep.eta())>eta: return False
        if lep.pt()      <pt : return False
        return True
     
    def testLepVtx(self, lep, dxy, dz):
        # vertex
        if abs(lep.dz()) >dz : return False
        if abs(lep.dxy())>dxy: return False
        # passed
        return True
    
    def preselectPromptElectrons(self, ele, pt=30, eta=2.5, dxy=0.045, dz=0.2):
        # kinematics
        if not self.testLepKin(ele, pt, eta): return False
        # id
        if not ele.electronID("MVA_ID_nonIso_Fall17_Loose"): return False
        # vertex
        if not self.testLepVtx(ele, dxy, dz): return False
        # passed
        return True

    def preselectPromptMuons(self, mu, pt=25, eta=2.4, dxy=0.045, dz=0.2):
        # kinematics
        if not self.testLepKin(mu, pt, eta): return False
        # id
        if not mu.looseId(): return False
        # vertex
        if not self.testLepVtx(mu, dxy, dz): return False
        # passed
        return True
   
    def isOotMuon(self, muon):
        '''
        returns True if the muon fires the out-of-time selection proposed by Piotr
        https://indico.cern.ch/event/695762/contributions/2853865/attachments/1599433/2535174/ptraczyk_201802_oot_fakes.pdf
        
        For in-time muons you want this to return False.
        '''
        cmb = muon.time()
        rpc = muon.rpcTime()
        
        # I guess one needs to understand which type of time is needed
        # there is an enum to do that
        # http://cmslxr.fnal.gov/source/DataFormats/MuonReco/interface/MuonTime.h#0007
        
        if rpc.direction == -1:
            rpc.time    = rpc.timeAtIpOutIn()
            rpc.timeerr = rpc.timeAtIpOutInErr()
        elif rpc.direction == 1:
            rpc.time = rpc.timeAtIpInOut()
            rpc.timeerr = rpc.timeAtIpInOutErr()
        else:
            # print 'WARNING: undefined muon direction, cannot understand RPC time'
            return False

        if cmb.direction == -1:
            cmb.time    = cmb.timeAtIpOutIn()
            cmb.timeerr = cmb.timeAtIpOutInErr()
        elif cmb.direction == 1:
            cmb.time = cmb.timeAtIpInOut()
            cmb.timeerr = cmb.timeAtIpInOutErr()
        else:
            # print 'WARNING: undefined muon direction, cannot understand CMB time'
            return False
        
        cmbok = (cmb.nDof>7)
        rpcok = (rpc.nDof>1 and rpc.timeerr==0)
        
        if rpcok:
            if abs(rpc.time)>10 and not (cmbok and abs(cmb.time)<10):
                return True
        else:
            if cmbok and (cmb.time>20 or cmb.time<-45):
                return True
        
        return False

    def checkLeptonFlavors(self, electrons, muons):
        ''' Checks whether the existing leptons are 
        in the correct flavor combination'''
        minNumMu  = 0
        minNumEle = 0

        if self.cfg_ana.promptLepton=='mu':
            minNumMu  += 1
        if self.cfg_ana.promptLepton=='ele':
            minNumEle += 1
        if self.cfg_ana.L1L2LeptonType == 'ee':
            minNumEle += 2
        if self.cfg_ana.L1L2LeptonType == 'mm':
            minNumMu  += 2
        if self.cfg_ana.L1L2LeptonType == 'em':
            minNumMu  += 1
            minNumEle += 1

        if len(electrons) < minNumEle: return False
        if len(muons)     < minNumMu: return False
        return True

    def makeLeptonPairs(self, event, electrons, muons):
        ''' Create all the possible di-lepton pairs 
        out of the different collections'''
        if self.cfg_ana.L1L2LeptonType == 'ee':
            leptons = electrons
        if self.cfg_ana.L1L2LeptonType == 'mm':
            leptons = muons
        if self.cfg_ana.L1L2LeptonType == 'em':
            leptons = electrons + muons

        dileptons = combinations(leptons, 2)
        dileptons = [(lep1, lep2) for lep1, lep2 in dileptons if deltaR(lep1, lep2)>0.01]

        if self.cfg_ana.L1L2LeptonType == 'em':
            dileptons = [(lep1, lep2) for lep1, lep2 in dileptons if abs(lep1.pdgId()) + abs(lep2.pdgId()) == 24]
            for pair in dileptons:
                pair = sorted(pair, key = lambda lep: (abs(lep.pdgId()),-lep.pt()),reverse = False)

        return dileptons
        
    def selectDiLepton(self, event, dileptonsvtx):
        which_candidate = getattr(self.cfg_ana, 'candidate_selection', 'maxpt')
        
        if which_candidate == 'minmass'    : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(),  x.mass()                        ), reverse=False)[0]
        if which_candidate == 'minchi2'    : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(),  x.chi2()                        ), reverse=False)[0]
        if which_candidate == 'mindr'      : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(),  x.dr()                          ), reverse=False)[0]
        if which_candidate == 'maxdphi'    : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.dphi()                        ), reverse=False)[0]
        if which_candidate == 'mindeta'    : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(),  x.deta()                        ), reverse=False)[0]
        if which_candidate == 'maxdisp2dbs': event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.disp2DFromBS()                ), reverse=False)[0]
        if which_candidate == 'maxdisp2dpv': event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.disp2DFromPV()                ), reverse=False)[0]
        if which_candidate == 'maxdisp3dpv': event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.disp3DFromPV()                ), reverse=False)[0]
        if which_candidate == 'maxdls2dbs' : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.disp2DFromBSSignificance()    ), reverse=False)[0]
        if which_candidate == 'maxdls2dpv' : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.disp2DFromPVSignificance()    ), reverse=False)[0]
        if which_candidate == 'maxdls3dpv' : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.disp3DFromPVSignificance()    ), reverse=False)[0]
        if which_candidate == 'maxcos'     : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.cosTransversePointingAngleBS()), reverse=False)[0]
        if which_candidate == 'maxpt'      : event.displaced_dilepton_reco_cand = None if not len(dileptonsvtx) else sorted(dileptonsvtx, key = lambda x : (x.isSS(), -x.pt()                          ), reverse=False)[0]


    def process(self, event):
        return self.searchHNL(event)
        
    def searchHNL(self, event):
        self.readCollections(event.input)
        self.counters.counter('HNL').inc('all events')
        # make PF candidates
        try:
            pfs = map(PhysicsObject, self.handles['pfcand'].product())
            event.pfs = pfs
        except: print(event.eventId, event.run, event.lumi); return False#; set_trace()
        self.counters.counter('HNL').inc('good pf collections')
      
#        event.rho = self.handles['rho'].product()[0]

        #####################################################################################
        # primary vertex
        #####################################################################################
        if not len(event.goodVertices):
            return False

        self.counters.counter('HNL').inc('>0 good vtx')

        #####################################################################################
        # produce collections and map our objects to convenient Heppy objects
        #####################################################################################
        # make muon collections
        event.muons       = map(Muon, self.handles['muons'].product())
       # event.dsamuons    = self.buildDisplacedMuons(self.handles['dsamuons'].product())
       # event.dgmuons     = self.buildDisplacedMuons(self.handles['dgmuons' ].product())

        for imu in event.muons   : imu.type = 13; imu.rho = event.rho
#        for imu in event.dsamuons: imu.type = 26
#        for imu in event.dgmuons : imu.type = 39

        # save a flag to know whether the muons is likely OOT
        # FIXME! for displaced too?
        for imu in event.muons:
            imu.isoot = self.isOotMuon(imu)

        event.electrons   = map(Electron, self.handles['electrons'].product())
        
        # prepare the electrons for ID mangling
        for ele in event.electrons:
            ele.event = event.input.object() # RM: this is needed god knows why to get the eleID
            ele.rho = event.rho

        event.photons     = map(Photon  , self.handles['photons'  ].product())
        event.taus        = map(Tau     , self.handles['taus'     ].product())

        # make vertex objects 
        event.pvs         = self.handles['pvs'     ].product()
        event.svs         = self.handles['svs'     ].product()
        event.beamspot    = self.handles['beamspot'].product()

        # make met object
        event.pfmet       = self.handles['pfmet'   ].product().at(0)
        event.puppimet    = self.handles['puppimet'].product().at(0)

        # make jet object
        jets = map(Jet, self.handles['jets'].product())        

        # assign to the leptons the primary vertex, will be needed to compute a few quantities
        pv = event.goodVertices[0]
        
        self.assignVtx(event.muons    , pv)
        self.assignVtx(event.electrons, pv)

        #####################################################################################
        # filter for events with at least 3 leptons in proper flavor combination
        #####################################################################################
        
        #check there are enough leptons
        if len(event.muons + event.electrons) < 3: 
            return False
        self.counters.counter('HNL').inc('>= 3 leptons')
        
        #check there are enough leptons in the resp. flavor combination
        if not self.checkLeptonFlavors(event.electrons, event.muons):
            return False 

        #save the key numbers
        event.nElectrons = len(event.electrons)
        event.nMuons     = len(event.muons)
        event.nLeptons   = len(event.electrons) + len(event.muons) 
        
        self.counters.counter('HNL').inc('>= 3 leptons with correct flavor combo')

        #####################################################################################
        # Preselect electrons
        #####################################################################################
        #FIXME: make min electron pt configurable and set the default at 5 GeV
        event.electrons  = [iele for iele in event.electrons if iele.pt()>5. and abs(iele.eta())<2.5]

        #check there are enough leptons in the resp. flavor combination
        if not self.checkLeptonFlavors(event.electrons, event.muons):
            return False 

        self.counters.counter('HNL').inc('enough electrons passing preselection')

        #####################################################################################
        # Preselect muons
        #####################################################################################
        
        event.muons      = [imu for imu in event.muons if imu.pt()>3. and abs(imu.eta())<2.4]
        # event.dsamuons   = [imu for imu in event.dsamuons       if imu.pt()>3. and abs(imu.eta())>2.4]
        # event.dgmuons    = [imu for imu in event.dgmuons        if imu.pt()>3. and abs(imu.eta())>2.4]

        #check there are enough leptons in the resp. flavor combination
        if not self.checkLeptonFlavors(event.electrons, event.muons):
            return False 
        self.counters.counter('HNL').inc('enough muons passing preselection')

        #####################################################################################
        # Preselect the prompt leptons
        #####################################################################################
        prompt_mu_cands  = sorted([mu  for mu  in event.muons     if self.preselectPromptMuons    (mu) ], key = lambda x : x.pt(), reverse = True)
        prompt_ele_cands = sorted([ele for ele in event.electrons if self.preselectPromptElectrons(ele)], key = lambda x : x.pt(), reverse = True)

        if   self.cfg_ana.promptLepton=='mu':
            prompt_leps = prompt_mu_cands       
        elif self.cfg_ana.promptLepton=='ele':
            prompt_leps = prompt_ele_cands
        else:
            print 'ERROR: HNLAnalyzer not supported lepton flavour', self.cfg_ana.promptLepton
            exit(0) 
        if not len(prompt_leps):
            return False
        
        self.counters.counter('HNL').inc('>0 prompt lep')

        #####################################################################################
        # HLT matching
        #####################################################################################
        
        # match only if the trigger fired and if it is among those we care about
        fired_triggers = [info for info in getattr(event, 'trigger_infos', []) if info.fired and '_'.join(info.name.split('_')[:-1]) in self.cfg_ana.triggersAndFilters.keys()]
    
        drmax=0.15
        
        # loop over the selected prompt leptons
        for ilep in prompt_leps:
        
            # prepare the HLT obj container, empty
            ilep.matched_hlt_obj = []
            
            # loop over the final HLT objects of each path
            for info in fired_triggers:
            
                # get the HLT name w/o version
                hltname     = '_'.join(info.name.split('_')[:-1])          
                # get the filter name you want to match the offline lepton to
                lastfilter  = self.cfg_ana.triggersAndFilters[hltname]
                # get the corresponding HLT objects
                lastobjects = [iobj for iobj in info.objects if lastfilter in [ilab for ilab in iobj.filterLabels()]]
                # match HLT objects and leptons
                matchedobjs = [iobj for iobj in lastobjects if deltaR(iobj, ilep)<drmax]
                # extend the list of matched objects
                ilep.matched_hlt_obj.extend(matchedobjs)
            
            # remove duplicates through 'set'
            ilep.matched_hlt_obj = [iobj for iobj in set(ilep.matched_hlt_obj)]
        
        # now filter out non matched leptons
        prompt_leps = [ilep for ilep in prompt_leps if len(ilep.matched_hlt_obj)>0]
        
        if len(prompt_leps)==0:
            return False
        
        self.counters.counter('HNL').inc('>0 trig match prompt lep')
        
        #####################################################################################
        # Select the prompt lepton candidate and remove it from the collection of leptons
        #####################################################################################

        # the collection is already sorted by pt, just take the first
        prompt_lep = prompt_leps[0]

        # remove the prompt lepton from the corresponding lepton collection that will be later used to find the displaced di-lepton
        event.filtered_muons     = [mu  for mu  in event.muons     if mu.physObj  != prompt_lep.physObj]
        event.filtered_electrons = [ele for ele in event.electrons if ele.physObj != prompt_lep.physObj]
         
        ########################################################################################
        # Preselection for the reco leptons and then create pairs
        ########################################################################################
        # some simple preselection
        event.muons      = [imu for imu in event.filtered_muons if imu.pt()>3. and abs(imu.eta())<2.4]
        # event.dsamuons   = [imu for imu in event.dsamuons       if imu.pt()>3. and abs(imu.eta())>2.4]
        # event.dgmuons    = [imu for imu in event.dgmuons        if imu.pt()>3. and abs(imu.eta())>2.4]
        event.electrons  = [iele for iele in event.filtered_electrons if iele.pt()>5. and abs(iele.eta())<2.5]

        # create all the possible di-lepton pairs out of the different collections
        dileptons = self.makeLeptonPairs(event,event.electrons,event.muons)

        if not len(dileptons):
            return False

        self.counters.counter('HNL').inc('> 0 di-lepton')

        ########################################################################################
        # Vertex Fit: Select only dilepton pairs with mutual vertices
        ########################################################################################
        dileptonsvtx = []
        for index, pair in enumerate(dileptons):
            if pair[0]==pair[1]: continue
            sv = fitVertex(pair,self.cfg_ana.L1L2LeptonType)
            if not sv: continue
            dileptonsvtx.append(DiLepton(pair, sv, pv, event.beamspot))

        event.dileptonsvtx = dileptonsvtx
        
        if not len(event.dileptonsvtx):
            return False 
        
        self.counters.counter('HNL').inc('> 0 di-lepton + vtx')

        ########################################################################################
        # Select the most promising dilepton candidate
        ########################################################################################
        self.selectDiLepton(event, dileptonsvtx)

        ########################################################################################
        # Create a reco HNL3L object and "harvest" all the relevant eventinfos
        ########################################################################################
        event.the_3lep_cand = HN3L(prompt_lep, 
                                   event.displaced_dilepton_reco_cand.lep1(), 
                                   event.displaced_dilepton_reco_cand.lep2(), 
                                   event.pfmet)


        # save reco secondary vertex
        event.recoSv = event.displaced_dilepton_reco_cand.vtx()

        event.recoSv.disp3DFromBS      = ROOT.VertexDistance3D().distance(event.recoSv, pv)
        event.recoSv.disp3DFromBS_sig  = event.recoSv.disp3DFromBS.significance()
        
        # create an 'ideal' vertex out of the BS
        point = ROOT.reco.Vertex.Point(
            event.beamspot.position().x(),
            event.beamspot.position().y(),
            event.beamspot.position().z(),
        )
        error = event.beamspot.covariance3D()
        chi2 = 0.
        ndof = 0.
        bsvtx = ROOT.reco.Vertex(point, error, chi2, ndof, 2) # size? say 3? does it matter?
                                        
        event.recoSv.disp2DFromBS      = ROOT.VertexDistanceXY().distance(event.recoSv, bsvtx)
        event.recoSv.disp2DFromBS_sig  = event.recoSv.disp2DFromBS.significance()
        event.recoSv.prob              = ROOT.TMath.Prob(event.recoSv.chi2(), int(event.recoSv.ndof()))
        
        dilep_p4 = event.displaced_dilepton_reco_cand.lep1().p4() + event.displaced_dilepton_reco_cand.lep2().p4()

        perp = ROOT.math.XYZVector(dilep_p4.px(),
                                   dilep_p4.py(),
                                   0.)
        
        dxybs = ROOT.GlobalPoint(-1*((event.beamspot.x0() - event.recoSv.x()) + (event.recoSv.z() - event.beamspot.z0()) * event.beamspot.dxdz()), 
                                 -1*((event.beamspot.y0() - event.recoSv.y()) + (event.recoSv.z() - event.beamspot.z0()) * event.beamspot.dydz()),
                                  0)
        
        vperp = ROOT.math.XYZVector(dxybs.x(), dxybs.y(), 0.)
        
        cos = vperp.Dot(perp)/(vperp.R()*perp.R())
        
        event.recoSv.disp2DFromBS_cos = cos

        ########################################################################################
        # Define event.selectedLeptons, will be used by JetAnalyzer.py
        ########################################################################################

        # the selected 3 leptons must be leptons and not jets
        event.selectedLeptons = [event.the_3lep_cand.l0(),
                                 event.the_3lep_cand.l1(),
                                 event.the_3lep_cand.l2()]

        # plus any isolated electron or muon is also a good lepton rather than a jet
        event.selMuons     = [mu  for mu  in event.muons     if self.preselectPromptMuons    (mu , pt=10) and mu .relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0)<0.15]
        event.selElectrons = [ele for ele in event.electrons if self.preselectPromptElectrons(ele, pt=10) and ele.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0)<0.15]
        # RM: what about taus?

        event.selectedLeptons += event.selMuons
        event.selectedLeptons += event.selElectrons

        ########################################################################################
        # Extra prompt and isolated lepton veto
        ########################################################################################        
        event.veto_mus   = [mu for mu in event.selMuons     if mu.physObj not in [event.the_3lep_cand.l0().physObj, event.the_3lep_cand.l1().physObj, event.the_3lep_cand.l2().physObj] ]
        event.veto_eles  = [ele  for ele  in event.selElectrons if ele .physObj not in [event.the_3lep_cand.l0().physObj, event.the_3lep_cand.l1().physObj, event.the_3lep_cand.l2().physObj] ]

        #FIXME: Is this step really needed?
        if len(event.veto_eles): event.veto_save_ele = sorted([ele for ele in event.veto_eles], key = lambda x : x.pt, reverse = True)[0] 
        if len(event.veto_mus ): event.veto_save_mu  = sorted([mu  for mu  in event.veto_mus ], key = lambda x : x.pt, reverse = True)[0] 

        ########################################################################################
        # charged PF isolation
        ########################################################################################        

        event.the_3lep_cand.abs_tot_iso03_rhoArea    = totIso(event, 'rhoArea', 0.3) 
        event.the_3lep_cand.abs_tot_iso04_rhoArea    = totIso(event, 'rhoArea', 0.4) 
        event.the_3lep_cand.abs_tot_iso05_rhoArea    = totIso(event, 'rhoArea', 0.5) 

        event.the_3lep_cand.rel_tot_iso03_rhoArea    = event.the_3lep_cand.abs_tot_iso03_rhoArea / event.the_3lep_cand.hnVisP4().pt()
        event.the_3lep_cand.rel_tot_iso04_rhoArea    = event.the_3lep_cand.abs_tot_iso04_rhoArea / event.the_3lep_cand.hnVisP4().pt()
        event.the_3lep_cand.rel_tot_iso05_rhoArea    = event.the_3lep_cand.abs_tot_iso05_rhoArea / event.the_3lep_cand.hnVisP4().pt()

        event.the_3lep_cand.abs_tot_iso03_deltaBeta  = totIso(event, 'dBeta', 0.3) 
        event.the_3lep_cand.abs_tot_iso04_deltaBeta  = totIso(event, 'dBeta', 0.4) 
        event.the_3lep_cand.abs_tot_iso05_deltaBeta  = totIso(event, 'dBeta', 0.5) 

        event.the_3lep_cand.rel_tot_iso03_deltaBeta  =  event.the_3lep_cand.abs_tot_iso03_deltaBeta /  event.the_3lep_cand.hnVisP4().pt()
        event.the_3lep_cand.rel_tot_iso04_deltaBeta  =  event.the_3lep_cand.abs_tot_iso04_deltaBeta /  event.the_3lep_cand.hnVisP4().pt()
        event.the_3lep_cand.rel_tot_iso05_deltaBeta  =  event.the_3lep_cand.abs_tot_iso05_deltaBeta /  event.the_3lep_cand.hnVisP4().pt()


        #####################################################################################
        # After passing all selections and we have an HNL candidate, pass a "true" boolean!
        #####################################################################################
        return True



def totIso(event, offset_mode, dRCone):
    ch_pu_iso = chargedHadronIso(event, dRCone, True)
    ch_pv_iso = chargedHadronIso(event, dRCone, False)
    neu_iso   = neutralHadronIso(event, dRCone)
    ph_iso    = photonIso(event, dRCone)
    if offset_mode == 'rhoArea': 
        eta = event.the_3lep_cand.hnVisP4().eta()
        offset = offset_rhoArea(event.rho, dRCone, eta)
    if offset_mode == 'dBeta': 
        offset = offset_dBeta(0.5, ch_pu_iso)
    tot_iso = ch_pv_iso + max(0., ph_iso + neu_iso - offset)
    # if dRCone == 0.3:
        # print '2M dr %.1f: ch_pv_iso: %.2f, neu_iso: %.2f, ph_iso: %.2f, ch_pu_iso: %.2f, l1+l2pt: %.2f, id: %i'%(dRCone, ch_pv_iso, neu_iso, ph_iso, ch_pu_iso, event.the_3lep_cand.l1().pt()+event.the_3lep_cand.l2().pt(), event.eventId)
    return tot_iso

# This is taken from src/PhysicsTools/Heppy/python/physicsobjects/Lepton.py   AND   src/PhysicsTools/Heppy/python/physicsobjects/Electron.py
def offset_rhoArea(rho, dRCone, eta):
    area = 0.0
    if abs(eta) < 0.8000: area = 0.0566
    if abs(eta) > 0.8000 and abs(eta) < 1.3000: area = 0.0562
    if abs(eta) > 1.3000 and abs(eta) < 2.0000: area = 0.0363
    if abs(eta) > 2.0000 and abs(eta) < 2.2000: area = 0.0119
    if abs(eta) > 2.2000 and abs(eta) < 2.4000: area = 0.0064
    if dRCone != 0.3: area *= ( (dRCone ** 2) / (0.3 **2) )
    # print 'area = {a}, offset = {o}'.format(a = area, o = area * rho) 
    return area * rho
    
def offset_dBeta(dBeta, ch_pu_iso):
    # print 'dbeta = {db}, offset = {o}'.format(db = dBeta, o = dBeta * ch_pu_iso)
    return ch_pu_iso * dBeta
        
def chargedHadronIso(event, dRCone, PU = False): 
    if PU == True:
        charged_pfs = [ipf for ipf in event.pfs if ( ipf.charge() != 0 and ipf.pt() > 0.5 )]
        charged_pfs = [ipf for ipf in charged_pfs if ipf.fromPV() <= 1]
    if PU == False:
        charged_pfs = [ipf for ipf in event.pfs if ( ipf.charge() != 0 and abs(ipf.pdgId()) != 11 and abs(ipf.pdgId()) != 13 and ipf.pt() > 0.5 )]
        charged_pfs = [ipf for ipf in charged_pfs if (ipf.fromPV() > 1 and abs(ipf.pdgId()) == 211) ]
    charged_pfs  = [ipf for ipf in charged_pfs  if deltaR(ipf, event.the_3lep_cand.hnVisP4()) < dRCone ]
    ch_iso       = sum([ipf.pt() for ipf in charged_pfs]) 
#    for i in charged_pfs: print 'charged hadron, pile up:\t', dRCone, PU, i.dz(), i.dxy(), i.pt(), i.pdgId()
    return ch_iso

def neutralHadronIso(event, dRCone): 
    neutral_pfs = [ipf for ipf in event.pfs if ( ipf.charge() == 0 and abs(ipf.pdgId()) != 22 )]
    neutral_pfs = [ipf for ipf in neutral_pfs if ipf.pt() > 0.5]
    neutral_pfs = [ipf for ipf in neutral_pfs if deltaR(ipf, event.the_3lep_cand.hnVisP4()) < dRCone ]
    neu_iso     = sum([ipf.pt() for ipf in neutral_pfs])
#    for i in neutral_pfs: print 'neutral hadron\t', dRCone, i.dz(), i.dxy(), i.pt(), i.pdgId()
    return neu_iso

def photonIso(event, dRCone): 
    photon_pfs = [ipf for ipf in event.pfs if abs(ipf.pdgId()) == 22]
    photon_pfs = [ipf for ipf in photon_pfs if ipf.pt() > 0.5]
    photon_pfs = [ipf for ipf in photon_pfs if deltaR(ipf, event.the_3lep_cand.hnVisP4()) < dRCone ] 
    ph_iso     = sum([ipf.pt() for ipf in photon_pfs])
#    for i in photon_pfs: print 'photon\t\t', dRCone, i.dz(), i.dxy(), i.pt(), i.pdgId()
    return ph_iso
