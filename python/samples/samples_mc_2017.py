import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

# FIXME! put the right cross sections
# FIXME! check in ComponentCreator how to cache the file fetching
# FIXME! create meaningful lists

TTJets_amcat                    = creator.makeMyPrivateMCComponent('TTJets_amcat'                  , '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/vstampf-HNLSKIM2017_TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                         , 'PRIVATE', '*.root', 'phys03', xSec=831.76, useAAA=True)
TTJets_amcat        .nGenEvents = 153432257 
#.sigma = 831.76 pb; .nevents = 39769534

TTJets_mdgrph                   = creator.makeMyPrivateMCComponent('TTJets_madgraph'               , '/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/vstampf-HNLSKIM2017_TTJets_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                           , 'PRIVATE', '*.root', 'phys03', xSec=831.76, useAAA=True)
TTJets_mdgrph       .nGenEvents = 615134
#.sigma = NOT FOUND pb; .nevents = 158461 
              
DYJetsToLL_M50                  = creator.makeMyPrivateMCComponent('DYJetsToLL_M50'                , '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/manzoni-HNLSKIM2017_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                       , 'PRIVATE', '*.root', 'phys03', xSec=2075.14*3, useAAA=True)#old xSec: 1921.8*3
DYJetsToLL_M50      .nGenEvents = 27413121
#.sigma = 1921.8*3 pb; .nevents = 11074873 
DYJetsToLL_M50_ext              = creator.makeMyPrivateMCComponent('DYJetsToLL_M50_ext'            , '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/manzoni-HNLSKIM2017_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_ext-115d0bad8e8ff59118d83f903524e0b3/USER'                   , 'PRIVATE', '*.root', 'phys03', xSec=2075.14*3, useAAA=True)#old xSec: 1921.8*3
DYJetsToLL_M50_ext  .nGenEvents = 158048935
#.sigma = 1921.8*3 pb; .nevents = 63912552; .L = 11085.536476220212 pb^-1 

WLLJJ_WToLNu_EWK                = creator.makeMyPrivateMCComponent('WLLJJ_WToLNu_EWK'              , '/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/manzoni-HNLSKIM2017_WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'             , 'PRIVATE', '*.root', 'phys03', useAAA=True)
WLLJJ_WToLNu_EWK    .nGenEvents = 880000
#.sigma = NOT FOUND pb

WW_DoubleScattering             = creator.makeMyPrivateMCComponent('WW_DoubleScattering'           , '/WW_DoubleScattering_13TeV-pythia8_TuneCP5/manzoni-HNLSKIM2017_WW_DoubleScattering_13TeV-pythia8_TuneCP5-115d0bad8e8ff59118d83f903524e0b3/USER'                                         , 'PRIVATE', '*.root', 'phys03', useAAA=True)
WW_DoubleScattering .nGenEvents = 1000000 
#.sigma = NOT FOUND pb
 
WZTo3LNu                        = creator.makeMyPrivateMCComponent('WZTo3LNu'                      , '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/manzoni-HNLSKIM2017_WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                     , 'PRIVATE', '*.root', 'phys03', xSec=4.4297, useAAA=True)
WZTo3LNu            .nGenEvents = 10881896 
#.sigma = 4.4297 pb

# ZZTo4L                          = creator.makeMyPrivateMCComponent('ZZTo4L'                        , '/ZZTo4L_13TeV_powheg_pythia8/manzoni-HNLSKIM2017_ZZTo4L_13TeV_powheg_pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                                                     , 'PRIVATE', '*.root', 'phys03', xSec=1.256, useAAA=True)
ZZTo4L                          = creator.makeMyPrivateMCComponent('ZZTo4L'                        , '/ZZTo4L_13TeV_powheg_pythia8/manzoni-HNLSKIM2017_ZZTo4L_13TeV_powheg_pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                                                     , 'PRIVATE', '*.root', 'phys03', xSec=1.325, useAAA=True)
ZZTo4L              .nGenEvents = 6835701 
#.sigma = 1.256 pb

ZZTo4L_ext                      = creator.makeMyPrivateMCComponent('ZZTo4L_ext'                    , '/ZZTo4L_13TeV_powheg_pythia8/manzoni-HNLSKIM2017_ZZTo4L_13TeV_powheg_pythia8_ext-115d0bad8e8ff59118d83f903524e0b3/USER'                                                                 , 'PRIVATE', '*.root', 'phys03', xSec=1.256, useAAA=True)
ZZTo4L_ext          .nGenEvents = 98009599
#.sigma = 1.256 pb


WJetsToLNu                      = creator.makeMyPrivateMCComponent('WJetsToLNu'                    , '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                  , 'PRIVATE', '*.root', 'phys03', xSec=59850., useAAA=True)
WJetsToLNu          .nGenEvents = 44652002 # check the production efficiency in Lesya's crab job
#.sigma = (8580+11370)*3 pb ==> xs W+ + xs W- * BR -->l nu *3  




WJetsToLNu_HT400To600           = creator.makeMyPrivateMCComponent('WJetsToLNu_HT400To600'         , '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'          , 'PRIVATE', '*.root', 'phys03', xSec=48.91, useAAA=True)
#.sigma = 48.91 \pm 0.072 pb (LO); .nevents = 5572699 
WJetsToLNu_HT600To800           = creator.makeMyPrivateMCComponent('WJetsToLNu_HT600To800'         , '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'          , 'PRIVATE', '*.root', 'phys03', xSec=12.05, useAAA=True)
#.sigma = 12.05 \pm 0.0073 pb (LO); .nevents = 4443563
WJetsToLNu_HT800To1200          = creator.makeMyPrivateMCComponent('WJetsToLNu_HT800To1200'        , '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'        , 'PRIVATE', '*.root', 'phys03', xSec=5.501, useAAA=True)
#.sigma = 5.501 \pm 0.017 pb (LO); .nevents = 8675292 
WJetsToLNu_HT1200To2500         = creator.makeMyPrivateMCComponent('WJetsToLNu_HT1200To2500'       , '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'      , 'PRIVATE', '*.root', 'phys03', xSec=1.329, useAAA=True)
#.sigma = 1.329 \pm 0.0025 pb (LO); .nevents = 5696067 
# WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8.sigma = 20508.9*3 pb
 
W1JetsToLNu_LHEWpT_250_400      = creator.makeMyPrivateMCComponent('W1JetsToLNu_LHEWpT_250_400'    , '/W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'    , 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 11545472 
W1JetsToLNu_LHEWpT_400_inf      = creator.makeMyPrivateMCComponent('W1JetsToLNu_LHEWpT_400_inf'    , '/W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'    , 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 2822947 
W1JetsToLNu_LHEWpT_400_inf_ext  = creator.makeMyPrivateMCComponent('W1JetsToLNu_LHEWpT_400_inf_ext', '/W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_ext-115d0bad8e8ff59118d83f903524e0b3/USER', 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 3139785 
 
W2JetsToLNu_LHEWpT_50_150       = creator.makeMyPrivateMCComponent('W2JetsToLNu_LHEWpT_50_150 '    , '/W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'      , 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 10755628 
W2JetsToLNu_LHEWpT_100_150      = creator.makeMyPrivateMCComponent('W2JetsToLNu_LHEWpT_100_150'    , '/W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'    , 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 14264210 
W2JetsToLNu_LHEWpT_250_400      = creator.makeMyPrivateMCComponent('W2JetsToLNu_LHEWpT_250_400'    , '/W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'    , 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 38515628
W2JetsToLNu_LHEWpT_400_inf      = creator.makeMyPrivateMCComponent('W2JetsToLNu_LHEWpT_400_inf'    , '/W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/lshchuts-HNLSKIM2017_W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'    , 'PRIVATE', '*.root', 'phys03', useAAA=True)
#.sigma = NOT FOUND pb; .nevents = 18636486 
 
W3JetsToLNu                     = creator.makeMyPrivateMCComponent('W3JetsToLNu'                   , '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                , 'PRIVATE', '*.root', 'phys03', xSec=993.4*1.17, useAAA=True)
#.sigma = 993.4*1.17 pb; .nevents = 6265138; .L = 5390.395413145565 pb^-1 
 
W4JetsToLNu                     = creator.makeMyPrivateMCComponent('W4JetsToLNu'                   , '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/lshchuts-HNLSKIM2017_W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-115d0bad8e8ff59118d83f903524e0b3/USER'                                , 'PRIVATE', '*.root', 'phys03', xSec=542.4*1.17, useAAA=True)
#.sigma = 542.4*1.17 pb; .nevents = 3356894; .L = 5289.712704535714 pb^-1  

# LINK for crosssections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns

##########################################################################################
# assign to each sample its own PU profile file. For 2017 it is important to do it per-sample
##########################################################################################
TTJets_amcat                   .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTJets_amcat_full.root'                   # not in Albert, derived manually
# TTJets_mdgrph                  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTJets_mdgrph.root'                  # not in Albert
DYJetsToLL_M50                 .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJetsToLL_M50.root'                 # in Albert DYJetsToLL  /DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
DYJetsToLL_M50_ext             .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJetsToLL_M50_ext.root'             # in Albert DYJetsToLL-ext  /DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM
# WLLJJ_WToLNu_EWK               .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WLLJJ_WToLNu_EWK.root'               # not in Albert
# WW_DoubleScattering            .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WW_DoubleScattering.root'            # not in Albert
WZTo3LNu                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WZTo3LNu.root'                       # in Albert WZTo3LNu  /WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
ZZTo4L                         .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ZZTo4L.root'                         # in Albert ZZTo4L  /ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
ZZTo4L_ext                     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ZZTo4L_ext.root'                     # in Albert ZZTo4L-ext  /ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM
# WJetsToLNu_HT400To600          .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WJetsToLNu_HT400To600.root'          # not in Albert
# WJetsToLNu_HT600To800          .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WJetsToLNu_HT600To800.root'          # not in Albert
# WJetsToLNu_HT800To1200         .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WJetsToLNu_HT800To1200.root'         # not in Albert
# WJetsToLNu_HT1200To2500        .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WJetsToLNu_HT1200To2500.root'        # not in Albert
# W1JetsToLNu_LHEWpT_250_400     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W1JetsToLNu_LHEWpT_250_400.root'     # not in Albert
# W1JetsToLNu_LHEWpT_400_inf     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W1JetsToLNu_LHEWpT_400_inf.root'     # not in Albert
# W1JetsToLNu_LHEWpT_400_inf_ext .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W1JetsToLNu_LHEWpT_400_inf_ext.root' # not in Albert
# W2JetsToLNu_LHEWpT_50_150      .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W2JetsToLNu_LHEWpT_50_150.root'      # not in Albert
# W2JetsToLNu_LHEWpT_100_150     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W2JetsToLNu_LHEWpT_100_150.root'     # not in Albert
# W2JetsToLNu_LHEWpT_250_400     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W2JetsToLNu_LHEWpT_250_400.root'     # not in Albert
# W2JetsToLNu_LHEWpT_400_inf     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W2JetsToLNu_LHEWpT_400_inf.root'     # not in Albert
WJetsToLNu                     .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WJetsToLNu.root'                    # in Albert W3JetsToLNu-LO  /W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
W3JetsToLNu                    .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W3JetsToLNu.root'                    # in Albert W3JetsToLNu-LO  /W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
W4JetsToLNu                    .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_W4JetsToLNu.root'                    # in Albert W4JetsToLNu-LO  /W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM


##########################################################################################
hnl_bkg = [
    TTJets_amcat                  ,
    TTJets_mdgrph                 ,
 
    DYJetsToLL_M50                ,
    DYJetsToLL_M50_ext            ,

    WLLJJ_WToLNu_EWK              ,
    WW_DoubleScattering           ,
    WZTo3LNu                      ,
    ZZTo4L                        ,
    ZZTo4L_ext                    ,

    WJetsToLNu_HT400To600         ,
    WJetsToLNu_HT600To800         ,
    WJetsToLNu_HT800To1200        ,
    WJetsToLNu_HT1200To2500       ,
 
    W1JetsToLNu_LHEWpT_250_400    ,
    W1JetsToLNu_LHEWpT_400_inf    ,
    W1JetsToLNu_LHEWpT_400_inf_ext,
 
    W2JetsToLNu_LHEWpT_50_150     ,
    W2JetsToLNu_LHEWpT_100_150    ,
    W2JetsToLNu_LHEWpT_250_400    ,
    W2JetsToLNu_LHEWpT_400_inf    ,
 
    WJetsToLNu                    ,
    W3JetsToLNu                   ,
    W4JetsToLNu                   ,
] 

hnl_bkg_essentials = [
    TTJets_amcat      ,
    DYJetsToLL_M50_ext,
    WW_DoubleScattering,
    WZTo3LNu          ,
    ZZTo4L            ,
    WJetsToLNu        ,
]

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
for ibkg in hnl_bkg:
    ibkg.puFileData = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_data_golden_json_2017.root'








