from math import sqrt

from itertools import combinations, product

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
from ROOT import TVector3, Math
import ROOT
from pdb import set_trace


class DiLepton(object):
    '''
    '''
    def __init__(self, pair, sv, pv, bs):
        # self._leptons = sorted(pair, key = lambda lep : (-abs(lep.pdgId()),lep.pt()), reverse = True)
        self._leptons = pair

        self._vtx = sv
        self._pv  = pv
        self._bs  = bs
        # create an 'ideal' vertex out of the BS
        point = ROOT.reco.Vertex.Point(
            bs.position().x(),
            bs.position().y(),
            bs.position().z(),
        )
        error = bs.covariance3D()
        chi2 = 0.
        ndof = 0.
        bsvtx = ROOT.reco.Vertex(point, error, chi2, ndof, 2) # size? say 2? does it matter?
        self._bsvtx  = bsvtx

    def leptons(self):
        return self._leptons

    def lep1(self):
        return self.leptons()[0]

    def lep2(self):
        return self.leptons()[1]

    def p4(self):
        return self.lep1().p4() + self.lep2().p4()
    
    def pt(self):
        return self.p4().pt()

    def eta(self):
        return self.p4().eta()

    def phi(self):
        return self.p4().phi()

    def px(self):
        return self.p4().px()

    def py(self):
        return self.p4().py()

    def pz(self):
        return self.p4().pz()

    def p(self):
        return self.p4().p()

    def e(self):
        return self.p4().e()

    def mass(self):
        return self.p4().mass()

    def deta(self):
        return abs(self.lep1().eta() - self.lep2().eta()) 
       
    def dphi(self):
        return abs(deltaPhi(self.lep1().phi(), self.lep2().phi()))

    def dr(self):
        return deltaR(self.lep1(), self.lep2()) 

    def vtx(self):
        return self._vtx

    def chi2(self):
        return self.vtx().chi2()

    def isSS(self):
        return int(self.lep1().charge()==self.lep2().charge())

    def _disp3DFromPV(self):
        return ROOT.VertexDistance3D().distance(self.vtx(), self._pv)

    def disp3DFromPV(self):
        return self._disp3DFromPV().value()

    def disp3DFromPVSignificance(self):
        return self._disp3DFromPV().significance()

    def _disp2DFromBS(self):
        return ROOT.VertexDistanceXY().distance(self.vtx(), self._bsvtx)

    def disp2DFromBS(self):
        return self._disp2DFromBS().value()

    def disp2DFromBSSignificance(self):
        return self._disp2DFromBS().significance()

    def _disp2DFromPV(self):
        return ROOT.VertexDistanceXY().distance(self.vtx(), self._pv)

    def disp2DFromPV(self):
        return self._disp2DFromPV().value()

    def disp2DFromPVSignificance(self):
        return self._disp2DFromPV().significance()

    def cosTransversePointingAngleBS(self):
        
        if not hasattr(self, '_cos'):

            perp = ROOT.math.XYZVector(self.px(),
                                       self.py(),
                                       0.)
        
            dxybs = ROOT.GlobalPoint(-1*((self._bs.x0() - self.vtx().x()) + (self.vtx().z() - self._bs.z0()) * self._bs.dxdz()), 
                                     -1*((self._bs.y0() - self.vtx().y()) + (self.vtx().z() - self._bs.z0()) * self._bs.dydz()),
                                      0)
        
            vperp = ROOT.math.XYZVector(dxybs.x(), dxybs.y(), 0.)
        
            cos = vperp.Dot(perp)/(vperp.R()*perp.R())
            
            self._cos = cos

        return self._cos

    def __str__(self):
        return '\n'.join(['',
                          self.lep1().__str__(),
                          self.lep2().__str__(),
                          '\t pt       %.2f' %self.pt(),
                          '\t eta      %.2f' %self.eta(),
                          '\t phi      %.2f' %self.phi(),
                          '\t mass     %.3f' %self.mass(),
                          '\t deltaR   %.5f' %self.dr(),
                          '\t deltaPhi %.5f' %self.dphi(),
                          '\t deltaEta %.5f' %self.deta(),
                          '\t vertex x=%.2f y=%.2f z=%.2f' %(self.vtx().x(), self.vtx().y(), self.vtx().z()),
                          '\t vertex chi2 %.5f' %self.chi2(),
                          '\t 2d displacement from BS %.3f with L/sigma %.3f' %(self.disp2DFromBS(), self.disp2DFromBSSignificance()),
                          '\t 2d displacement from PV %.3f with L/sigma %.3f' %(self.disp2DFromPV(), self.disp2DFromPVSignificance()),
                          '\t 3d displacement from PV %.3f with L/sigma %.3f' %(self.disp3DFromPV(), self.disp3DFromPVSignificance()),
                          '\t pointing angle cosine %.7f' %self.cosTransversePointingAngleBS(),
                          '',
                        ])                          
