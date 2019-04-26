import math

from itertools import combinations, product
# from copy import deepcopy as dc

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
from ROOT import TVector3, Math
import ROOT

class HN3L(object):

    ''' 
    '''

    def __init__(self, l0, l1, l2, met=None):
        self.l0_ = l0 # prompt lepton
        self.l1_ = l1 # leading pt lepton
        self.l2_ = l2 # trailing pt displaced lepton
        self.met_ = met

    # objects
    def l0(self):
        return self.l0_

    def l1(self):
        return self.l1_

    def l2(self):
        return self.l2_

    def met(self):
        return self.met_

    def WCharge(self):
        return self.l0().charge() + self.l1().charge() + self.l2().charge()

    def hnCharge(self):
        return self.l1().charge() + self.l2().charge()
        
    # W kinematics w/ met
    def WPx(self):
        return self.WP4().Px()

    def WPy(self):
        return self.WP4().Py()

    def WPz(self):
        return self.WP4().Pz()

    def WE(self):
        return self.WP4().E()

    def WP4(self):
        return self.l0().p4() + self.l1().p4() + self.l2().p4() + self.met().p4() if self.met() else None

    def WPt(self):
        return self.WP4().pt() if self.met() else None

    def WEta(self):
        return self.WP4().eta() if self.met() else None

    def WPhi(self):
        return self.WP4().phi() if self.met() else None

    def WMass(self):
        return self.WP4().mass() if self.met() else None

    def WSumPt(self):
        return self.l0().pt() + self.l1().pt() + self.l2().pt() + self.met().pt() if self.met() else None

    # W kinematics w/o met
    def WVisP4(self):
        return self.l0().p4() + self.l1().p4() + self.l2().p4()

    def WVisPt(self):
        return self.WVisP4().pt()

    def WVisEta(self):
        return self.WVisP4().eta()

    def WVisPhi(self):
        return self.WVisP4().phi()

    def WVisMass(self):
        return self.WVisP4().mass()

    def WVisSumPt(self):
        return self.l0().pt() + self.l1().pt() + self.l2().pt()

    # heavy neutrino kinematics w/ met
    def hnPx(self):
        return self.hnP4().Px()

    def hnPy(self):
        return self.hnP4().Py()

    def hnPz(self):
        return self.hnP4().Pz()

    def hnE(self):
        return self.hnP4().E()

    def hnP4(self):
        return self.l1().p4() + self.l2().p4() + self.met().p4() if self.met() else None

    def hnPt(self):
        return self.hnP4().pt() if self.met() else None

    def hnEta(self):
        return self.hnP4().eta() if self.met() else None

    def hnPhi(self):
        return self.hnP4().phi() if self.met() else None

    def hnMass(self):
        return self.hnP4().mass() if self.met() else None

    def hnSumPt(self):
        return self.l1().pt() + self.l2().pt() + self.met().pt() if self.met() else None

    # heavy neutrino kinematics w/o met
    def hnVisP4(self):
        return self.l1().p4() + self.l2().p4()

    def hnVisPt(self):
        return self.hnVisP4().pt()

    def hnVisEta(self):
        return self.hnVisP4().eta()

    def hnVisPhi(self):
        return self.hnVisP4().phi()

    def hnVisMass(self):
        return self.hnVisP4().mass()

    def hnVisE(self):
        return self.hnVisP4().E()

    def hnVisSumPt(self):
        return self.l1().pt() + self.l2().pt()
        
    # pair masses
    def mass01(self):
        return (self.l0().p4() + self.l1().p4()).mass() 

    def mass02(self):
        return (self.l0().p4() + self.l2().p4()).mass() 

    def mass12(self):
        return (self.l1().p4() + self.l2().p4()).mass() 

    # lepton charges
    def charge01(self):
        return self.l0().charge() + self.l1().charge()

    def charge02(self):
        return self.l0().charge() + self.l2().charge()

    def charge12(self):
        return self.l1().charge() + self.l2().charge()

    # delta R & delta phi
    def dR01(self):
        return deltaR(self.l0().p4(), self.l1().p4())

    def dR02(self):
        return deltaR(self.l0().p4(), self.l2().p4())

    def dR12(self):
        return deltaR(self.l1().p4(), self.l2().p4())

    def dR0MET(self):
        return deltaR(self.l0().p4(), self.met().p4()) if self.met() else None

    def dR1MET(self):
        return deltaR(self.l1().p4(), self.met().p4()) if self.met() else None

    def dR2MET(self):
        return deltaR(self.l2().p4(), self.met().p4()) if self.met() else None

    def dPhi01(self):
        return deltaPhi(self.l0().phi(), self.l1().phi())

    def dPhi02(self):
        return deltaPhi(self.l0().phi(), self.l2().phi())

    def dPhi12(self):
        return deltaPhi(self.l1().phi(), self.l2().phi())

    def dPhi0MET(self):
        return deltaPhi(self.l0().phi(), self.met().phi()) if self.met() else None

    def dPhi1MET(self):
        return deltaPhi(self.l1().phi(), self.met().phi()) if self.met() else None

    def dPhi2MET(self):
        return deltaPhi(self.l2().phi(), self.met().phi()) if self.met() else None

    def dRvisHnMET(self):
        return deltaR(self.hnVisP4(), self.met()) if self.met() else None

    def dRvisHn0(self):
        return deltaR(self.hnVisP4(), self.l0())

    def dRHnMET(self):
        return deltaR(self.hnP4(), self.met()) if self.met() else None

    def dRHn0(self):
        return deltaR(self.hnP4(), self.l0()) if self.met() else None

    def dPhiVisHnMET(self):
        return deltaPhi(self.hnVisP4().phi(), self.met().phi()) if self.met() else None

    def dPhiVisHn0(self):
        return deltaPhi(self.hnVisP4().phi(), self.l0().phi())

    def dPhiHnMET(self):
        return deltaPhi(self.hnP4().phi(), self.met().phi()) if self.met() else None

    def dPhiHn0(self):
        return deltaPhi(self.hnP4().phi(), self.l0().phi()) if self.met() else None

    # pt of two-body pairs
    def pt01(self):
        return (self.l0().p4() + self.l1().p4()).pt()

    def pt02(self):
        return (self.l0().p4() + self.l2().p4()).pt()

    def pt12(self):
        return (self.l1().p4() + self.l2().p4()).pt()

    def pt0MET(self):
        return (self.l0().p4() + self.met().p4()).pt() if self.met() else None

    def pt1MET(self):
        return (self.l1().p4() + self.met().p4()).pt() if self.met() else None

    def pt2MET(self):
        return (self.l2().p4() + self.met().p4()).pt() if self.met() else None

    # transverse masses
    def mt0(self):
        mt0 = self.calcMT(self.l0().p4(), self.met()) if self.met() else None
        return mt0

    def mt1(self):
        mt1 = self.calcMT(self.l1().p4(), self.met()) if self.met() else None
        return mt1

    def mt2(self):
        mt2 = self.calcMT(self.l2().p4(), self.met()) if self.met() else None
        return mt2

    def mtVisHnMET(self):
        mtHnMET = self.calcMT(self.hnVisP4(), self.met()) if self.met() else None
        return mtHnMET

    # pointing angle
    def cos(self):

        perp = ROOT.math.XYZVector(self.hnVisP4().px(),
                                   self.hnVisP4().py(),
                                   0.)
        
        dxybs = ROOT.GlobalPoint(-1*(self.l0().vertex().x() - self.l1().vertex().x()), 
                                 -1*(self.l0().vertex().y() - self.l1().vertex().y()),
                                  0)
        
        vperp = ROOT.math.XYZVector(dxybs.x(), dxybs.y(), 0.)
        
        cos = vperp.Dot(perp)/(vperp.R()*perp.R())
                
        return cos

    # more stuff
    def calcPZeta(self):
        l0PT  = TVector3(self.l0() .p4().x(), self.l0() .p4().y(), 0.)
        l1PT = TVector3(self.l1().p4().x(), self.l1().p4().y(), 0.)
        l2PT = TVector3(self.l2().p4().x(), self.l2().p4().y(), 0.)
        metPT = TVector3(self.met().p4().x(), self.met().p4().y(), 0.)
        zetaAxis = (l0PT.Unit() + l1PT.Unit() + l2PT.Unit()).Unit()
        self.pZetaVis_ = l0PT*zetaAxis + l1PT*zetaAxis + l2PT*zetaAxis
        self.pZetaMET_ = metPT*zetaAxis

    # Calculate the transverse mass with the same algorithm
    # as previously in the C++ DiObject class
    @staticmethod
    def calcMT(cand1, cand2):
        pt = cand1.pt() + cand2.pt()
        px = cand1.px() + cand2.px()
        py = cand1.py() + cand2.py()
        try:
            return math.sqrt(pt*pt - px*px - py*py)
        except ValueError:
            print 'Funny rounding issue', pt, px, py
            print cand1.px(), cand1.py(), cand1.pt()
            print cand2.px(), cand2.py(), cand2.pt()
            return 0.

    def __getattr__(self, name):
        '''Redefine getattr to original version.'''
        raise AttributeError
