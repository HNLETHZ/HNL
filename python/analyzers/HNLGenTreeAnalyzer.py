'''
Analyses a HNL -> 3L signal event, identifying the prompt and displaced leptons.
'''

import ROOT
from itertools import product, combinations
import math

from PhysicsTools.Heppy.analyzers.core.Analyzer      import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle    import AutoHandle
from PhysicsTools.Heppy.physicsobjects.GenParticle   import GenParticle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject
from PhysicsTools.HeppyCore.utils.deltar             import deltaR, deltaR2

from CMGTools.HNL.utils.utils         import isAncestor, displacement2D, displacement3D, makeRecoVertex # utility functions
from CMGTools.HNL.physicsobjects.HN3L import HN3L

from pdb import set_trace

class HNLGenTreeAnalyzer(Analyzer):
    '''
    '''

    def declareHandles(self):
        super(HNLGenTreeAnalyzer, self).declareHandles()

        self.mchandles['genp_pruned'] = AutoHandle(('prunedGenParticles', '', 'PAT' ), 'std::vector<reco::GenParticle>'                )
        self.mchandles['genp_packed'] = AutoHandle(('packedGenParticles', '', 'PAT' ), 'std::vector<pat::PackedGenParticle>'           )

    def beginLoop(self, setup):
        super(HNLGenTreeAnalyzer, self).beginLoop(setup)
        self.counters.addCounter('HNLGenTree')
        count = self.counters.counter('HNLGenTree')
        count.register('all events')
        
    def process(self, event):
        self.readCollections(event.input)
        
        self.counters.counter('HNLGenTree').inc('all events')

        # produce collections
        event.genp_pruned = self.mchandles['genp_pruned'].product()
        event.genp_packed = self.mchandles['genp_packed'].product()

        # no point to run this if it's not a HNL signal
        if 'HN3L' not in self.cfg_comp.name:
            return True
        
#         for pp in event.genp_packed:
#             printer = lambda : 'pat::PackedGenParticle:   %d, pt  %.2f, eta  %.2f, phi  %.2f, mass  %.2f, status  %d' %(pp.pdgId(), pp.pt(), pp.eta(), pp.phi(), pp.mass(), pp.status())
#             import pdb ; pdb.set_trace()
#             pp.__str__ = printer
#             import pdb ; pdb.set_trace()
# 
#         import pdb ; pdb.set_trace()

        # all gen particles
        event.genp = [ip for ip in event.genp_pruned] + [ip for ip in event.genp_packed]

        # get the heavy neutrino
        the_hns = [ip for ip in event.genp_pruned if abs(ip.pdgId())==9900012 and ip.isLastCopy()]
        event.the_hn = the_hns[0] # one per event

        # prompt lepton
        event.the_pl = map(GenParticle, [ip for ip in event.genp_pruned if abs(ip.pdgId()) in [11,13,15] and ip.isPromptFinalState() and not isAncestor(event.the_hn, ip)])[0]      

        # get the immediate daughters of the heavy neutrino decay
        event.the_hn.initialdaus = [event.the_hn.daughter(jj) for jj in range(event.the_hn.numberOfDaughters())]

        event.the_hn.lep1 = max([ii for ii in event.the_hn.initialdaus if abs(ii.pdgId()) in [11, 13, 15]], key = lambda x : x.pt())
        event.the_hn.lep2 = min([ii for ii in event.the_hn.initialdaus if abs(ii.pdgId()) in [11, 13, 15]], key = lambda x : x.pt())
        event.the_hn.neu  =     [ii for ii in event.the_hn.initialdaus if abs(ii.pdgId()) in [12, 14, 16]][0] # there can be only one

        # identify the secondary vertex
        event.the_hn.the_sv = event.the_hn.lep1.vertex()
    
        # need to analyse the lepton after they radiated / converted
        for ip in [event.the_hn.lep1, event.the_hn.lep2, event.the_pl]:
            finaldaus  = []
            for ipp in event.genp_packed:
#             for ipp in event.genp: # try with all particles, see if it makes sense
                mother = ipp.mother(0)
                if mother and isAncestor(ip, mother):
                    finaldaus.append(ipp)
            ip.finaldaughters = sorted(finaldaus , key = lambda x : x.pt(), reverse = True)
            ip.hasConvOrRad = (len(ip.finaldaughters)>1)
            if len(ip.finaldaughters)>1:
                try:
                    ip.finallep = max([ii for ii in ip.finaldaughters if ii.pdgId()==ip.pdgId()], key = lambda x : x.pt())
                except:
                    try:
                        ip.finallep = max([ii for ii in ip.finaldaughters if abs(ii.pdgId()) in [11, 13]], key = lambda x : x.pt())                
                    except:
                        return False
#                         import pdb ; pdb.set_trace()
            else:
                ip.finallep = ip

        # 4-momentum of the visible part of the HN
        event.the_hn.vishn = event.the_hn.lep1.finallep.p4() + event.the_hn.lep2.finallep.p4()

        # make it into a handy class
        event.the_hnl = HN3L(event.the_pl.finallep, event.the_hn.lep1.finallep, event.the_hn.lep2.finallep, event.the_hn.neu)

        return True
    
