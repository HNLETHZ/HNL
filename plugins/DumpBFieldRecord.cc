// -*- C++ -*-
//
// Package:    DumpBFieldRecord
// Class:      DumpBFieldRecord
// 
/**\class DumpBFieldRecord DumpBFieldRecord.cc junk/DumpBFieldRecord/src/DumpBFieldRecord.cc

 Description: This writes out a ROOT file with a BFieldRecord object taken from an sqlite file. 

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  "Salvatore Rappoccio"
//         Created:  Thu Feb 11 14:21:59 CST 2010
//
//

// system include files
#include <iostream>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESWatcher.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "PhysicsTools/CondLiteIO/interface/RecordWriter.h"
#include "DataFormats/Provenance/interface/ESRecordAuxiliary.h"
#include "DataFormats/FWLite/interface/format_type_name.h"

#include "CondFormats/MFObjects/interface/MagFieldConfig.h"
#include "CondFormats/DataRecord/interface/MagFieldConfigRcd.h"
#include "CondFormats/PhysicsToolsObjects/interface/BinningPointByMap.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/VolumeBasedEngine/interface/VolumeBasedMagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

#include "FWCore/Framework/interface/DependentRecordImplementation.h"
#include "FWCore/Framework/interface/eventsetuprecord_registration_macro.h"

#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

class DumpBFieldRecord : public edm::EDAnalyzer {
    public:
        explicit DumpBFieldRecord(const edm::ParameterSet&);
        ~DumpBFieldRecord() override;
  
    private:
        void beginJob() override ;
        void analyze(const edm::Event&, const edm::EventSetup&) override;
        void endJob() override ;
  
        std::string fieldLabel_;
//         edm::ESWatcher<MagFieldConfigRcd> recWatcher_;
        edm::ESWatcher<IdealMagneticFieldRecord> recWatcher_;
        std::unique_ptr<fwlite::RecordWriter> writer_;
        edm::IOVSyncValue firstValue_;
        edm::IOVSyncValue lastValue_;
};

// constructors and destructor
DumpBFieldRecord::DumpBFieldRecord(const edm::ParameterSet& iConfig) :
  fieldLabel_(iConfig.getParameter<std::string>("field"))
{}

DumpBFieldRecord::~DumpBFieldRecord(){}

void DumpBFieldRecord::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    std::cout << "Hello from DumpBFieldRecord!" << std::endl;
    std::cout << __LINE__ << "]\t" << std::endl;

    if(recWatcher_.check(iSetup)) {
//         const MagneticField& r = iSetup.get<MagFieldConfigRcd>();
//         const IdealMagneticFieldRecord& ideal = iSetup.get<IdealMagneticFieldRecord>();
        const IdealMagneticFieldRecord& record = iSetup.get<IdealMagneticFieldRecord>();
//         const MagFieldConfigRcd& record = iSetup.get<IdealMagneticFieldRecord>();
//         const MagFieldConfigRcd& record = iSetup.get<MagFieldConfigRcd>();
//         const MagFieldConfig& record = iSetup.get<MagFieldConfig>();

        std::cout << __LINE__ << "]\t" << std::endl;
        if(! writer_.get()) {
            std::cout << __LINE__ << "]\t" << std::endl;
            edm::Service<TFileService> fs ;
            std::cout << __LINE__ << "]\t" << std::endl;
            TFile * f = &(fs->file());
            std::cout << __LINE__ << "]\t" << record.key().name() << "\t" << f->GetName() << std::endl;
            // f->make<MagneticField>();
            
//             fwlite::RecordWriter * writer_ = new fwlite::RecordWriter(record.key().name(), f );
            writer_ = std::unique_ptr<fwlite::RecordWriter>(new fwlite::RecordWriter(record.key().name(), f ));
//             std::unique_ptr<fwlite::RecordWriter> writer_ = new fwlite::RecordWriter(record.key().name(), f );
            std::cout << __LINE__ << "]\t" << std::endl;
        }

        std::cout << __LINE__ << "]\t" << std::endl;

        firstValue_ = record.validityInterval().first();
        lastValue_  = record.validityInterval().last();

        std::cout << __LINE__ << "]\t" << std::endl;

//         edm::ESHandle<MagFieldConfigRcd> BField;
        edm::ESHandle<MagneticField> BField;
//         edm::ESHandle<MagFieldConfig> BField;

        std::cout << __LINE__ << "]\t" << std::endl;


//         OAE_1103l_071212
//         MagFieldConfig_RI90322_RII130503_3_8T
//         grid_130503_3_8t_v9_large
//         grid_160812_3_8t_Run1

//         record.get( "grid_130503_3_8t_v9_large", BField );
//         record.get( "3_8t_v9_large", BField );
        record.get( fieldLabel_, BField );
//         record.get( "3.8T", BField );
//         record.get( BField );
//         record.get( "grid_160812_3_8t_Run1", BField );
        std::cout << __LINE__ << "]\t" << std::endl;
        const MagneticField & theField = *(BField.product());
//         const MagneticField & theField = *(BField.product()->produce());
//         const MagFieldConfig & theField = *(BField.product());
//         const MagFieldConfig & theFieldCfg = *(BField.product());
//         const MagneticField & theField = theFieldCfg.produce(ideal);
//         const MagFieldConfigRcd & theField = *(BField.product());
        std::cout << __LINE__ << "]\t" << std::endl;
        std::cout << __LINE__ << "]\tnominal B value " << theField.nominalValue() << std::endl;
//         std::cout << __LINE__ << "]\tnominal B value " << theField.produce() << std::endl;

        double x,y,z;

        x = 0.; y = 0.; z = 0.;
        GlobalPoint g(x,y,z);          
        std::cout << __LINE__ << "]\tAt R=" << g.perp() << " phi=" << g.phi()<< " B=" << theField.inTesla(g) << std::endl;

        x = 50.; y = 50.; z = 0.;
        GlobalPoint gg(x,y,z);          
        std::cout << __LINE__ << "]\tAt R=" << gg.perp() << " phi=" << gg.phi()<< " B=" << theField.inTesla(gg) << std::endl;

        x = 200.; y = 200.; z = 0.;
        GlobalPoint ggg(x,y,z);          
        std::cout << __LINE__ << "]\tAt R=" << ggg.perp() << " phi=" << ggg.phi()<< " B=" << theField.inTesla(ggg) << std::endl;

        x = 300.; y = 300.; z = 0.;
        GlobalPoint gggg(x,y,z);          
        std::cout << __LINE__ << "]\tAt R=" << gggg.perp() << " phi=" << gggg.phi()<< " B=" << theField.inTesla(gggg) << std::endl;

        x = 400.; y = 400.; z = 0.;
        GlobalPoint ggggg(x,y,z);          
        std::cout << __LINE__ << "]\tAt R=" << ggggg.perp() << " phi=" << ggggg.phi()<< " B=" << theField.inTesla(ggggg) << std::endl;
     
        writer_->update(&(theField), typeid(MagneticField)    , record.key().name());

//         writer_->update(&(theField), typeid(MagFieldConfig)    , record.key().name());
//         writer_->update(&(theField), typeid(MagFieldConfigRcd), record.key().name());
//         writer_->update(&(record)  , typeid(MagFieldConfigRcd), record.key().name());
//         writer_->update(&(record)  , typeid(IdealMagneticFieldRecord), record.key().name());

        std::cout << __LINE__ << "]\t" << std::endl;


        std::cout << firstValue_.eventID().run() << std::endl;
        std::cout << firstValue_.time().value() << std::endl;

        std::cout << __LINE__ << "]\t" << std::endl;

        //writer_->fill(edm::ESRecordAuxiliary(edm::EventID(0,0,0),edm::Timestamp()));
        edm::ESRecordAuxiliary(edm::EventID(0,0,0),edm::Timestamp());
        //writer_->fill(edm::ESRecordAuxiliary(firstValue_.eventID(),firstValue_.time()));
        //writer_->fill();
        //std::cout<<edm::ESRecordAuxiliary(firstValue_.eventID(),firstValue_.time())<<std::endl;
        //edm::ESRecordAuxiliary(firstValue_.eventID(),firstValue_.time());
        
//         writer_->update(&(theField), typeid(MagneticField)    , record.key().name());

        std::cout << __LINE__ << "]\t" << std::endl;
//         writer_->fill(edm::ESRecordAuxiliary(lastValue_.eventID(),
//                                              lastValue_.time()));

        std::cout << __LINE__ << "]\t" << std::endl;

        writer_->write();

        std::cout << __LINE__ << "]\t" << std::endl;

        }
}

void DumpBFieldRecord::beginJob(){}

void DumpBFieldRecord::endJob() {
  //*
  std::cout << __LINE__ << "]\t" << std::endl;
  if(writer_.get()) {
    std::cout << __LINE__ << "]\t" << std::endl;
    //writer_->fill(edm::ESRecordAuxiliary(lastValue_.eventID(),lastValue_.time()));
    std::cout << __LINE__ << "]\t" << std::endl;
     writer_->write();
    std::cout << __LINE__ << "]\t" << std::endl;
  } //*/
  std::cout << __LINE__ << "]\t" << std::endl;

}

//define this as a plug-in
DEFINE_FWK_MODULE(DumpBFieldRecord);

