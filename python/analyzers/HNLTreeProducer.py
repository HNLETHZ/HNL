import ROOT
import numpy as np
from CMGTools.HNL.analyzers.TreeProducerBase import TreeProducerBase
from PhysicsTools.HeppyCore.utils.deltar import deltaR, bestMatch
from CMGTools.HNL.utils.utils import isAncestor, displacement2D, displacement3D, makeRecoVertex # utility functions
from pdb import set_trace

class HNLTreeProducer(TreeProducerBase):
    '''
    RM: add more info:
    - gen impact parameter  ==> how to do it at gen level?
    - gen met including pu (all neutrinos)
    - di-lepton isolation
    make this iherit from a common reco tree producer, then specialise by lepton flavour
    '''
    def declareVariables(self, setup):
        '''
        '''
        # event variables
        self.bookEvent(self.tree)
        self.var      (self.tree, 'n_cands')
        self.var      (self.tree, 'rho')
        self.var      (self.tree, 'nLeptons')
        self.var      (self.tree, 'nElectrons')
        self.var      (self.tree, 'nMuons')
        
        # reco variables
        self.bookHNL (self.tree, 'hnl')
        self.var     (self.tree, 'hnl_iso03_abs_rhoArea')
        self.var     (self.tree, 'hnl_iso04_abs_rhoArea')
        self.var     (self.tree, 'hnl_iso05_abs_rhoArea')
        self.var     (self.tree, 'hnl_iso03_abs_deltaBeta')
        self.var     (self.tree, 'hnl_iso04_abs_deltaBeta')
        self.var     (self.tree, 'hnl_iso05_abs_deltaBeta')
#        self.var     (self.tree, 'hnl_iso_abs_met')
        self.var     (self.tree, 'hnl_iso03_rel_rhoArea')
        self.var     (self.tree, 'hnl_iso04_rel_rhoArea')
        self.var     (self.tree, 'hnl_iso05_rel_rhoArea')
        self.var     (self.tree, 'hnl_iso03_rel_deltaBeta')
        self.var     (self.tree, 'hnl_iso04_rel_deltaBeta')
        self.var     (self.tree, 'hnl_iso05_rel_deltaBeta')
#        self.var     (self.tree, 'hnl_iso_rel_met')
        
        if   self.cfg_ana.promptLepType == 'ele':
            self.bookEle (self.tree, 'l0')
            self.var(self.tree, 'hlt_Ele27_WPTight_Gsf'        )
            self.var(self.tree, 'hlt_Ele32_WPTight_Gsf'        )
            self.var(self.tree, 'hlt_Ele35_WPTight_Gsf'        )
            self.var(self.tree, 'hlt_Ele115_CaloIdVT_GsfTrkIdT')
            self.var(self.tree, 'hlt_Ele135_CaloIdVT_GsfTrkIdT')

        elif self.cfg_ana.promptLepType == 'mu':
            self.bookMuon(self.tree, 'l0')
            self.var(self.tree, 'hlt_IsoMu24'                   )
            self.var(self.tree, 'hlt_IsoMu27'                   )
            self.var(self.tree, 'hlt_Mu50'                      )
        else:
             print 'ERROR: prompt lepton type non specified or missing! Exit'
             exit(0)

        if self.cfg_ana.L1L2LeptonType == 'mm':
            self.bookMuon(self.tree, 'l1' )
            self.bookMuon(self.tree, 'l2' )
        if self.cfg_ana.L1L2LeptonType == 'ee':
            self.bookEle(self.tree, 'l1'  )
            self.bookEle(self.tree, 'l2'  )
        if self.cfg_ana.L1L2LeptonType == 'em':
            self.bookEle(self.tree, 'l1'  )
            self.bookMuon(self.tree, 'l2' )
        
        # book the matched  gen particle
        self.bookSimpleGenParticle(self.tree, 'l0_gen_match')
        self.bookSimpleGenParticle(self.tree, 'l1_gen_match')
        self.bookSimpleGenParticle(self.tree, 'l2_gen_match')

        # relevant for signal: check if reco matched with gen, save a bool
        self.var(self.tree, 'l0_is_real')
        self.var(self.tree, 'l1_is_real')
        self.var(self.tree, 'l2_is_real')

        self.var(self.tree, 'l0_good_match')
        self.var(self.tree, 'l1_good_match')
        self.var(self.tree, 'l2_good_match')

        # reco primary vertex
        self.var(self.tree, 'pv_x')
        self.var(self.tree, 'pv_y')
        self.var(self.tree, 'pv_z')
        self.var(self.tree, 'pv_xe')
        self.var(self.tree, 'pv_ye')
        self.var(self.tree, 'pv_ze')

        # beamspot
        self.var(self.tree, 'bs_x')
        self.var(self.tree, 'bs_y')
        self.var(self.tree, 'bs_z')
        self.var(self.tree, 'bs_sigma_x')
        self.var(self.tree, 'bs_sigma_y')
        self.var(self.tree, 'bs_sigma_z')
        self.var(self.tree, 'bs_dxdz')
        self.var(self.tree, 'bs_dydz')
        
        # reco HN decay vertex (when present)
        self.bookVertex(self.tree, 'sv')

        # # reco HN decay vertex (when present)
        # self.var(self.tree, 'sv_x' )
        # self.var(self.tree, 'sv_y' )
        # self.var(self.tree, 'sv_z' )
        # self.var(self.tree, 'sv_xe')
        # self.var(self.tree, 'sv_ye')
        # self.var(self.tree, 'sv_ze')
        # self.var(self.tree, 'sv_prob')
        # self.var(self.tree, 'sv_cos')

        # lepton vetoes
        self.var(self.tree, 'pass_e_veto')
        self.var(self.tree, 'pass_m_veto')

        # save vetoing lepton
        self.bookEle(self.tree, 'veto_ele')
        self.bookMuon(self.tree, 'veto_mu')
    
        # invariant masses with vetoing leptons
        self.var(self.tree, 'hnl_m_0Vele')
        self.var(self.tree, 'hnl_m_1Vele')
        self.var(self.tree, 'hnl_m_2Vele')
        self.var(self.tree, 'hnl_m_0Vmu')
        self.var(self.tree, 'hnl_m_1Vmu')
        self.var(self.tree, 'hnl_m_2Vmu')
        
        # gen level particles
        self.bookHNL     (self.tree, 'hnl_gen')
        self.bookParticle(self.tree, 'l0_gen' )
        self.bookParticle(self.tree, 'l1_gen' )
        self.bookParticle(self.tree, 'l2_gen' )
        self.bookParticle(self.tree, 'n_gen'  )

        # gen primary vertex
        self.var(self.tree, 'pv_gen_x')
        self.var(self.tree, 'pv_gen_y')
        self.var(self.tree, 'pv_gen_z')

        # gen HN decay vertex
        self.var(self.tree, 'sv_gen_x')
        self.var(self.tree, 'sv_gen_y')
        self.var(self.tree, 'sv_gen_z')

        # displacements
        self.var(self.tree, 'hnl_2d_gen_disp')
        self.var(self.tree, 'hnl_3d_gen_disp')

        self.var(self.tree, 'hnl_2d_disp')
        self.var(self.tree, 'hnl_3d_disp')

        self.var(self.tree, 'hnl_2d_disp_sig')
        self.var(self.tree, 'hnl_3d_disp_sig')

        # met information
        self.bookExtraMetInfo(self.tree)

        self.var(self.tree, 'Flag_goodVertices')
        self.var(self.tree, 'Flag_globalSuperTightHalo2016Filter')
        self.var(self.tree, 'Flag_HBHENoiseFilter')
        self.var(self.tree, 'Flag_HBHENoiseIsoFilter')
        self.var(self.tree, 'Flag_EcalDeadCellTriggerPrimitiveFilter')
        self.var(self.tree, 'Flag_BadPFMuonFilter')
        self.var(self.tree, 'Flag_BadChargedCandidateFilter')
        self.var(self.tree, 'Flag_eeBadScFilter')
        self.var(self.tree, 'Flag_ecalBadCalibFilter')
#        self.var(self.tree, 'Flag_any_met_filters')
        
        # jet information
        self.bookJet(self.tree, 'j1' , fill_extra=False)
        self.bookJet(self.tree, 'j2' , fill_extra=False)
        self.bookJet(self.tree, 'bj1', fill_extra=False)
        self.bookJet(self.tree, 'bj2', fill_extra=False)
        self.var(self.tree, 'htj' )
        self.var(self.tree, 'htbj')
        self.var(self.tree, 'nj'  )
        self.var(self.tree, 'nbj' )
        
        # LHE weight
        self.var(self.tree, 'lhe_weight')

    def process(self, event):
        '''
        '''
        self.readCollections(event.input)
        self.tree.reset()
        # event variables 
        self.fillEvent(self.tree, event)
        self.fill     (self.tree, 'n_cands', len(event.dileptonsvtx))
        self.fill     (self.tree, 'rho'    , event.rho)
        self.fill     (self.tree, 'nLeptons'    , event.nLeptons)
        self.fill     (self.tree, 'nElectrons'  , event.nElectrons)
        self.fill     (self.tree, 'nMuons'    , event.nMuons)

        # reco HNL
        self.fillHNL (self.tree, 'hnl'                  , event.the_3lep_cand                 )
        # FIXME: one day, move all those single variables into groups like bookHNL/fillHNL
        self.fill    (self.tree, 'hnl_iso03_abs_rhoArea', event.the_3lep_cand.abs_tot_iso03_rhoArea)
        self.fill    (self.tree, 'hnl_iso04_abs_rhoArea', event.the_3lep_cand.abs_tot_iso04_rhoArea)
        self.fill    (self.tree, 'hnl_iso05_abs_rhoArea', event.the_3lep_cand.abs_tot_iso05_rhoArea)
        self.fill    (self.tree, 'hnl_iso03_abs_deltaBeta', event.the_3lep_cand.abs_tot_iso03_deltaBeta)
        self.fill    (self.tree, 'hnl_iso04_abs_deltaBeta', event.the_3lep_cand.abs_tot_iso04_deltaBeta)
        self.fill    (self.tree, 'hnl_iso05_abs_deltaBeta', event.the_3lep_cand.abs_tot_iso05_deltaBeta)
#        self.fill    (self.tree, 'hnl_iso_abs_met'      , event.the_3lep_cand.abs_ch_iso_met  )
        self.fill    (self.tree, 'hnl_iso03_rel_rhoArea', event.the_3lep_cand.rel_tot_iso03_rhoArea)
        self.fill    (self.tree, 'hnl_iso04_rel_rhoArea', event.the_3lep_cand.rel_tot_iso04_rhoArea)
        self.fill    (self.tree, 'hnl_iso05_rel_rhoArea', event.the_3lep_cand.rel_tot_iso05_rhoArea)
        self.fill    (self.tree, 'hnl_iso03_rel_deltaBeta', event.the_3lep_cand.rel_tot_iso03_deltaBeta)
        self.fill    (self.tree, 'hnl_iso04_rel_deltaBeta', event.the_3lep_cand.rel_tot_iso04_deltaBeta)
        self.fill    (self.tree, 'hnl_iso05_rel_deltaBeta', event.the_3lep_cand.rel_tot_iso05_deltaBeta)
#        self.fill    (self.tree, 'hnl_iso_rel_met'      , event.the_3lep_cand.rel_ch_iso_met  )
        if self.cfg_ana.L1L2LeptonType == 'mm':
            self.fillMuon(self.tree, 'l1'                   , event.the_3lep_cand.l1()            )
            self.fillMuon(self.tree, 'l2'                   , event.the_3lep_cand.l2()            )
        if self.cfg_ana.L1L2LeptonType == 'ee':
            self.fillEle(self.tree, 'l1'                   , event.the_3lep_cand.l1()            )
            self.fillEle(self.tree, 'l2'                   , event.the_3lep_cand.l2()            )
        if self.cfg_ana.L1L2LeptonType == 'em':
            self.fillEle(self.tree, 'l1'                   , event.the_3lep_cand.l1()            )
            self.fillMuon(self.tree, 'l2'                   , event.the_3lep_cand.l2()            )


        if self.cfg_ana.promptLepType == 'ele' :       self.fillEle (self.tree, 'l0', event.the_3lep_cand.l0())
        if self.cfg_ana.promptLepType == 'mu'  :       self.fillMuon(self.tree, 'l0', event.the_3lep_cand.l0())

        # output of MC analysis ONLY FOR SIGNAL
        if hasattr(event, 'the_hnl'):
            self.fillHNL     (self.tree, 'hnl_gen', event.the_hnl      )
            self.fillParticle(self.tree, 'l0_gen' , event.the_hnl.l0() )
            self.fillParticle(self.tree, 'l1_gen' , event.the_hnl.l1() )
            self.fillParticle(self.tree, 'l2_gen' , event.the_hnl.l2() )
            self.fillParticle(self.tree, 'n_gen'  , event.the_hnl.met())

        # reco primary vertex
        pv = event.goodVertices[0]
        self.fill(self.tree, 'pv_x' , pv.x())
        self.fill(self.tree, 'pv_y' , pv.y())
        self.fill(self.tree, 'pv_z' , pv.z())
        self.fill(self.tree, 'pv_xe', pv.xError())
        self.fill(self.tree, 'pv_ye', pv.yError())
        self.fill(self.tree, 'pv_ze', pv.zError())
        
        # true primary vertex
        if hasattr(event, 'the_hnl'):
            self.fill(self.tree, 'pv_gen_x', event.the_hn.vx())
            self.fill(self.tree, 'pv_gen_y', event.the_hn.vy())
            self.fill(self.tree, 'pv_gen_z', event.the_hn.vz())

        # beamspot
        self.fill(self.tree, 'bs_x', event.beamspot.x0())
        self.fill(self.tree, 'bs_y', event.beamspot.y0())
        self.fill(self.tree, 'bs_z', event.beamspot.z0())
        self.fill(self.tree, 'bs_sigma_x', event.beamspot.BeamWidthX())
        self.fill(self.tree, 'bs_sigma_y', event.beamspot.BeamWidthY())
        self.fill(self.tree, 'bs_sigma_z', event.beamspot.sigmaZ())
        self.fill(self.tree, 'bs_dxdz', event.beamspot.dxdz())
        self.fill(self.tree, 'bs_dydz', event.beamspot.dydz())

        # true HN decay vertex
        if hasattr(event, 'the_hn'):
            self.fill(self.tree, 'sv_gen_x', event.the_hn.lep1.vertex().x()) # don't use the final lepton to get the vertex from!
            self.fill(self.tree, 'sv_gen_y', event.the_hn.lep1.vertex().y()) # don't use the final lepton to get the vertex from!
            self.fill(self.tree, 'sv_gen_z', event.the_hn.lep1.vertex().z()) # don't use the final lepton to get the vertex from!

            # displacements
            self.fill(self.tree, 'hnl_2d_gen_disp', displacement2D(event.the_hn.lep1, event.the_hn))
            self.fill(self.tree, 'hnl_3d_gen_disp', displacement3D(event.the_hn.lep1, event.the_hn))

        # HLT bits & matches
        trig_list = [trig.name for trig in event.trigger_infos if trig.fired]
        if self.cfg_ana.promptLepType == 'ele':
            self.fill(self.tree, 'hlt_Ele27_WPTight_Gsf'               , any('HLT_Ele27_WPTight_Gsf'                 in name for name in trig_list))
            self.fill(self.tree, 'hlt_Ele32_WPTight_Gsf'               , any('HLT_Ele32_WPTight_Gsf'                 in name for name in trig_list))
            self.fill(self.tree, 'hlt_Ele35_WPTight_Gsf'               , any('HLT_Ele35_WPTight_Gsf'                 in name for name in trig_list))
            self.fill(self.tree, 'hlt_Ele115_CaloIdVT_GsfTrkIdT'       , any('HLT_Ele115_CaloIdVT_GsfTrkIdT'         in name for name in trig_list))
            self.fill(self.tree, 'hlt_Ele135_CaloIdVT_GsfTrkIdT'       , any('HLT_Ele135_CaloIdVT_GsfTrkIdT'         in name for name in trig_list))
        if self.cfg_ana.promptLepType == 'mu':
            self.fill(self.tree, 'hlt_IsoMu24'                          , any('HLT_IsoMu24'                           in name for name in trig_list))
            self.fill(self.tree, 'hlt_IsoMu27'                          , any('HLT_IsoMu27'                           in name for name in trig_list))
            self.fill(self.tree, 'hlt_Mu50'                             , any('HLT_Mu50'                              in name for name in trig_list))
    
        
        # reco secondary vertex and displacement
        self.fillVertex(self.tree, 'sv' , event.recoSv)

        # # reco secondary vertex and displacement
        # self.fill(self.tree, 'sv_x'   , event.recoSv.x()             )
        # self.fill(self.tree, 'sv_y'   , event.recoSv.y()             )
        # self.fill(self.tree, 'sv_z'   , event.recoSv.z()             )
        # self.fill(self.tree, 'sv_xe'  , event.recoSv.xError()        )
        # self.fill(self.tree, 'sv_ye'  , event.recoSv.yError()        )
        # self.fill(self.tree, 'sv_ze'  , event.recoSv.zError()        )
        # self.fill(self.tree, 'sv_prob', event.recoSv.prob            )
        # self.fill(self.tree, 'sv_cos' , event.recoSv.disp2DFromBS_cos)
    
        self.fill(self.tree, 'hnl_2d_disp', event.recoSv.disp2DFromBS.value()) # from beamspot
        self.fill(self.tree, 'hnl_3d_disp', event.recoSv.disp3DFromBS.value()) # from PV
    
        self.fill(self.tree, 'hnl_2d_disp_sig', event.recoSv.disp2DFromBS_sig) # from beamspot
        self.fill(self.tree, 'hnl_3d_disp_sig', event.recoSv.disp3DFromBS_sig) # from PV

        # jet/met variables
        self.fillExtraMetInfo(self.tree, event)

#        set_trace()
        # met filter flags
        self.fill(self.tree, 'Flag_goodVertices'                      , event.Flag_goodVertices                      )
        self.fill(self.tree, 'Flag_globalSuperTightHalo2016Filter'    , event.Flag_globalSuperTightHalo2016Filter    )
        self.fill(self.tree, 'Flag_HBHENoiseFilter'                   , event.Flag_HBHENoiseFilter                   )
        self.fill(self.tree, 'Flag_HBHENoiseIsoFilter'                , event.Flag_HBHENoiseIsoFilter                )
        self.fill(self.tree, 'Flag_EcalDeadCellTriggerPrimitiveFilter', event.Flag_EcalDeadCellTriggerPrimitiveFilter)
        self.fill(self.tree, 'Flag_BadPFMuonFilter'                   , event.Flag_BadPFMuonFilter                   )
        self.fill(self.tree, 'Flag_BadChargedCandidateFilter'         , event.Flag_BadChargedCandidateFilter         )
        self.fill(self.tree, 'Flag_eeBadScFilter'                     , event.Flag_eeBadScFilter                     )
        self.fill(self.tree, 'Flag_ecalBadCalibFilter'                , event.Flag_ecalBadCalibFilter                )
#        self.fill(self.tree, 'Flag_any_met_filters', event.Flag_goodVertices or event.Flag_globalSuperTightHalo2016Filter or event.Flag_HBHENoiseFilter or event.Flag_HBHENoiseIsoFilter or event.Flag_EcalDeadCellTriggerPrimitiveFilter or event.Flag_BadPFMuonFilter or event.Flag_BadChargedCandidateFilter or event.Flag_eeBadScFilter or event.Flag_ecalBadCalibFilter)

        if len(event.cleanJets )>0: self.fillJet(self.tree, 'j1' , event.cleanJets [0], fill_extra=False)
        if len(event.cleanJets )>1: self.fillJet(self.tree, 'j2' , event.cleanJets [1], fill_extra=False)
        if len(event.cleanBJets)>0: self.fillJet(self.tree, 'bj1', event.cleanBJets[0], fill_extra=False)
        if len(event.cleanBJets)>1: self.fillJet(self.tree, 'bj2', event.cleanBJets[1], fill_extra=False)

        self.fill(self.tree, 'htj' , event.HT_cleanJets   )
        self.fill(self.tree, 'htbj', event.HT_bJets       )
        self.fill(self.tree, 'nj'  , len(event.cleanJets) )
        self.fill(self.tree, 'nbj' , len(event.cleanBJets))

        # gen match
        if self.cfg_comp.isMC == True and hasattr(event, 'genParticles'):
            stable_genp   =  [pp for pp in event.genParticles if pp.status() == 1] # and pp.vertex().z()!=0)]
            stable_genp   += [pp for pp in event.genp_packed  if pp.status() == 1] # and pp.vertex().z()!=0)] 
            # particle status: http://home.thep.lu.se/~torbjorn/pythia81html/ParticleProperties.html
            # 1 ... stable; 23 ... from hardest scattering subprocess
#            stable_genp += [pp for pp in event.genParticles if (pp.status()==23  and pp.vertex().z()!=0)]
#            stable_genp += [pp for pp in event.genp_packed  if (pp.status()==23  and pp.vertex().z()!=0)] 
        
            tomatch = [(event.the_3lep_cand.l0(), 0.05*0.05),
                       (event.the_3lep_cand.l1(), 0.2 *0.2 ),
                       (event.the_3lep_cand.l2(), 0.2 *0.2 )]
        
            for ilep, idr2 in tomatch:
                bestmatch, dr2 = bestMatch(ilep, stable_genp)
                if (dr2 < idr2 and abs((ilep.pt() - bestmatch.pt())/ilep.pt()) < 0.2 ): 
                    ilep.bestmatch = bestmatch

            # relevant for mc: check if reco matched with gen, save a float
            if hasattr(event.the_3lep_cand.l0(), 'bestmatch'):
                LEP0 = event.the_3lep_cand.l0()
                self.fillSimpleGenParticle(self.tree, 'l0_gen_match', LEP0.bestmatch)
                self.fill(self.tree, 'l0_good_match', deltaR(LEP0.bestmatch, LEP0))
#                if deltaR(LEP0.bestmatch, LEP0) < 0.04 and LEP0.pdgId() == LEP0.bestmatch.pdgId():
#                    self.fill(self.tree, 'l0_good_match', 1)


            if hasattr(event.the_3lep_cand.l1(), 'bestmatch'):
                LEP1 = event.the_3lep_cand.l1()
                self.fillSimpleGenParticle(self.tree, 'l1_gen_match', LEP1.bestmatch)
                self.fill(self.tree, 'l1_good_match', deltaR(LEP1.bestmatch, LEP1))
#                if deltaR(LEP1.bestmatch, LEP1) < 0.04 and LEP1.pdgId() == LEP1.bestmatch.pdgId():
#                    self.fill(self.tree, 'l1_good_match', 1)


            if hasattr(event.the_3lep_cand.l2(), 'bestmatch'):
                LEP2 = event.the_3lep_cand.l2()
                self.fillSimpleGenParticle(self.tree, 'l2_gen_match', LEP2.bestmatch)
                self.fill(self.tree, 'l2_good_match', deltaR(LEP2.bestmatch, LEP2))
#                if deltaR(LEP2.bestmatch, LEP2) < 0.04 and LEP2.pdgId() == LEP2.bestmatch.pdgId():
#                    self.fill(self.tree, 'l2_good_match', 1)

            # matching by pointer does not work, so let's trick it with deltaR
            if hasattr(event, 'the_hnl'):
                if hasattr(event.the_3lep_cand.l0(), 'bestmatch'): self.fill(self.tree, 'l0_is_real', deltaR(event.the_3lep_cand.l0().bestmatch,event.the_hnl.l0()) < 0.01)
                if hasattr(event.the_3lep_cand.l1(), 'bestmatch'): self.fill(self.tree, 'l1_is_real', deltaR(event.the_3lep_cand.l1().bestmatch,event.the_hnl.l1()) < 0.05)
                if hasattr(event.the_3lep_cand.l2(), 'bestmatch'): self.fill(self.tree, 'l2_is_real', deltaR(event.the_3lep_cand.l2().bestmatch,event.the_hnl.l2()) < 0.05)

            print('event:', event.eventId, 'lumi:', event.lumi)

        # extra lepton veto
        self.fill(self.tree, 'pass_e_veto', len(event.veto_eles)==0)
        self.fill(self.tree, 'pass_m_veto', len(event.veto_mus )==0)

        # save vetoing lepton invariant masses
        if len(event.veto_eles):
                self.fillEle(self.tree, 'veto_ele', event.veto_save_ele)
                self.fill(self.tree, 'hnl_m_0Vele', (event.veto_save_ele.p4() + event.the_3lep_cand.l0().p4()).mass())
                self.fill(self.tree, 'hnl_m_1Vele', (event.veto_save_ele.p4() + event.the_3lep_cand.l1().p4()).mass())
                self.fill(self.tree, 'hnl_m_2Vele', (event.veto_save_ele.p4() + event.the_3lep_cand.l2().p4()).mass())
        if len(event.veto_mus):
                self.fillMuon(self.tree, 'veto_mu', event.veto_save_mu)
                self.fill(self.tree, 'hnl_m_0Vmu', (event.veto_save_mu.p4() + event.the_3lep_cand.l0().p4()).mass())
                self.fill(self.tree, 'hnl_m_1Vmu', (event.veto_save_mu.p4() + event.the_3lep_cand.l1().p4()).mass())
                self.fill(self.tree, 'hnl_m_2Vmu', (event.veto_save_mu.p4() + event.the_3lep_cand.l2().p4()).mass())
        # LHE weight
        self.fill(self.tree, 'lhe_weight', np.sign(getattr(event, 'LHE_originalWeight', 1.)))
                
        self.fillTree(event)


