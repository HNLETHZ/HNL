#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "TrackingTools/PatternTools/interface/ClosestApproachInRPhi.h"
#include "TrackingTools/PatternTools/interface/TSCBLBuilderNoMaterial.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "MagneticField/ParametrizedEngine/src/OAEParametrizedMagneticField.h"

#include "RecoVertex/KinematicFitPrimitives/interface/ParticleMass.h"
#include "RecoVertex/KinematicFitPrimitives/interface/MultiTrackKinematicConstraint.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFit/interface/KinematicConstrainedVertexFitter.h"
#include "RecoVertex/KinematicFit/interface/TwoTrackMassKinematicConstraint.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleFitter.h"
#include "RecoVertex/KinematicFit/interface/MassKinematicConstraint.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicVertex.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParametersError.h"

#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"

#include "RecoVertex/VertexTools/interface/VertexDistance3D.h"
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"


class HNLKinematicVertexFitter {

  public:
    HNLKinematicVertexFitter() {};
    virtual ~HNLKinematicVertexFitter() {};
    

    // constructed by reco::TrackRef
    reco::TransientTrack getTransientTrack(const reco::TrackRef& trackRef) {    
      reco::TransientTrack transientTrack(trackRef, paramField);

      return transientTrack;
    }

    RefCountedKinematicTree Fit(const std::vector<reco::RecoChargedCandidate> & candidates){

      KinematicParticleFactoryFromTransientTrack pFactory;  
      std::vector<RefCountedKinematicParticle> XParticles;

      for (std::vector<reco::RecoChargedCandidate>::const_iterator ilc = candidates.begin(); ilc != candidates.end(); ++ilc){
        float pmass  = ilc->mass();
        float pmasse = 1.e-6* pmass;
        XParticles.push_back(pFactory.particle(getTransientTrack(ilc->track()), pmass, chi, ndf, pmasse));
      }

      KinematicConstrainedVertexFitter kvFitter;
      RefCountedKinematicTree KinVtx = kvFitter.fit(XParticles); 
      
      return KinVtx;
        
    }

    // constructed by reco::Track
    reco::TransientTrack getTransientTrack(const reco::Track& track) {    
      reco::TransientTrack transientTrack(track, paramField);

      return transientTrack;
    }

    RefCountedKinematicTree Fit(const std::vector<reco::Track> & candidates, std::string L1L2LeptonType){

      KinematicParticleFactoryFromTransientTrack pFactory;  
      std::vector<RefCountedKinematicParticle> XParticles;
      int i = 0;
      for (std::vector<reco::Track>::const_iterator ilc = candidates.begin(); ilc != candidates.end(); ++ilc){
        float pmass = 5.11e-4;
        if (L1L2LeptonType == "ee"){
            pmass = 5.11e-4; 
        }
        if (L1L2LeptonType == "mm"){
            pmass = 1.05658e-1; 
        }
        if (L1L2LeptonType == "em"){
            if (i==0){pmass = 5.11e-4;}
            if (i==1){pmass = 1.05658e-1;}
        }
        float pmasse = 1.e-6 * pmass;
        XParticles.push_back(pFactory.particle(getTransientTrack(*ilc), pmass, chi, ndf, pmasse));
        i++;
      }

      KinematicConstrainedVertexFitter kvFitter;
      RefCountedKinematicTree KinVtx = kvFitter.fit(XParticles); 
      
      return KinVtx;
        
    }

  private:
    
    OAEParametrizedMagneticField *paramField = new OAEParametrizedMagneticField("3_8T");
    // Insignificant mass sigma to avoid singularities in the covariance matrix.
    // initial chi2 and ndf before kinematic fits. The chi2 of the reconstruction is not considered 
    float chi        = 0.;
    float ndf        = 0.;

};

