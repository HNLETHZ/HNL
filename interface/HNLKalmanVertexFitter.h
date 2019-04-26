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

#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"

class HNLKalmanVertexFitter {

  public:
    HNLKalmanVertexFitter() {};
    virtual ~HNLKalmanVertexFitter() {};

    reco::TransientTrack getTransientTrack(const reco::TrackRef& trackRef) {    
      reco::TransientTrack transientTrack(trackRef, paramField);
      return transientTrack;
    }

//     TransientVertex Fit(const reco::TrackRefVector & tracks)
//     {
//     
//       // do tau vertex fit
//       std::vector<reco::TransientTrack> tks;
//       for (reco::TrackRefVector::const_iterator itk = tracks.begin(); itk != tracks.end(); ++itk){
//           tks.push_back(getTransientTrack(*itk));
//       }

    TransientVertex Fit(const std::vector<reco::TrackRef> & tracks)
    {
    
      // do tau vertex fit
      std::vector<reco::TransientTrack> tks;
      for (std::vector<reco::TrackRef>::const_iterator itk = tracks.begin(); itk != tracks.end(); ++itk){
          tks.push_back(getTransientTrack(*itk));
      }
    
      KalmanVertexFitter kvf;
      TransientVertex tv = kvf.vertex(tks);
      
      // reco::Vertex tauvertex = tautv;
      
      return tv;
          
    };

  private:
    OAEParametrizedMagneticField *paramField = new OAEParametrizedMagneticField("3_8T");

};