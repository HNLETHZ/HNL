'''
Matching bewteen gen and reco quantities.
'''

import ROOT
from itertools import product, combinations
import math
import numpy as np
from copy import deepcopy as dc

from PhysicsTools.Heppy.analyzers.core.Analyzer      import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle    import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Muon          import Muon
from PhysicsTools.Heppy.physicsobjects.Electron      import Electron
from PhysicsTools.Heppy.physicsobjects.Tau           import Tau
from PhysicsTools.Heppy.physicsobjects.Photon        import Photon
from PhysicsTools.Heppy.physicsobjects.Tau           import Tau
from PhysicsTools.Heppy.physicsobjects.Jet           import Jet
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject
from PhysicsTools.HeppyCore.utils.deltar             import deltaR, deltaPhi, inConeCollection, bestMatch

from CMGTools.HNL.utils.utils                  import isAncestor, displacement2D, displacement3D, makeRecoVertex, fitVertex # utility functions
from CMGTools.HNL.physicsobjects.HN3L          import HN3L
from CMGTools.HNL.physicsobjects.DisplacedMuon import DisplacedMuon

from pdb import set_trace

##########################################################################################
# load custom library to ROOT. This contains the kinematic vertex fitter class
ROOT.gSystem.Load('libCMGToolsHNL')
from ROOT import HNLKinematicVertexFitter as VertexFitter

class RecoGenAnalyzer(Analyzer):
    '''
    '''
    def declareHandles(self):
        super(RecoGenAnalyzer, self).declareHandles()

        self.handles  ['muons'      ] = AutoHandle(('slimmedMuons'                 , '', 'PAT' ), 'std::vector<pat::Muon>'                        )
        self.handles  ['electrons'  ] = AutoHandle(('slimmedElectrons'             , '', 'PAT' ), 'std::vector<pat::Electron>'                    )
        self.handles  ['photons'    ] = AutoHandle(('slimmedPhotons'               , '', 'PAT' ), 'std::vector<pat::Photon>'                      )
        self.handles  ['taus'       ] = AutoHandle(('slimmedTaus'                  , '', 'PAT' ), 'std::vector<pat::Tau>'                         )
        self.handles  ['jets'       ] = AutoHandle(('slimmedJets'                  , '', 'PAT' ), 'std::vector<pat::Jet>'                         )
        self.handles  ['dsmuons'    ] = AutoHandle(('displacedStandAloneMuons'     , '', 'RECO'), 'std::vector<reco::Track>'                      )
        self.handles  ['dgmuons'    ] = AutoHandle(('displacedGlobalMuons'         , '', 'RECO'), 'std::vector<reco::Track>'                      )
        self.handles  ['pvs'        ] = AutoHandle(('offlineSlimmedPrimaryVertices', '', 'PAT' ), 'std::vector<reco::Vertex>'                     )
        self.handles  ['svs'        ] = AutoHandle(('slimmedSecondaryVertices'     , '', 'PAT' ), 'std::vector<reco::VertexCompositePtrCandidate>')
        self.handles  ['beamspot'   ] = AutoHandle(('offlineBeamSpot'              , '', 'RECO'), 'reco::BeamSpot'                                )
        self.handles  ['met'        ] = AutoHandle(('slimmedMETs'                  , '', 'PAT' ), 'std::vector<pat::MET>'                         )

    def assignVtx(self, particles, vtx):
        for ip in particles:
            ip.associatedVertex = vtx

    def beginLoop(self, setup):
        super(RecoGenAnalyzer, self).beginLoop(setup)
        self.counters.addCounter('RecoGenTreeAnalyzer')
        count = self.counters.counter('RecoGenTreeAnalyzer')
        count.register('all events')
 
        # stuff I need to instantiate only once
        self.vtxfit = VertexFitter()
        # create a std::vector<RecoChargedCandidate> to be passed to the fitter 
        self.tofit = ROOT.std.vector('reco::RecoChargedCandidate')()
       
    def buildDisplacedMuons(self, collection):
        muons = [DisplacedMuon(mm, collection) for mm in collection]
        return muons

    def process(self, event):
        self.readCollections(event.input)
        self.counters.counter('RecoGenTreeAnalyzer').inc('all events')

        # produce collections and map our objects to convenient Heppy objects
        event.muons       = map(Muon         , self.handles  ['muons'      ].product())
        event.electrons   = map(Electron     , self.handles  ['electrons'  ].product())
        event.photons     = map(Photon       , self.handles  ['photons'    ].product())
        event.taus        = map(Tau          , self.handles  ['taus'       ].product())
        event.jets        = map(Jet          , self.handles  ['jets'       ].product())
        event.dsmuons     = self.buildDisplacedMuons(self.handles['dsmuons'].product())
        event.dgmuons     = self.buildDisplacedMuons(self.handles['dgmuons'].product())

        # vertex stuff
        event.pvs         = self.handles['pvs'     ].product()
        event.svs         = self.handles['svs'     ].product()
        event.beamspot    = self.handles['beamspot'].product()

        # met
        event.met         = self.handles['met'].product().at(0)

        # assign to the leptons the primary vertex, will be needed to compute a few quantities
        # FIXME! understand exactly to which extent it is reasonable to assign the PV to *all* leptons
        #        regardless whether they're displaced or not
        if len(event.pvs):
            myvtx = event.pvs[0]
        else:
            myvtx = event.beamspot
        
        self.assignVtx(event.muons    , myvtx)
        self.assignVtx(event.electrons, myvtx)
        self.assignVtx(event.photons  , myvtx)
        self.assignVtx(event.taus     , myvtx)

        # all matchable objects
#         matchable = event.electrons + event.photons + event.muons + event.taus + event.dsmuons + event.dgmuons 
#         matchable = event.electrons + event.photons + event.muons + event.taus + event.dsmuons 
        # matchable = event.electrons + event.photons + event.taus + event.muons + event.dsmuons + event.dgmuons 
        matchable = event.electrons + event.photons + event.taus + event.muons
        
        #define the dr to cut on
        dr_cut = 0.2

        # match gen to reco
        for ip in [event.the_hnl.l0(), 
                   event.the_hnl.l1(), 
                   event.the_hnl.l2()]:
            ip.bestmatch     = None
            ip.bestmatchtype = None
            ip.matches = inConeCollection(ip, matchable, getattr(self.cfg_ana, 'drmax', dr_cut), 0.)

            # matches the corresponding "slimmed electron" to the gen particle
            if len(event.electrons):
                dr2 = np.inf
                match, dr2 = bestMatch(ip,event.electrons)
                if dr2 < dr_cut * dr_cut: 
                    ip.bestelectron = match

            # # matches the corresponding "slimmed photon" to the gen particle
            # if len(event.photons):
                # dr2 = np.inf
                # match, dr2 = bestMatch(ip,event.photons)
                # if dr2 < dr_cut * dr_cut: 
                    # ip.bestphoton = match

            # matches the corresponding "slimmed muon" to the gen particle
            if len(event.muons):
                dr2 = np.inf
                match, dr2 = bestMatch(ip,event.muons)
                if dr2 < dr_cut * dr_cut: 
                    ip.bestmuon = match
                    
            
            # # matches the corresponding "slimmed tau" to the gen particle
            # if len(event.taus):
                # dr2 = np.inf
                # match, dr2 = bestMatch(ip,event.taus)
                # if dr2 < dr_cut * dr_cut: 
                    # ip.besttau = match
            
            # matches the corresponding "displaced stand alone muon" to the gen particle
            if len(event.dsmuons):
                dr2 = np.inf
                match, dr2 = bestMatch(ip,event.dsmuons)
                if dr2 < dr_cut * dr_cut: 
                    ip.bestdsmuon = match
                    
            # matches the corresponding "displaced global muon" to the gen particle
            if len(event.dgmuons):
                dr2 = np.inf
                match, dr2 = bestMatch(ip,event.dgmuons)
                if dr2 < dr_cut * dr_cut: 
                    ip.bestdgmuon = match
            
            # to find the best match, give precedence to any matched 
            # particle in the matching cone with the correct PDG ID
            # then to the one which is closest
            ip.matches.sort(key = lambda x : (x.pdgId()==ip.pdgId(), -deltaR(x, ip)), reverse = True )
            
            if len(ip.matches) and abs(ip.pdgId())==abs(ip.matches[0].pdgId()):
                ip.bestmatch = ip.matches[0]
                ip.bestmatchdR = deltaR(ip,ip.bestmatch)
                # remove already matched particles, avoid multiple matches to the same candidate while recording the type of reconstruction
                matchable.remove(ip.bestmatch)

                # record which is which
                if ip.bestmatch in event.electrons: ip.bestmatchtype = 11
                if ip.bestmatch in event.photons  : ip.bestmatchtype = 22
                if ip.bestmatch in event.muons    : ip.bestmatchtype = 13
                if ip.bestmatch in event.taus     : ip.bestmatchtype = 15
                if ip.bestmatch in event.dsmuons  : ip.bestmatchtype = 26
                if ip.bestmatch in event.dgmuons  : ip.bestmatchtype = 39

            else:
                ip.bestmatchtype = -1 
    
        # clear it before doing it again
        event.recoSv = None

        # let's refit the secondary vertex, IF both leptons match to some reco particle
        pair = [event.the_hnl.l1().bestmatch, event.the_hnl.l2().bestmatch]
        if (pair[0] != None) and\
           (pair[1] != None) and\
           (pair[0].physObj != pair[1].physObj):

            event.recoSv = fitVertex(pair)

            if event.recoSv:
                # primary vertex
                pv = event.goodVertices[0]

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
                
                dilep_p4 = event.the_hnl.l1().bestmatch.p4() + event.the_hnl.l2().bestmatch.p4()

                perp = ROOT.math.XYZVector(dilep_p4.px(),
                                           dilep_p4.py(),
                                           0.)
        
                dxybs = ROOT.GlobalPoint(-1*((event.beamspot.x0() - event.recoSv.x()) + (event.recoSv.z() - event.beamspot.z0()) * event.beamspot.dxdz()), 
                                         -1*((event.beamspot.y0() - event.recoSv.y()) + (event.recoSv.z() - event.beamspot.z0()) * event.beamspot.dydz()),
                                          0)
        
                vperp = ROOT.math.XYZVector(dxybs.x(), dxybs.y(), 0.)
        
                cos = vperp.Dot(perp)/(vperp.R()*perp.R())
                
                event.recoSv.disp2DFromBS_cos = cos
    
        return True
    
