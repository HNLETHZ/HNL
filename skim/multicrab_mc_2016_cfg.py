from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['BeamFit_LumiBased_NewAlignWorkflow.txt']
# config.JobType.maxMemoryMB     = 9999
config.JobType.priority        = 9999

config.Data.unitsPerJob        = 40
config.Data.splitting          = 'LumiBased'

config.Data.publication        = False # set it to true for the real thing!
config.Data.outputDatasetTag   = 'ReRecoSept2016v2'

config.Site.storageSite        = 'T2_CH_CERN'
# config.Site.blacklist          = ['T1_US_FNAL']
# config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'ReRecoSept2016v2'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_data_' + tag
    config.Data.outLFNDirBase = '/store/group/phys_tracking/beamspot/13TeV/' + tag 
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = {}

    datasets['ZeroBiasRun2016Bv1'] = ('/ZeroBias/Run2016B-TkAlMinBias-PromptReco-v1/ALCARECO', 'BeamFit_LumiBased_NewAlignWorkflow_ALCARECO.py')
    datasets['ZeroBiasRun2016Bv2'] = ('/ZeroBias/Run2016B-PromptReco-v2/RECO'                , 'BeamFit_LumiBased_NewAlignWorkflow_RECO.py'    )
    datasets['ZeroBiasRun2016Cv2'] = ('/ZeroBias/Run2016C-TkAlMinBias-PromptReco-v2/ALCARECO', 'BeamFit_LumiBased_NewAlignWorkflow_ALCARECO.py')
    datasets['ZeroBiasRun2016Dv2'] = ('/ZeroBias/Run2016D-TkAlMinBias-PromptReco-v2/ALCARECO', 'BeamFit_LumiBased_NewAlignWorkflow_ALCARECO.py')
    datasets['ZeroBiasRun2016Ev2'] = ('/ZeroBias/Run2016E-TkAlMinBias-PromptReco-v2/ALCARECO', 'BeamFit_LumiBased_NewAlignWorkflow_ALCARECO.py')
    datasets['ZeroBiasRun2016Fv1'] = ('/ZeroBias/Run2016F-TkAlMinBias-PromptReco-v1/ALCARECO', 'BeamFit_LumiBased_NewAlignWorkflow_ALCARECO.py')
    datasets['ZeroBiasRun2016Gv1'] = ('/ZeroBias/Run2016G-TkAlMinBias-PromptReco-v1/ALCARECO', 'BeamFit_LumiBased_NewAlignWorkflow_ALCARECO.py')


    
    for k, v in datasets.iteritems():
        config.JobType.psetName    = v[1]
        config.General.requestName = k
        config.Data.inputDataset   = v[0]
        print 'submitting config:'
        print config
        submit(config)

