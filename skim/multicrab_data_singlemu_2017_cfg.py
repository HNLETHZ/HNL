from collections import OrderedDict
from datasets2017 import single_mu
from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'skim_by_hlt_singlemu_cfg.py'
config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['miniAOD_skim.root']
config.Data.splitting          = 'Automatic'

# config.JobType.maxMemoryMB     = 2500
# config.JobType.priority        = 999

# config.Data.unitsPerJob        = 12000
# config.Data.splitting          = 'EventAwareLumiBased'
# JSON files:
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/
config.Data.lumiMask           = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.publication        = True
config.Data.outputDatasetTag   = 'HNLSKIM2017'

config.Site.storageSite        = 'T2_CH_CSCS'
# config.Site.blacklist          = ['T1_US_FNAL']
# config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'test'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_singlemu_' + tag
#     config.Data.outLFNDirBase = '/store/group/phys_tau/HLT2016/' + tag 
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = OrderedDict()

    datasets['SingleMuon2017C'] = ('/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD','/SingleMuon/Run2017C-17Nov2017-v1/AOD')

    for k, v in datasets.iteritems():
        config.General.requestName = k
        config.Data.inputDataset          = v[0]
        config.Data.secondaryInputDataset = v[1]
        print 'submitting config:'
        print config
        submit(config)