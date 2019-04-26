import ROOT
from CMGTools.HNL.analyzers.TreeProducerBase import TreeProducerBase
from PhysicsTools.HeppyCore.utils.deltar import deltaR
from CMGTools.HNL.utils.utils import isAncestor, displacement2D, displacement3D, makeRecoVertex # utility functions
from pdb import set_trace

class HNLTreeProducer(TreeProducerBase):
    '''
    '''
    def declareVariables(self, setup):
        '''
        '''
        # output for reco analysis
        self.bookEvent(self.tree)
                
        self.var(self.tree, 'n_cands')

#         self.bookHNCandidate(self.tree, 'hnl_minchi2'    )
#         self.bookHNCandidate(self.tree, 'hnl_maxpt'      )
#         self.bookHNCandidate(self.tree, 'hnl_mindr'      )
#         self.bookHNCandidate(self.tree, 'hnl_maxdphi'    )
#         self.bookHNCandidate(self.tree, 'hnl_mindeta'    )
#         self.bookHNCandidate(self.tree, 'hnl_maxdisp2dbs')
#         self.bookHNCandidate(self.tree, 'hnl_maxdisp2dpv')
#         self.bookHNCandidate(self.tree, 'hnl_maxdisp3dpv')
#         self.bookHNCandidate(self.tree, 'hnl_maxdls2dbs' )
#         self.bookHNCandidate(self.tree, 'hnl_maxdls2dpv' )
#         self.bookHNCandidate(self.tree, 'hnl_maxdls3dpv' )
        self.bookHNCandidate(self.tree, 'hnl_maxcos'     )

        self.bookParticle(self.tree, 'mu1')
        self.var(self.tree, 'mu1_type')
        self.bookParticle(self.tree, 'mu2')
        self.var(self.tree, 'mu2_type')

        # output for mc analysis
        # the W->lN, N->llnu candidate
        self.bookHNL(self.tree, 'hnl')

        # the prompt lepton
        self.bookParticle(self.tree, 'l0')
        self.bookEle      (self.tree, 'l0_matched_electron'    )
        self.bookPhoton   (self.tree, 'l0_matched_photon'      )
        self.bookMuon     (self.tree, 'l0_matched_muon'        )
        self.bookMuonTrack(self.tree, 'l0_matched_muon_track'  )
        self.bookTau      (self.tree, 'l0_matched_tau'         )
        self.bookParticle (self.tree, 'l0_matched_dsmuon'      )
        self.bookMuonTrack(self.tree, 'l0_matched_dsmuon_track')
        self.bookParticle (self.tree, 'l0_matched_dgmuon'      )
        self.bookMuonTrack(self.tree, 'l0_matched_dgmuon_track')
        self.bookParticle (self.tree, 'l0_bestmatch'           )
        self.var(self.tree, 'l0_bestmatch_type')
       

        # displaced leptons (from the HN)
        self.bookParticle(self.tree, 'l1')
        self.bookEle      (self.tree, 'l1_matched_electron'    )
        self.bookPhoton   (self.tree, 'l1_matched_photon'      )
        self.bookMuon     (self.tree, 'l1_matched_muon'        )
        self.bookMuonTrack(self.tree, 'l1_matched_muon_track'  )
        self.bookTau      (self.tree, 'l1_matched_tau'         )
        self.bookParticle (self.tree, 'l1_matched_dsmuon'      )
        self.bookMuonTrack(self.tree, 'l1_matched_dsmuon_track')
        self.bookParticle (self.tree, 'l1_matched_dgmuon'      )
        self.bookMuonTrack(self.tree, 'l1_matched_dgmuon_track')
        self.bookParticle (self.tree, 'l1_bestmatch'           )
        self.var(self.tree, 'l1_bestmatch_type')

        self.bookParticle(self.tree, 'l2')
        self.bookEle      (self.tree, 'l2_matched_electron'    )
        self.bookPhoton   (self.tree, 'l2_matched_photon'      )
        self.bookMuon     (self.tree, 'l2_matched_muon'        )
        self.bookMuonTrack(self.tree, 'l2_matched_muon_track'  )
        self.bookTau      (self.tree, 'l2_matched_tau'         )
        self.bookParticle (self.tree, 'l2_matched_dsmuon'      )
        self.bookMuonTrack(self.tree, 'l2_matched_dsmuon_track')
        self.bookParticle (self.tree, 'l2_matched_dgmuon'      )
        self.bookMuonTrack(self.tree, 'l2_matched_dgmuon_track')
        self.bookParticle (self.tree, 'l2_bestmatch'           )
        self.var(self.tree, 'l2_bestmatch_type')

        # final neutrino
        self.bookGenParticle(self.tree, 'n')

        # true primary vertex
        self.var(self.tree, 'pv_x')
        self.var(self.tree, 'pv_y')
        self.var(self.tree, 'pv_z')

        # true HN decay vertex
        self.var(self.tree, 'sv_x')
        self.var(self.tree, 'sv_y')
        self.var(self.tree, 'sv_z')
        
        # reco HN decay vertex (when present)
        self.var(self.tree, 'sv_reco_x' )
        self.var(self.tree, 'sv_reco_y' )
        self.var(self.tree, 'sv_reco_z' )
        self.var(self.tree, 'sv_reco_xe')
        self.var(self.tree, 'sv_reco_ye')
        self.var(self.tree, 'sv_reco_ze')
        self.var(self.tree, 'sv_reco_prob')
        self.var(self.tree, 'sv_reco_cos')

        # displacements
        self.var(self.tree, 'hnl_2d_disp')
        self.var(self.tree, 'hnl_3d_disp')

        self.var(self.tree, 'hnl_2d_reco_disp')
        self.var(self.tree, 'hnl_3d_reco_disp')

        self.var(self.tree, 'hnl_2d_reco_disp_sig')
        self.var(self.tree, 'hnl_3d_reco_disp_sig')

        # flag if the event is in CMS acceptance |eta|<2.5
        self.var(self.tree, 'is_in_acc')

    def process(self, event):
        '''
        '''
        self.readCollections(event.input)
        self.tree.reset()

        # output of reco analysis
        self.fillEvent(self.tree, event)

        self.fill(self.tree, 'n_cands', len(event.dimuonsvtx))

        # different candidates
        if len(event.dimuonsvtx):
#             self.fillHNCandidate(self.tree, 'hnl_minchi2'    , event.hnl_minchi2    )
#             self.fillHNCandidate(self.tree, 'hnl_maxpt'      , event.hnl_maxpt      )
#             self.fillHNCandidate(self.tree, 'hnl_mindr'      , event.hnl_mindr      )
#             self.fillHNCandidate(self.tree, 'hnl_maxdphi'    , event.hnl_maxdphi    )
#             self.fillHNCandidate(self.tree, 'hnl_mindeta'    , event.hnl_mindeta    )
#             self.fillHNCandidate(self.tree, 'hnl_maxdisp2dbs', event.hnl_maxdisp2dbs)
#             self.fillHNCandidate(self.tree, 'hnl_maxdisp2dpv', event.hnl_maxdisp2dpv)
#             self.fillHNCandidate(self.tree, 'hnl_maxdisp3dpv', event.hnl_maxdisp3dpv)
#             self.fillHNCandidate(self.tree, 'hnl_maxdls2dbs' , event.hnl_maxdls2dbs )
#             self.fillHNCandidate(self.tree, 'hnl_maxdls2dpv' , event.hnl_maxdls2dpv )
#             self.fillHNCandidate(self.tree, 'hnl_maxdls3dpv' , event.hnl_maxdls3dpv )
            self.fillHNCandidate(self.tree, 'hnl_maxcos'     , event.hnl_maxcos     )
                        
            self.fillParticle(self.tree, 'mu1', event.hnl_maxcos.lep1())
            self.fill(self.tree, 'mu1_type', event.hnl_maxcos.lep1().type)
            self.fillParticle(self.tree, 'mu2', event.hnl_maxcos.lep2())
            self.fill(self.tree, 'mu2_type', event.hnl_maxcos.lep2().type)


        # output of MC analysis
        self.fillHNL(self.tree, 'hnl', event.the_hnl)

        # the prompt lepton
        self.fillParticle(self.tree, 'l0' , event.the_hnl.l0())
        if hasattr(event.the_hnl.l0(), 'bestelectron'): self.fillEle     (self.tree, 'l0_matched_electron', event.the_hnl.l0().bestelectron)
        if hasattr(event.the_hnl.l0(), 'bestphoton'  ): self.fillPhoton  (self.tree, 'l0_matched_photon'  , event.the_hnl.l0().bestphoton  )
        if hasattr(event.the_hnl.l0(), 'bestmuon'    ): self.fillMuon    (self.tree, 'l0_matched_muon'    , event.the_hnl.l0().bestmuon    ) ; self.fillMuonTrack(self.tree, 'l0_matched_muon_track', event.the_hnl.l0().bestmuon.bestTrack())
        if hasattr(event.the_hnl.l0(), 'besttau'     ): self.fillTau     (self.tree, 'l0_matched_tau'     , event.the_hnl.l0().besttau     )
        if hasattr(event.the_hnl.l0(), 'bestdsmuon'  ): self.fillParticle(self.tree, 'l0_matched_dsmuon'  , event.the_hnl.l0().bestdsmuon  ) ; self.fillMuonTrack(self.tree, 'l0_matched_dsmuon_track', event.the_hnl.l0().bestdsmuon )
        if hasattr(event.the_hnl.l0(), 'bestdgmuon'  ): self.fillParticle(self.tree, 'l0_matched_dgmuon'  , event.the_hnl.l0().bestdgmuon  ) ; self.fillMuonTrack(self.tree, 'l0_matched_dgmuon_track', event.the_hnl.l0().bestdgmuon )
        if event.the_hnl.l0().bestmatch != None: self.fillParticle(self.tree, 'l0_bestmatch'       , event.the_hnl.l0().bestmatch   )
        self.fill(self.tree, 'l0_bestmatch_type',event.the_hnl.l0().bestmatchtype)
        
        # displaced leptons (from the HN)
        self.fillParticle(self.tree, 'l1', event.the_hnl.l1())
        if hasattr(event.the_hnl.l1(), 'bestelectron'): self.fillEle     (self.tree, 'l1_matched_electron', event.the_hnl.l1().bestelectron)
        if hasattr(event.the_hnl.l1(), 'bestphoton'  ): self.fillPhoton  (self.tree, 'l1_matched_photon'  , event.the_hnl.l1().bestphoton  )
        if hasattr(event.the_hnl.l1(), 'bestmuon'    ): self.fillMuon    (self.tree, 'l1_matched_muon'    , event.the_hnl.l1().bestmuon    ) ; self.fillMuonTrack(self.tree, 'l1_matched_muon_track', event.the_hnl.l1().bestmuon.bestTrack())        
        if hasattr(event.the_hnl.l1(), 'besttau'     ): self.fillTau     (self.tree, 'l1_matched_tau'     , event.the_hnl.l1().besttau     )
        if hasattr(event.the_hnl.l1(), 'bestdsmuon'  ): self.fillParticle(self.tree, 'l1_matched_dsmuon'  , event.the_hnl.l1().bestdsmuon  ) ; self.fillMuonTrack(self.tree, 'l1_matched_dsmuon_track', event.the_hnl.l1().bestdsmuon )
        if hasattr(event.the_hnl.l1(), 'bestdgmuon'  ): self.fillParticle(self.tree, 'l1_matched_dgmuon'  , event.the_hnl.l1().bestdgmuon  ) ; self.fillMuonTrack(self.tree, 'l1_matched_dgmuon_track', event.the_hnl.l1().bestdgmuon )
        if event.the_hnl.l1().bestmatch != None: self.fillParticle(self.tree, 'l1_bestmatch'       , event.the_hnl.l1().bestmatch   )
        self.fill(self.tree, 'l1_bestmatch_type',event.the_hnl.l1().bestmatchtype)

        self.fillParticle(self.tree, 'l2', event.the_hnl.l2())
        if hasattr(event.the_hnl.l2(), 'bestelectron'): self.fillEle     (self.tree, 'l2_matched_electron', event.the_hnl.l2().bestelectron)
        if hasattr(event.the_hnl.l2(), 'bestphoton'  ): self.fillPhoton  (self.tree, 'l2_matched_photon'  , event.the_hnl.l2().bestphoton  )
        if hasattr(event.the_hnl.l2(), 'bestmuon'    ): self.fillMuon    (self.tree, 'l2_matched_muon'    , event.the_hnl.l2().bestmuon    ) ; self.fillMuonTrack(self.tree, 'l2_matched_muon_track', event.the_hnl.l2().bestmuon.bestTrack())        
        if hasattr(event.the_hnl.l2(), 'besttau'     ): self.fillTau     (self.tree, 'l2_matched_tau'     , event.the_hnl.l2().besttau     )
        if hasattr(event.the_hnl.l2(), 'bestdsmuon'  ): self.fillParticle(self.tree, 'l2_matched_dsmuon'  , event.the_hnl.l2().bestdsmuon  ) ; self.fillMuonTrack(self.tree, 'l2_matched_dsmuon_track', event.the_hnl.l2().bestdsmuon )
        if hasattr(event.the_hnl.l2(), 'bestdgmuon'  ): self.fillParticle(self.tree, 'l2_matched_dgmuon'  , event.the_hnl.l2().bestdgmuon  ) ; self.fillMuonTrack(self.tree, 'l2_matched_dgmuon_track', event.the_hnl.l2().bestdgmuon )
        if event.the_hnl.l2().bestmatch != None: self.fillParticle(self.tree, 'l2_bestmatch'       , event.the_hnl.l2().bestmatch   )
        self.fill(self.tree, 'l2_bestmatch_type',event.the_hnl.l2().bestmatchtype)
        

        # final neutrino
        self.fillGenParticle(self.tree, 'n'  , event.the_hnl.met())

        # true primary vertex
        self.fill(self.tree, 'pv_x', event.the_hn.vx())
        self.fill(self.tree, 'pv_y', event.the_hn.vy())
        self.fill(self.tree, 'pv_z', event.the_hn.vz())

        # true HN decay vertex
        self.fill(self.tree, 'sv_x', event.the_hn.lep1.vertex().x()) # don't use the final lepton to get the vertex from!
        self.fill(self.tree, 'sv_y', event.the_hn.lep1.vertex().y()) # don't use the final lepton to get the vertex from!
        self.fill(self.tree, 'sv_z', event.the_hn.lep1.vertex().z()) # don't use the final lepton to get the vertex from!

        # displacements
        self.fill(self.tree, 'hnl_2d_disp', displacement2D(event.the_hn.lep1, event.the_hn))
        self.fill(self.tree, 'hnl_3d_disp', displacement3D(event.the_hn.lep1, event.the_hn))
        
        # reco secondary vertex and displacement
        if event.recoSv:
            self.fill(self.tree, 'sv_reco_x'   , event.recoSv.x()             )
            self.fill(self.tree, 'sv_reco_y'   , event.recoSv.y()             )
            self.fill(self.tree, 'sv_reco_z'   , event.recoSv.z()             )
            self.fill(self.tree, 'sv_reco_xe'  , event.recoSv.xError()        )
            self.fill(self.tree, 'sv_reco_ye'  , event.recoSv.yError()        )
            self.fill(self.tree, 'sv_reco_ze'  , event.recoSv.zError()        )
            self.fill(self.tree, 'sv_reco_prob', event.recoSv.prob            )
            self.fill(self.tree, 'sv_reco_cos' , event.recoSv.disp2DFromBS_cos)
    
            self.fill(self.tree, 'hnl_2d_reco_disp', event.recoSv.disp2DFromBS.value()) # from beamspot
            self.fill(self.tree, 'hnl_3d_reco_disp', event.recoSv.disp3DFromBS.value()) # from PV
    
            self.fill(self.tree, 'hnl_2d_reco_disp_sig', event.recoSv.disp2DFromBS_sig) # from beamspot
            self.fill(self.tree, 'hnl_3d_reco_disp_sig', event.recoSv.disp3DFromBS_sig) # from PV

        # flag if the event is in CMS acceptance |eta|<2.4 (general CMS is 2.5, but the muon system is 2.4)
        is_in_acc =  abs(event.the_hnl.l0().eta())<2.4 and \
                     abs(event.the_hnl.l1().eta())<2.4 and \
                     abs(event.the_hnl.l2().eta())<2.4
 
        self.fill(self.tree, 'is_in_acc', is_in_acc)

        self.fillTree(event)


