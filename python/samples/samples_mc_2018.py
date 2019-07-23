import PhysicsTools.HeppyCore.framework.config as cfg
import os

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable
# https://twiki.cern.ch/twiki/bin/view/CMS/EgHLTRunIISummary#2018_AN1

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

TTJets = creator.makeMCComponent(
    name    = 'TTJets', 
    dataset = '/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 831.76, 
    useAAA  = True
)
TTJets .nGenEvents = TTJets.dataset_entries 

TTJets_ext = creator.makeMCComponent(
    name    = 'TTJets_ext', 
    dataset = '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 831.76, 
    useAAA  = True
)
TTJets_ext .nGenEvents = TTJets_ext.dataset_entries 


WJetsToLNu = creator.makeMCComponent(
    name    = 'WJetsToLNu', 
    dataset = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 59850.,
    useAAA  = True
)
WJetsToLNu .nGenEvents = WJetsToLNu.dataset_entries 


DYBB = creator.makeMCComponent(
    name    = 'DYBB',
    dataset = '/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root',
    xSec    = 1.459e+01,# +- 5.139e-02 pb
    useAAA  = True
)
DYBB .nGenEvents = DYBB.dataset_entries 


DYJetsToLL_M5to50 = creator.makeMCComponent(
    name    = 'DYJetsToLL_M50to50',
    dataset = '/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root',
    xSec    = -99,
    useAAA  = True
)
DYJetsToLL_M5to50.nGenEvents = DYJetsToLL_M5to50.dataset_entries 


DYJetsToLL_M50 = creator.makeMCComponent(
    name    = 'DYJetsToLL_M50',
    dataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', 
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 2075.14*3, 
    useAAA  = True
)
DYJetsToLL_M50.nGenEvents = DYJetsToLL_M50.dataset_entries


DYJetsToLL_M50_ext = creator.makeMCComponent(
    name    = 'DYJetsToLL_M50_ext',
    dataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    # xSec    = 1921.8*3, #oldValue 
    xSec    = 2075.14*3, 
    useAAA  = True
)
DYJetsToLL_M50_ext.nGenEvents = DYJetsToLL_M50_ext.dataset_entries


#from fall17 samples of https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDMeasurementsHelp#2017_measurements_MC2017_v2_samp
WW = creator.makeMCComponent(
    name    = 'WW',
    dataset = '/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
    user    = 'CMS',
    pattern = '.*root', 
    xSec    = 75.88, 
    useAAA  = True
)
WW.nGenEvents = WW.dataset_entries


#from fall17 samples of https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDMeasurementsHelp#2017_measurements_MC2017_v2_samp
WZ = creator.makeMCComponent(
    name    = 'WZ',
    dataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',
    user    = 'CMS',
    pattern = '.*root', 
    xSec    = 27.6, 
    useAAA  = True
)
WZ.nGenEvents = WZ.dataset_entries


#from fall17 samples of https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDMeasurementsHelp#2017_measurements_MC2017_v2_samp
ZZ = creator.makeMCComponent(
    name    = 'ZZ',
    dataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
    user    = 'CMS',
    pattern = '.*root', 
    xSec    = 12.14, 
    useAAA  = True
)
ZZ.nGenEvents = ZZ.dataset_entries


# LINK for crosssections: 
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDMeasurementsHelp#2017_measurements_MC2017_v2_samp

##########################################################################################
# assign to each sample its own PU profile file. For 2017 it is important to do it per-sample
##########################################################################################
# TODO temporary workaround for pu of new samples
# DYBB                                      .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYBB.root' 
# DYJetsToLL_M10to50                        .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJets_M10to50.root' 
# DYJetsToLL_M50                            .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJetsToLL_M50.root' 
# DYJetsToLL_M50_ext                        .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJetsToLL_M50_ext.root' 
# WJetsToLNu                                .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WJetsToLNu.root'  
##########################################################################################

##########################################################################################
#  data PileUp profile
##########################################################################################
# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Pileup_JSON_Files_For_Run_II
# have a loo at this too, the mb cross section might be off https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/755.html
'''
pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt\
              --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PileUp/pileup_latest.txt\
              --calcMode true --minBiasXsec 69200 --maxPileupBin 200 --numPileupBins 200  pileup_data_golden_json_2017.root
'''
# for ibkg in hnl_bkg_noskim:
    # ibkg.puFileData = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_data_golden_json_2017.root'

