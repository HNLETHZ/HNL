from triggers import ele_hlts
from event_content import miniaod_event_content_data, aod_event_content

import FWCore.ParameterSet.Config as cms

process = cms.Process('HNLSKIM')

# this inputs the input files
process.source = cms.Source (
    'PoolSource',
    fileNames=cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/MINIAOD/31Mar2018-v1/30000/D68DB155-E538-E811-B677-0CC47A78A340.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/F0DDCB78-2CE1-E711-8DE5-008CFAC942E0.root /store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/ECBB3B7F-2CE1-E711-9605-008CFA197DA4.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/A48EFA7A-2DE1-E711-88A3-008CFAC93FFC.root /store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/7EF18786-2AE1-E711-927A-001E67D195F0.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/5A8B8882-2BE1-E711-B10E-EC0D9A0B32E0.root /store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/06E0477B-2CE1-E711-BD9B-008CFAC93DB0.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70000/826513DB-FFE0-E711-B572-4C79BA1814C3.root /store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70000/7A1D52F1-FFE0-E711-BC14-4C79BA180929.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70000/62688CF2-FFE0-E711-B9E5-4C79BA180C09.root /store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/A4A7CBA2-99E0-E711-9268-0242AC130002.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/8AB947DB-DDE0-E711-AC9B-FA163E85E28C.root /store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50001/AC0DD52F-A4E0-E711-8E6C-0242AC130002.root',
    )
)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 1000 )
)

# skim by HLT trigger
process.triggerSelection = cms.EDFilter( 
    'TriggerResultsFilter',
    triggerConditions = cms.vstring(ele_hlts),
    hltResults        = cms.InputTag( 'TriggerResults', '', 'HLT' ),
    l1tResults        = cms.InputTag( '' ),
    throw             = cms.bool(False),
)

# path & schedule
process.hltSkim = cms.Path( process.triggerSelection )

# talk to output module
process.out = cms.OutputModule('PoolOutputModule',
#     fileName = cms.untracked.string('miniAOD_singleele_skim.root'),
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
