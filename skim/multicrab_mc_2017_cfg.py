from collections import OrderedDict
from datasetbkg import all_samples, groups
from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'skim_by_hlt_mc_2017_cfg.py'
config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['miniAOD_skim.root']
config.Data.splitting          = 'Automatic'

# config.JobType.maxMemoryMB     = 2500
# config.JobType.priority        = 999

# config.Data.unitsPerJob        = 12000
# config.Data.splitting          = 'EventAwareLumiBased'
# JSON files:
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/
# config.Data.lumiMask           = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.publication        = True

config.Site.storageSite        = 'T2_CH_CSCS'
# config.Site.blacklist          = ['T1_US_FNAL']
# config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'v1'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_mc2017_' + tag
#     config.Data.outLFNDirBase = '/store/group/phys_tau/HLT2016/' + tag 
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    # subset of samples to run
    mygroups = groups[:1]    # <======== ADAPT THIS TO YOUR CASE!

    for k, v in all_samples.iteritems():
        if k not in mygroups:
            continue
        for kk, vv in v.iteritems():
            config.General.requestName        = kk
            config.Data.inputDataset          = vv[0]
            config.Data.secondaryInputDataset = vv[1]
            config.Data.outputDatasetTag      = 'HNLSKIM2017_'+kk
            print 'submitting config:'
            print config
            submit(config)        
        