import ROOT
from math import sqrt
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject
from pdb import set_trace
# load custom library to ROOT. This contains the kinematic vertex fitter class
ROOT.gSystem.Load('libCMGToolsHNL')
from ROOT import HNLKinematicVertexFitter as VertexFitter

# initiate the VertexFitter
vtxfit = VertexFitter()

# create a std::vector<RecoChargedCandidate> to be passed to the fitter

def isAncestor(a, p):
    if a == p :
        return True
    for i in xrange(0,p.numberOfMothers()):
        if isAncestor(a,p.mother(i)):
            return True
    return False

def displacement2D(p1, p2):    
    dx = p1.vx() - p2.vx()    
    dy = p1.vy() - p2.vy()    
    return sqrt(dx**2 + dy**2)    

def displacement3D(p1, p2):    
    dx = p1.vx() - p2.vx()    
    dy = p1.vy() - p2.vy()    
    dz = p1.vz() - p2.vz()    
    return sqrt(dx**2 + dy**2 + dz**2)    

def makeRecoVertex(kinVtx, kinVtxChi2=0., kinVtxNdof=0, kinVtxTrkSize=0):
    point = ROOT.reco.Vertex.Point(
        kinVtx.vertexState().position().x(),
        kinVtx.vertexState().position().y(),
        kinVtx.vertexState().position().z(),
    )
    error = kinVtx.vertexState().error().matrix()
    chi2  = kinVtxChi2 if kinVtxChi2 else kinVtx.chiSquared()
    ndof  = kinVtxNdof if kinVtxNdof else kinVtx.degreesOfFreedom()
    recoVtx = ROOT.reco.Vertex(point, error, chi2, ndof, kinVtxTrkSize)
    return recoVtx

def fitVertex_RecoChargedCandidates(pair):
    tofit = ROOT.std.vector('reco::RecoChargedCandidate')()
    vtx = None
    tofit.clear()
    for il in pair:

        ic = ROOT.reco.RecoChargedCandidate() # instantiate a dummy RecoChargedCandidate
        ic.setCharge(il.charge())           # assign the correct charge

        if il.pdgId()%13==0:
            if il.muonBestTrack().isNull(): # check that the track is valid. e.g. photons... 
            # if il.standAloneMuon().isNull(): # check that the track is valid. e.g. photons... 
            # if il.globalTrack().isNull(): # check that the track is valid. e.g. photons... 
                continue
            ic.setTrack(il.muonBestTrack())
            # ic.setTrack(il.standAloneMuon())
            # ic.setTrack(il.globalTrack())
        else:
            if il.track().isNull():
                continue
            ic.setTrack(il.track())

        # if the reco particle is a displaced thing, it does not have the p4() method, so let's build it 
        myp4 = ROOT.Math.LorentzVector('<ROOT::Math::PxPyPzE4D<double> >')(il.px(), il.py(), il.pz(), sqrt(il.mass()**2 + il.px()**2 + il.py()**2 + il.pz()**2))
        ic.setP4(myp4)                      # assign the correct p4
        if ic.track().isNonnull():          # check that the track is valid, there are photons around too!
            tofit.push_back(ic)

    # further sanity check: two *distinct* tracks
    if tofit.size() == 2 and tofit[0].track() != tofit[1].track():
        svtree = vtxfit.Fit(tofit) # the actual vertex fitting!
        if not svtree.get().isEmpty() and svtree.get().isValid(): # check that the vertex is good
            svtree.movePointerToTheTop()
            vtx = makeRecoVertex(svtree.currentDecayVertex().get(),kinVtxTrkSize=tofit.size())
            # set_trace()
    # set_trace()
    return vtx

def fitVertex(pair,L1L2LeptonType):
    tofit = ROOT.std.vector('reco::Track')()
    vtx = None
    tofit.clear()

    if pair[0] == pair[1]:
        print 'vtx fitter: both leps in the pair are the same!'
        return False
    
    for il in pair:
        if abs(il.pdgId())==13:
            if il.muonBestTrack().get():
                tofit.push_back(il.muonBestTrack().get())
                if not il.muonBestTrack().get().numberOfValidHits()>0: 
                    print 'there are no valid tracker hits in this muon track'
            else: print 'could not load muonBestTrack() from the muon'
            # if il.globalTrack().get():
                # tofit.push_back(il.globalTrack().get())
                # if not il.globalTrack().get().numberOfValidHits()>0: 
                    # print 'there are no valid tracker hits in this muon track'
            # # else: print 'could not load globalTrack() from the muon'
        if abs(il.pdgId()) == 26: 
            #TODO: to be implemented once solved the BField issue
            print 'pair contains dsa muons, not compatible yet. make sure to only use PF (slimmed) muons.'
        if abs(il.pdgId())==11:
            if il.gsfTrack().get():
                tofit.push_back(ROOT.reco.Track(il.gsfTrack().get()))
                if not ROOT.reco.Track(il.gsfTrack().get()).numberOfValidHits()>0:
                    print 'there are no valid tracker hits in this electron track'%(index)
            else: print 'could not load gsfTrack() from the electron'%(index)

    if tofit.size() == 2 and tofit[0]!=tofit[1]:
        #call the vertix fit function from framework
        sv = vtxfit.Fit(tofit, L1L2LeptonType)
            
        

        if not sv.get().isEmpty() and sv.get().isValid(): # check that the vertex is good
            sv.movePointerToTheTop()
            vtx = makeRecoVertex(sv.currentDecayVertex().get(),kinVtxTrkSize=tofit.size())
        else:
            return False
    return vtx



