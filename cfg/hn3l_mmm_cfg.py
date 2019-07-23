from CMGTools.HNL.hn3l_cfg import *

# specify the samples considered
from CMGTools.HNL.samples.samples_data_2018 import Single_mu_2018, Single_mu_2018A, Single_mu_2018B, Single_mu_2018C, Single_mu_2018D
from CMGTools.HNL.samples.samples_mc_2018   import TTJets, TTJets_ext, WJetsToLNu, DYBB, DYJetsToLL_M5to50, DYJetsToLL_M50, DYJetsToLL_M50_ext, WW, WZ, ZZ 

samples = [TTJets, WJetsToLNu, TTJets_ext, DYBB, DYJetsToLL_M5to50, DYJetsToLL_M50, DYJetsToLL_M50_ext, WW, WZ, ZZ]
samples = [Single_mu_2018A, Single_mu_2018B, Single_mu_2018C, Single_mu_2018D]
samples = [DYBB]


# edit the lines here to specify your ntuple production mode production         = False # state whether you're running production mode or not
production         = False # state whether you're running production mode or not
isData             = False
isSignal           = False
promptLeptonType   = "mu" # choose from 'ele', 'mu'
L1L2LeptonType     = "mm"  # choose from 'ee', 'mm', 'em'

# this calls the master cfg file with the proper settings
config = generateKeyConfigs(samples,production, promptLeptonType, L1L2LeptonType, isData = isData, isSignal = isSignal)
