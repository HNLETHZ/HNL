from triggers import mu_hlts_2017, ele_hlts_2017
from event_content import miniaod_event_content_mc, aod_event_content

import FWCore.ParameterSet.Config as cms

process = cms.Process('HNLSKIM')

# this inputs the input files
process.source = cms.Source (
    'PoolSource',
    fileNames=cms.untracked.vstring(
        '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/10661591-8E42-E811-91ED-0025905C94D0.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
        '/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/08F53DF1-0E1C-E811-94F2-6C3BE5B5B078.root',
        '/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/ACB69933-471C-E811-B238-0CC47A4D765E.root',
        '/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/C8285EF8-561D-E811-A90F-0CC47A4D767E.root',
        '/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/F260F37A-381C-E811-B288-38EAA78E2C94.root',
        '/store/mc/RunIIFall17DRPremix/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/AODSIM/94X_mc2017_realistic_v11-v1/00000/FCFB3502-291C-E811-818F-38EAA78D8B54.root',
  )
)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 1000 )
)

# skim by HLT trigger
process.triggerSelection = cms.EDFilter( 
    'TriggerResultsFilter',
    triggerConditions = cms.vstring(mu_hlts_2017 + ele_hlts_2017),
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
