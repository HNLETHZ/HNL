import ROOT
from CMGTools.HNL.analyzers.TreeProducerBase import TreeProducerBase
from PhysicsTools.HeppyCore.utils.deltar import deltaR
from CMGTools.HNL.utils.utils import isAncestor, displacement2D, displacement3D, makeRecoVertex # utility functions
from pdb import set_trace

class HNLTreeProducerData(TreeProducerBase):
    '''
    '''
    def declareVariables(self, setup):
        '''
        '''
        # output for reco analysis
        self.bookEvent(self.tree)
        self.bookHNLReco(self.tree)
        self.bookDiMuon(self.tree, 'dimuonMaxCosBPA')
        self.bookDisplacedMuon (self.tree,'dMu1MaxCosBPA')
        self.bookDisplacedMuon (self.tree,'dMu2MaxCosBPA')
        self.bookEle(self.tree, 'prompt_ele') 
        self.bookExtraMetInfo(self.tree)
        # jet information
        self.bookJet(self.tree, 'jet1' , fill_extra=False)
        self.bookJet(self.tree, 'jet2' , fill_extra=False)
        self.bookJet(self.tree, 'bjet1', fill_extra=False)
        self.bookJet(self.tree, 'bjet2', fill_extra=False)
        self.var(self.tree, 'HTjets' )
        self.var(self.tree, 'HTbjets')
        self.var(self.tree, 'njets'  )
        self.var(self.tree, 'nbjets' )

    def process(self, event):
        '''
        '''
        self.readCollections(event.input)
        self.tree.reset()
        self.fillExtraMetInfo(self.tree, event)
        # jet variables
        if len(event.cleanJets)>0:
            self.fillJet(self.tree, 'jet1', event.cleanJets[0], fill_extra=False)
        if len(event.cleanJets)>1:
            self.fillJet(self.tree, 'jet2', event.cleanJets[1], fill_extra=False)
        if len(event.cleanBJets)>0:
            self.fillJet(self.tree, 'bjet1', event.cleanBJets[0], fill_extra=False)
        if len(event.cleanBJets)>1:
            self.fillJet(self.tree, 'bjet2', event.cleanBJets[1], fill_extra=False)

        self.fill(self.tree, 'HTjets' , event.HT_cleanJets   )
        self.fill(self.tree, 'HTbjets', event.HT_bJets       )
        self.fill(self.tree, 'njets'  , len(event.cleanJets) )
        self.fill(self.tree, 'nbjets' , len(event.cleanBJets))

        # output of reco analysis
        self.fillEvent(self.tree, event)
        self.fillHNLReco(self.tree, event)
        if hasattr(event, 'dimuonMaxCosBPA'):
            self.fillDiMuon(self.tree, 'dimuonMaxCosBPA', event.dimuonMaxCosBPA)
            self.fillDisplacedMuon (self.tree,'dMu1MaxCosBPA', event.dMu1MaxCosBPA)
            self.fillDisplacedMuon (self.tree,'dMu2MaxCosBPA', event.dMu2MaxCosBPA)

        if event.the_prompt_cand != None: # hasattr(event, 'the_prompt_cand'):
            if abs(event.the_prompt_cand.pdgId()) == 11:
                self.fillEle(self.tree, 'prompt_ele', event.the_prompt_cand)


        self.fillTree(event)


