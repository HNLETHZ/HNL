import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

# FIXME! put the right cross sections

''' makeMyPrivateDataComponent is a copy of MakeMyPrivateMCComponent in ComponentCreator.py
    this should be adjusted (i guess) to include some data only attributes, like lumi, etc.
'''


# TODO json taken from here, probably needs update https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt
#try: json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
json = '../python/samples/golden_but_json.txt'
# Luminosity:59.69 /fb 


# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable
# https://twiki.cern.ch/twiki/bin/view/CMS/EgHLTRunIISummary#2018_AN1

Single_ele_2018A  = creator.makeDataComponent('Single_ele_2018A', '/EGamma/Run2018A-17Sep2018-v2/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2018B  = creator.makeDataComponent('Single_ele_2018B', '/EGamma/Run2018B-17Sep2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2018C  = creator.makeDataComponent('Single_ele_2018C', '/EGamma/Run2018C-17Sep2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2018D  = creator.makeDataComponent('Single_ele_2018D', '/EGamma/Run2018D-22Jan2019-v2/MINIAOD', 'CMS', '.*root', json, useAAA=True)
                                                                                                                            
Single_mu_2018A   = creator.makeDataComponent('Single_mu_2018A' , '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2018B   = creator.makeDataComponent('Single_mu_2018B' , '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2018C   = creator.makeDataComponent('Single_mu_2018C' , '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2018D   = creator.makeDataComponent('Single_mu_2018D' , '/SingleMuon/Run2018D-30Apr2019-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)

Single_ele_2018 = [
    Single_ele_2018A,
    Single_ele_2018B,
    Single_ele_2018C,
    Single_ele_2018D,
]

Single_mu_2018 = [
    Single_mu_2018A ,
    Single_mu_2018B ,
    Single_mu_2018C ,
    Single_mu_2018D ,
] 
