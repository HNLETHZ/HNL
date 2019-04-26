'''
wget http://tomc.web.cern.ch/tomc/availableDisplacedTrileptonSamples.txt
wget http://tomc.web.cern.ch/tomc/privateHeavyNeutrinoSamples.txt
'''

from collections import OrderedDict

class HNLSample():
    def __init__(self, path):#mass, v2, ctau, nevents, path, files=[]):
        self.path    = path   
#        self.mass    = mass   
#        self.v2      = v2     
#        self.ctau    = ctau   
#        self.nevents = nevents
#        self.files   = files
        self.name    = path.split('/')[-1]
    
    def __str__(self):
        import pdb ; pdb.set_trace()
        blabla  = self.name
#        blabla += '\n\tmass [GeV] %.1f' %self.mass
#        blabla += '\n\tv2         %f'   %self.v2
#        blabla += '\n\tctau [mm]  %.2f' %self.ctau
#        blabla += '\n\tnevents    %d'   %self.nevents
        blabla += '\n\t'+str(self.files)
        return blabla
    
    def _prependPath(self):
        self.files = ['/'.join(['root://cms-xrd-global.cern.ch/', self.path, ifile]) for ifile in self.files]

toread = [
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00282842712475_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00282842712475_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00282842712475_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00547722557505_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00547722557505_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00547722557505_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00707106781187_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00707106781187_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00707106781187_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00836660026534_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00836660026534_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00836660026534_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00282842712475_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00282842712475_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316227766017_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316227766017_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_tau_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_e_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_mu_massiveAndCKM_LO'),
    HNLSample('/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_tau_massiveAndCKM_LO'),
]

samplesdict = OrderedDict()

#with open('privateHeavyNeutrinoSamples.txt') as ff:
# with open('test.txt') as ff:
#    content = ff.readlines()

#current_key = ''
#for ii, line in enumerate(content):
#    line = line.rstrip()
#    if line.startswith('/pnfs/iihe/cms/'):
#        current_key = line.replace(':','')
#    if current_key not in samplesdict.keys():
#        samplesdict[current_key] = []
#    elif line.startswith('heavyNeutrino'):
#        samplesdict[current_key].append(line)
#    else:
#        print 'finished with', current_key
#     import pdb; pdb.set_trace()

#print '\n\n\n\n\n'

for sample in toread:
    if sample.path not in samplesdict.keys():
        print sample.path, 'missing'
        continue
    sample.files = samplesdict[sample.path]
    sample._prependPath()





