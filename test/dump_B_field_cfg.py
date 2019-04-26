import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")

process.load("CondCore.CondDB.CondDB_cfi") 

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = '94X_dataRun2_v6'

# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
# process.load("MagneticField.Engine.autoMagneticFieldProducer_cfi")
# process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

# process.load("MagneticField.Engine.autoMagneticFieldProducer_cfi")
# process.AutoMagneticFieldESProducer.valueOverride = 18268

# process.VolumeBasedMagneticFieldESProducer.debugBuilder = True
# process.VolumeBasedMagneticFieldESProducer.label = '3.8T'
# process.VolumeBasedMagneticFieldESProducer.valueOverride = 18268


# process.VolumeBasedMagneticFieldESProducerNew = cms.ESProducer(
#     "VolumeBasedMagneticFieldESProducer",
#     timerOn                     = cms.untracked.bool(False),
#     useParametrizedTrackerField = cms.bool(False),
#     label                       = cms.untracked.string('MFConfig_RI_RII_160812_3_8T'),
#     version                     = cms.string('MFConfig_RI_RII_160812_3_8T'),
#     debugBuilder                = cms.untracked.bool(True),
#     cacheLastVolume             = cms.untracked.bool(True),
#     scalingVolumes              = cms.vint32(),
#     scalingFactors              = cms.vdouble()
# )


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.source = cms.Source("EmptySource")

# talk to output module
# process.out = cms.OutputModule("PoolOutputModule",
#     fileName = cms.untracked.string("test2.root")
# )

# process.source = cms.Source(
#     "PoolSource",
#     fileNames=cms.untracked.vstring('file:/eos/user/d/dezhu/HNL/miniAOD/20180710_miniAOD/heavyNeutrino_23.root'),
# )

process.GlobalTag.toGet.append(
    cms.PSet(
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        record  = cms.string("MagFieldConfigRcd"),
        tag     = cms.string("MFConfig_RI_RII_160812_3_8T"),
        label   = cms.untracked.string("3.8T"),
    ),
)

process.MessageLogger = cms.Service("MessageLogger",
    categories   = cms.untracked.vstring("MagneticField", "AutoMagneticField"),
    destinations = cms.untracked.vstring("cout"),
    cout = cms.untracked.PSet(  
    noLineBreaks = cms.untracked.bool(True),
    threshold = cms.untracked.string("INFO"),
    INFO = cms.untracked.PSet(
      limit = cms.untracked.int32(0)
    ),
    WARNING = cms.untracked.PSet(
      limit = cms.untracked.int32(0)
    ),
    MagneticField = cms.untracked.PSet(
     limit = cms.untracked.int32(10000000)
    )
  )
)

process.TFileService = cms.Service(
    "TFileService", 
    fileName = cms.string("bfield.root"),
    closeFileFast = cms.untracked.bool(False)
)

process.myrootwriter = cms.EDAnalyzer(
    "DumpBFieldRecord",
    field = cms.string(''),
)

process.p = cms.Path(process.myrootwriter)
