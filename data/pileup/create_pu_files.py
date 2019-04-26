import ROOT
from copy import deepcopy as dc
from collections import OrderedDict

# albert = ROOT.TFile.Open('htt_stuff/pileup_2017_albert.root', 'read')
albert = ROOT.TFile.Open('/afs/cern.ch/user/a/adow/public/PU2017/pileup_2017.root', 'read')

samples = OrderedDict()

samples['DYJetsToLL_M50'    ] = 'pileup_DYJetsToLL'    
samples['DYJetsToLL_M50_ext'] = 'pileup_DYJetsToLL-ext'
samples['WZTo3LNu'          ] = 'pileup_WZTo3LNu'      
samples['ZZTo4L'            ] = 'pileup_ZZTo4L'        
samples['ZZTo4L_ext'        ] = 'pileup_ZZTo4L-ext'    
samples['WJetsToLNu'        ] = 'pileup_WJetsToLNu-LO'
samples['W3JetsToLNu'       ] = 'pileup_W3JetsToLNu-LO'
samples['W4JetsToLNu'       ] = 'pileup_W4JetsToLNu-LO'

for k, v in samples.iteritems():
    print k
    albert.cd()
    h1 = dc(albert.Get(v))
    h1.SetName('pileup')
    outfile = ROOT.TFile.Open('pileup_'+k+'.root', 'recreate')
    outfile.cd()
    h1.Write()
    outfile.Close()

