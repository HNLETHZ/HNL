import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

# FIXME! put the right cross sections

''' makeMyPrivateDataComponent is a copy of MakeMyPrivateMCComponent in ComponentCreator.py
    this should be adjusted (i guess) to include some data only attributes, like lumi, etc.
'''
json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

Single_ele_2017B  = creator.makeDataComponent('Single_ele_2017B', '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2017C  = creator.makeDataComponent('Single_ele_2017C', '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2017D  = creator.makeDataComponent('Single_ele_2017D', '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2017E  = creator.makeDataComponent('Single_ele_2017E', '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
Single_ele_2017F  = creator.makeDataComponent('Single_ele_2017F', '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD', 'CMS', '.*root', json, useAAA=True)
                                                                                                                            
Single_mu_2017B   = creator.makeDataComponent('Single_mu_2017B' , '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2017C   = creator.makeDataComponent('Single_mu_2017C' , '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2017D   = creator.makeDataComponent('Single_mu_2017D' , '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2017E   = creator.makeDataComponent('Single_mu_2017E' , '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)
Single_mu_2017F   = creator.makeDataComponent('Single_mu_2017F' , '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD'    , 'CMS', '.*root', json, useAAA=True)

Single_ele_2017 = [
    Single_ele_2017B,
    Single_ele_2017C,
    Single_ele_2017D,
    Single_ele_2017E,
    Single_ele_2017F,
]

Single_mu_2017 = [
    Single_mu_2017B ,
    Single_mu_2017C ,
    Single_mu_2017D ,
    Single_mu_2017E ,
    Single_mu_2017F ,
] 
