#define G__DICTIONARY


#include <atomic>
// #include <art>


#include "DataFormats/Common/interface/Wrapper.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "CMGTools/HNL/interface/HNLKinematicVertexFitter.h"
#include "CMGTools/HNL/interface/HNLKalmanVertexFitter.h"


#include "MagneticField/Layers/src/MagBinFinders.h"
#include "CondFormats/DataRecord/interface/MagFieldConfigRcd.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/VolumeGeometry/interface/MagVolume.h"
#include "MagneticField/VolumeBasedEngine/interface/MagGeometry.h"
#include "MagneticField/VolumeBasedEngine/interface/VolumeBasedMagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/DependentRecordTag.h"
#include "FWCore/Framework/interface/DependentRecordImplementation.h"
#include "Utilities/BinningTools/interface/PeriodicBinFinderInPhi.h"
#include "Utilities/BinningTools/interface/BaseBinFinder.h"
#include "MagneticField/UniformEngine/interface/UniformMagneticField.h"
#include "MagneticField/ParametrizedEngine/src/OAEParametrizedMagneticField.h"
#include "MagneticField/Layers/interface/MagBLayer.h"
#include "MagneticField/Layers/interface/MagBRod.h"
#include "MagneticField/Layers/interface/MagBSector.h"
#include "MagneticField/Layers/interface/MagBSlab.h"
#include "MagneticField/Layers/interface/MagELayer.h"
#include "MagneticField/Layers/interface/MagESector.h"
#include "FWCore/Framework/interface/EventSetupRecord.h"
#include "FWCore/Framework/interface/EventSetupRecordImplementation.h"
#include "MagneticField/VolumeGeometry/interface/MagneticFieldProvider.h"
#include "MagneticField/VolumeGeometry/interface/MagVolume6Faces.h"
#include "DataFormats/GeometrySurface/interface/GloballyPositioned.h"
#include "DataFormats/GeometrySurface/interface/TkRotation.h"


namespace {
  struct CMG_HNL {
    HNLKinematicVertexFitter hnlKinVtx_;
    HNLKalmanVertexFitter hnlKalVtx_;
    MagneticField* hnlMagneticFieldPtr_;
    MagFieldConfigRcd hnlMagFieldRcd_;
    VolumeBasedMagneticField hnlVolumeBasedMagneticField_;
    atomic<bool> hnlAtomicBool_;
//     std::atomic<char> hnlAtomicChar_;
//     MagVolume hnlMagVolume_;
//     MagVolume * hnlMagVolumePtr_;
//     std::atomic<MagVolume> hnla_;
//     std::atomic<MagVolume*> hnlb_;
//     std::atomic<const MagVolume> hnlc_;
//     std::atomic<const MagVolume*> hnld_;
//     atomic<const MagVolume*> hnld_;
//     atomic<MagVolume const *> hnle_;
//     MagGeometry hnlMagGeometry_;
//     MagGeometry * hnlMagGeometryPtr_;
    
    edm::eventsetup::EventSetupRecord * hnlEventSetupRecordPtr_;
    edm::eventsetup::EventSetupRecordImplementation<IdealMagneticFieldRecord> hnlEventSetupRecordImplementation_;
    edm::ValidityInterval hnlValidityInterval;
    map<edm::eventsetup::DataKey,const edm::eventsetup::DataProxy*> hnlDataKey_;
    edm::EventSetup* hnlEventSetupPtr_;
    edm::EventSetup hnlEventSetup_;
    edm::eventsetup::DependentRecordTag hnlDependentRecordTag_;
    edm::eventsetup::DependentRecordImplementation<IdealMagneticFieldRecord,boost::mpl::vector<MFGeometryFileRcd,RunInfoRcd,MagFieldConfigRcd,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na,mpl_::na> > hnlLotsOfJunk_ ;
    
    MagBinFinders::GeneralBinFinderInR<double>* hnl1_;
    MagBinFinders::GeneralBinFinderInR<double> hnl2_;
    MagBinFinders::GeneralBinFinderInZ<double> hnl3_;
    MagBinFinders::GeneralBinFinderInZ<double>* hnl4_;
    PeriodicBinFinderInPhi<float>* hnlPeriodicBinFinderInPhi_;
    BaseBinFinder<double>* hnlBaseBinFinderDouble_;
    BaseBinFinder<float>* hnlBaseBinFinderFloat_;
    UniformMagneticField hnlUniformMagField_;
    OAEParametrizedMagneticField hnlOAEParametrizedMagneticField_;
    magfieldparam::TkBfield hnlMagfieldparamTkBfield_;
    magfieldparam::BCycl<float> hnlMagfieldparamBCyclFloat_;
    magfieldparam::BCylParam<float> hnlMagfieldparamBCylParamFloat_;
    MagVolume6Faces hnlMag1_;
    MagneticFieldProvider<float>* hnlMagggg_;


    MagBLayer   hnlMag2_;
    MagBRod     hnlMag3_;
    MagBSector  hnlMag4_;
    MagBSlab    hnlMag5_;
    MagELayer   hnlMag6_;
    MagESector  hnlMag7_;
    
    GloballyPositioned<float> hnlMag8_;
    TkRotation<float> hnlMag9_;


//     std::vector<art::ProductID> hnlVecArtPID;
//     std::pair<art::ProductID, std::set<art::ProductID>> hnlPairArt;


  };
}