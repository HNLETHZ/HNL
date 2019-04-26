from triggers import mu_hlts_2017 
from event_content import miniaod_event_content_data, aod_event_content

import FWCore.ParameterSet.Config as cms

process = cms.Process('HNLSKIM')

# this inputs the input files
process.source = cms.Source (
    'PoolSource',
    fileNames=cms.untracked.vstring(
#         '/store/data/Run2016H/SingleMuon/MINIAOD/18Apr2017-v1/90000/46483D6E-A33E-E711-B0F3-3417EBE644B3.root',
        '/store/data/Run2017D/SingleMuon/MINIAOD/31Mar2018-v1/90000/D42C6863-CB37-E811-B651-20CF3027A5BB.root'
    ),
    secondaryFileNames = cms.untracked.vstring(
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/50000/84E6A8AA-7DE4-E711-91C4-0026B92779B0.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/50000/16178FA7-7DE4-E711-BE46-BC305B390AA7.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/60000/00BF93B0-88DA-E711-8012-7845C4FC374C.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/50000/B42116D2-78E4-E711-87FF-0023AEEEB79C.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/60000/145EE914-B7DA-E711-B26B-180373FFCE1E.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/50000/A21241D2-78E4-E711-BA6A-0023AEEEB79C.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/60000/F8B0CF58-ABDA-E711-827D-008CFAFBE5CE.root',
        '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/60000/A29DFB76-C0DA-E711-82FE-3417EBE6457C.root',
    )
)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 1000 )
)

# skim by HLT trigger
process.triggerSelection = cms.EDFilter( 
    'TriggerResultsFilter',
    triggerConditions = cms.vstring(mu_hlts_2017),
    hltResults        = cms.InputTag( 'TriggerResults', '', 'HLT' ),
    l1tResults        = cms.InputTag( '' ),
    throw             = cms.bool(False),
)

# path & schedule
process.hltSkim = cms.Path( process.triggerSelection )

# talk to output module
process.out = cms.OutputModule('PoolOutputModule',
#     fileName = cms.untracked.string('miniAOD_singlemu_skim.root'),
    fileName = cms.untracked.string('miniAOD_skim.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hltSkim',)
    ),
    outputCommands = cms.untracked.vstring(
        ['drop *'] + miniaod_event_content_data + aod_event_content
    ),
)

# A list of analyzers or output modules to be run after all paths have been run.
process.outpath = cms.EndPath(process.out)

# you want a logger, don't you?
process.MessageLogger = cms.Service("MessageLogger")
