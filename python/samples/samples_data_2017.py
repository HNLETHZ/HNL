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

Single_ele_2017  = creator.makeMyPrivateDataComponent('Single_ele_2017' ,'/SingleElectron/vstampf-HNLSKIM2017-a3ebfef9ab75dc703a0292f5032c1af2/USER', 'PRIVATE', '*.root', json, 'phys03', useAAA=True)
Single_ele_2017.nGenEvents = 460572549 # 56501676 (B) + 127366693 (C) + 50610320 (D) + 31945 (E resub) + 100173177 (E 1st round) + 125888738 (F)

Single_mu_2017   = creator.makeMyPrivateDataComponent('Single_mu_2017'  , '/SingleMuon/dezhu-HNLSKIM2017-6c435cbb87e441358a32d522d9d7cdf0/USER'     , 'PRIVATE', '*.root', json, 'phys03', useAAA=True)
Single_mu_2017.nGenEvents = 738091715 # 128496874 (B) + 154640002 (C) + 69031074 (D) + 151165497 (E) + 234758268 (F)

hnl_data = [
    Single_ele_2017,
    Single_mu_2017 ,
] 
