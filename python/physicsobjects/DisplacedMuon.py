import ROOT

from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject

import math

from itertools import combinations, product
# from copy import deepcopy as dc

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
from ROOT import TVector3, Math

from pdb import set_trace

class DisplacedMuon(PhysicsObject):

    def __init__(self, physObj, collection):
        self.physObj = physObj
        super(PhysicsObject, self).__init__()
        self.collection_ = collection
        self.position_in_collection = -1
        for jj, mm in enumerate(self.collection_):
            if mm == self.physObj:
                self.position_in_collection = jj
                break
        
        energy = math.sqrt(self.mass()**2 + self.physObj.px()**2 + self.physObj.py()**2 + self.physObj.pz()**2)
        self.p4_ = ROOT.Math.LorentzVector('ROOT::Math::PxPyPzE4D<double>')(self.physObj.px(),
                                                                            self.physObj.py(),
                                                                            self.physObj.pz(),
                                                                            energy)

    def mass(self):
        '''impose the muon mass to the displaced objects, that otherwise carry none'''
        return 0.10565837

    def p4(self):
        return self.p4_
        
    def pdgId(self):
        '''impose the muon PDG ID to the displaced objects, that otherwise carry none'''
        return -(self.charge()*13)

    def track(self):
        ''' return reco::TrackRef '''   
        try:
            return ROOT.reco.TrackRef(self.collection_, self.position_in_collection)
        except:
            print 'DisplacedMuon.track() failed'

    def muonBestTrack(self):
        return self.track()
