from triggers import mu_hlts, ele_hlts
from event_content import miniaod_event_content_mc, aod_event_content

import FWCore.ParameterSet.Config as cms

process = cms.Process('HNLSKIM')

# this inputs the input files
process.source = cms.Source (
    'PoolSource',
    fileNames=cms.untracked.vstring(
        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110000/005ED0EB-79F1-E611-B6DA-02163E011C2B.root',
#         '/store/mc/RunIISummer16MiniAODv2/WZTo3LNu_mllmin01_13TeV-powheg-pythia8_ext1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/110000/7849DACC-39DE-E611-B5EF-0CC47A7C35D2.root',
#         '/store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/AE4923DC-8FBD-E611-BE69-0CC47AD98F70.root',
#         '/store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/CC4F79C7-ACBD-E611-94B2-0025905B859E.root',
#         '/store/mc/RunIISummer16MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D4D9231F-27BE-E611-9EEB-001E67504F55.root',
#         '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B249E9C0-23BC-E611-A811-001E67A4061D.root',
#         '/store/mc/RunIISummer16MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DA7BCA69-5BB9-E611-AC7F-A0000420FE80.root',
#         '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/B2E53696-84D8-E611-A2BD-A4BADB1E6F7A.root',
#         '/store/mc/RunIISummer16MiniAODv2/tZq_ll_4f_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AC1D0602-5DC0-E611-B234-848F69FD29D0.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/062AB3F9-48F1-E611-B7BC-02163E0137A0.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/124AC56C-42F1-E611-91DB-02163E019D4A.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/2029FDDB-44F1-E611-91E2-02163E01436E.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/22AAE483-46F1-E611-901C-02163E019BD7.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/30D98C18-40F1-E611-A97C-02163E019B82.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/8475F869-42F1-E611-9CBC-02163E01A495.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/8A2C77FF-48F1-E611-859A-02163E014447.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/A413BD73-42F1-E611-8D69-02163E014294.root',
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/110002/B0DA89D6-44F1-E611-A240-02163E019DDC.root',
  )
)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 1000 )
)

# skim by HLT trigger
process.triggerSelection = cms.EDFilter( 
    'TriggerResultsFilter',
    triggerConditions = cms.vstring(mu_hlts + ele_hlts),
    hltResults        = cms.InputTag( 'TriggerResults', '', 'HLT' ),
    l1tResults        = cms.InputTag( '' ),
    throw             = cms.bool(False),
)

# path & schedule
process.hltSkim = cms.Path( process.triggerSelection )

# talk to output module
process.out = cms.OutputModule('PoolOutputModule',
    fileName = cms.untracked.string('miniAOD_skim.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hltSkim',)
    ),
    outputCommands = cms.untracked.vstring(
        ['drop *'] + miniaod_event_content_mc + aod_event_content
    ),
)

# A list of analyzers or output modules to be run after all paths have been run.
process.outpath = cms.EndPath(process.out)

# you want a logger, don't you?
process.MessageLogger = cms.Service("MessageLogger")
