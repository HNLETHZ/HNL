'''
wget http://tomc.web.cern.ch/tomc/availableDisplacedTrileptonSamples.txt
wget http://tomc.web.cern.ch/tomc/privateHeavyNeutrinoSamples.txt

13/9/2018
wget http://tomc.web.cern.ch/tomc/availableHeavyNeutrinoSamples.txt
wget http://tomc.web.cern.ch/tomc/heavyNeutrinoFileList.txt
'''

from collections import OrderedDict

class HNLSample():
    def __init__(self, mass, v2, ctau, nevents, xs, xse, path, files=[]):
        self.path    = path   
        self.mass    = mass   
        self.v2      = v2     
        self.ctau    = ctau  # [mm]
        self.nevents = nevents
        self.xs      = xs
        self.xse     = xse
        self.files   = files
        self.name    = path.split('/')[-1]
        self.title   = path.split('/')[-1].replace('.', 'p').replace('HeavyNeutrino_trilepton', 'HN3L').replace('HN3L_M-','HN3L_M_').replace('V-0p', 'V_0p')
    
    def __str__(self):
#         import pdb ; pdb.set_trace()
        blabla  = self.title
        blabla += '\n\tmass [GeV] %.1f' %self.mass
        blabla += '\n\tv2         %f'   %self.v2
        blabla += '\n\tctau [mm]  %.2f' %self.ctau
        blabla += '\n\tnevents    %d'   %self.nevents
        blabla += '\n\txs         %.5f' %self.xs
        blabla += '\n\txse        %.5f' %self.xse
        blabla += '\n\t'+str(self.files)
        return blabla
    
    def _prependPath(self):
        self.files = ['/'.join(['root://cms-xrd-global.cern.ch/', self.path, ifile]) for ifile in self.files]

# look for duplicates
#     HNLSample(    2.0   ,   1e-05   , 1943.42   ,   99000   ,   4.295e-02 , 2.337e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_mu_massiveAndCKM_LO'         ),
#     HNLSample(    2.0   ,   1e-05   , 1943.42   ,   95000   ,   4.205e+00 , 2.507e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_mu_massiveAndCKM_LO'                    ),
# M-2_V-0.00316227766017_mu_massiveAndCKM_LO

toread = [
    HNLSample(    2.0   ,   6e-06   , 3202.92   ,  100000   ,   2.558e-02 , 1.392e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_e_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   6e-06   , 3239.05   ,  100000   ,   2.570e-02 , 1.398e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_mu_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,   6e-06   , 9289.46   ,   89000   ,   1.081e-02 , 6.103e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_tau_massiveAndCKM_LO'        ),
    HNLSample(    2.0   ,   8e-06   , 2402.24   ,   99000   ,   3.448e-02 , 1.947e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00282842712475_e_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   8e-06   , 2429.28   ,  100000   ,   3.436e-02 , 1.870e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00282842712475_mu_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,   8e-06   , 6967.10   ,   47000   ,   1.463e-02 , 7.955e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00282842712475_tau_massiveAndCKM_LO'        ),
    HNLSample(    2.0   ,   1e-05   , 1921.77   ,  100000   ,   4.322e-02 , 2.323e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_e_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   1e-05   , 1943.42   ,   99000   ,   4.295e-02 , 2.337e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_mu_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,   1e-05   , 5573.68   ,  100000   ,   1.825e-02 , 9.924e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_tau_massiveAndCKM_LO'        ),
    HNLSample(    2.0   ,   2e-05   ,  960.89   ,  100000   ,   8.505e-02 , 4.659e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_e_massiveAndCKM_LO'            ),
    HNLSample(    2.0   ,   2e-05   ,  971.70   ,  100000   ,   8.619e-02 , 4.691e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_mu_massiveAndCKM_LO'           ),
    HNLSample(    2.0   ,   2e-05   , 2786.85   ,   86000   ,   3.649e-02 , 1.984e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_tau_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   3e-05   ,  640.58   ,   99000   ,   1.287e-01 , 6.740e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00547722557505_e_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   3e-05   ,  647.80   ,  100000   ,   1.295e-01 , 7.189e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00547722557505_mu_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,   3e-05   , 1857.91   ,   88000   ,   5.492e-02 , 2.960e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00547722557505_tau_massiveAndCKM_LO'        ),
    HNLSample(    2.0   ,   5e-05   ,  384.36   ,  100000   ,   2.163e-01 , 1.162e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00707106781187_e_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   5e-05   ,  388.68   ,  100000   ,   2.151e-01 , 1.161e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00707106781187_mu_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,   5e-05   , 1114.75   ,  100000   ,   9.019e-02 , 4.952e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00707106781187_tau_massiveAndCKM_LO'        ),
    HNLSample(    2.0   ,   7e-05   ,  274.54   ,  100000   ,   2.987e-01 , 1.626e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00836660026534_e_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,   7e-05   ,  277.63   ,  100000   ,   3.022e-01 , 1.631e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00836660026534_mu_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,   7e-05   ,  796.24   ,   88000   ,   1.284e-01 , 6.922e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00836660026534_tau_massiveAndCKM_LO'        ),
    HNLSample(    2.0   ,  0.0002   ,   96.09   ,  100000   ,   8.604e-01 , 4.776e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_e_massiveAndCKM_LO'           ),
    HNLSample(    2.0   ,  0.0002   ,   97.17   ,  100000   ,   8.452e-01 , 4.577e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_mu_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,  0.0002   ,  278.68   ,   99000   ,   3.609e-01 , 2.003e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_tau_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,  0.0003   ,   64.06   ,  100000   ,   1.268e+00 , 6.868e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_e_massiveAndCKM_LO'           ),
    HNLSample(    2.0   ,  0.0003   ,   64.78   ,  100000   ,   1.296e+00 , 6.991e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_mu_massiveAndCKM_LO'          ),
    HNLSample(    2.0   ,  0.0003   ,  185.79   ,   87000   ,   5.486e-01 , 2.983e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_tau_massiveAndCKM_LO'         ),
    HNLSample(    2.0   ,  0.0001   ,  192.18   ,  100000   ,   4.296e-01 , 2.250e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_e_massiveAndCKM_LO'                      ),
    HNLSample(    2.0   ,  0.0001   ,  194.34   ,  100000   ,   4.295e-01 , 2.338e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_mu_massiveAndCKM_LO'                     ),
    HNLSample(    2.0   ,  0.0001   ,  557.37   ,   79000   ,   1.828e-01 , 9.940e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_tau_massiveAndCKM_LO'                    ),
    HNLSample(    2.0   ,  0.0005   ,   38.44   ,  100000   ,   2.143e+00 , 1.123e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_e_massiveAndCKM_LO'            ),
    HNLSample(    2.0   ,  0.0005   ,   38.87   ,  100000   ,   2.182e+00 , 1.143e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_mu_massiveAndCKM_LO'           ),
    HNLSample(    2.0   ,  0.0005   ,  111.47   ,   93000   ,   9.131e-01 , 4.782e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_tau_massiveAndCKM_LO'          ),
    HNLSample(    3.0   ,   6e-06   , 1059.86   ,   24000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.00244948974278_tau_massiveAndCKM_LO'        ),
    HNLSample(    3.0   ,   8e-06   ,  794.89   ,   22000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.00282842712475_tau_massiveAndCKM_LO'        ),
    HNLSample(    3.0   ,   1e-05   ,  635.91   ,   26000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.00316227766017_tau_massiveAndCKM_LO'        ),
    HNLSample(    3.0   ,   2e-05   ,  317.96   ,   24000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.004472135955_tau_massiveAndCKM_LO'          ),
    HNLSample(    3.0   ,   3e-05   ,  211.97   ,   25000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.00547722557505_tau_massiveAndCKM_LO'        ),
    HNLSample(    3.0   ,   5e-05   ,  127.18   ,   22000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.00707106781187_tau_massiveAndCKM_LO'        ),
    HNLSample(    3.0   ,   7e-05   ,   90.84   ,   20000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.00836660026534_tau_massiveAndCKM_LO'        ),
    HNLSample(    3.0   ,  0.0002   ,   31.80   ,   18000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.0141421356237_tau_massiveAndCKM_LO'         ),
    HNLSample(    3.0   ,  0.0003   ,   21.20   ,   24000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.0173205080757_tau_massiveAndCKM_LO'         ),
    HNLSample(    3.0   ,  0.0001   ,   63.59   ,   24000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-3_V-0.01_tau_massiveAndCKM_LO'                    ),
    HNLSample(    5.0   ,   6e-06   ,   24.49   ,  100000   ,   2.401e-02 , 1.336e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_e_massiveAndCKM_LO'          ),
    HNLSample(    5.0   ,   6e-06   ,   24.61   ,   92000   ,   2.401e-02 , 1.301e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_mu_massiveAndCKM_LO'         ),
    HNLSample(    5.0   ,   6e-06   ,   44.29   ,   60000   ,   2.275e-02 , 1.227e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_tau_massiveAndCKM_LO'        ),
    HNLSample(    5.0   ,   8e-06   ,   18.37   ,  100000   ,   3.180e-02 , 1.723e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00282842712475_e_massiveAndCKM_LO'          ),
    HNLSample(    5.0   ,   8e-06   ,   18.46   ,    1000   ,   3.240e-02 , 1.696e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00282842712475_mu_massiveAndCKM_LO'         ),
    HNLSample(    5.0   ,   1e-05   ,   14.69   ,  100000   ,   3.972e-02 , 2.152e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316227766017_e_massiveAndCKM_LO'          ),
    HNLSample(    5.0   ,   1e-05   ,   14.77   ,   99000   ,   3.929e-02 , 2.186e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316227766017_mu_massiveAndCKM_LO'         ),
    HNLSample(    5.0   ,   2e-05   ,    7.35   ,  100000   ,   7.992e-02 , 4.305e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_e_massiveAndCKM_LO'            ),
    HNLSample(    5.0   ,   2e-05   ,    7.38   ,   74000   ,   8.063e-02 , 4.407e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_mu_massiveAndCKM_LO'           ),
    HNLSample(    5.0   ,   3e-05   ,    4.90   ,  100000   ,   1.185e-01 , 6.418e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_e_massiveAndCKM_LO'          ),
    HNLSample(    5.0   ,   3e-05   ,    4.92   ,   46000   ,   1.186e-01 , 6.420e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_mu_massiveAndCKM_LO'         ),
    HNLSample(    5.0   ,   3e-05   ,    8.86   ,   39000   ,   1.132e-01 , 6.148e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_tau_massiveAndCKM_LO'        ),
    HNLSample(    5.0   ,   5e-05   ,    2.94   ,  100000   ,   1.983e-01 , 1.084e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_e_massiveAndCKM_LO'          ),
    HNLSample(    5.0   ,   5e-05   ,    2.95   ,   93000   ,   2.004e-01 , 1.074e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_mu_massiveAndCKM_LO'         ),
    HNLSample(    5.0   ,   7e-05   ,    2.10   ,  100000   ,   2.792e-01 , 1.504e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_e_massiveAndCKM_LO'          ),
    HNLSample(    5.0   ,   7e-05   ,    2.11   ,  100000   ,   2.798e-01 , 1.507e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_mu_massiveAndCKM_LO'         ),
    HNLSample(    5.0   ,   7e-05   ,    3.80   ,  100000   ,   2.646e-01 , 1.434e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_tau_massiveAndCKM_LO'        ),
    HNLSample(    5.0   ,  0.0001   ,    1.47   ,  100000   ,   4.013e-01 , 2.223e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_e_massiveAndCKM_LO'                      ),
    HNLSample(    5.0   ,  0.0001   ,    1.48   ,   98000   ,   4.066e-01 , 2.129e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_mu_massiveAndCKM_LO'                     ),
    HNLSample(    5.0   ,  0.0001   ,    2.66   ,   78000   ,   3.783e-01 , 2.086e-03 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_tau_massiveAndCKM_LO'                    ),
    HNLSample(    8.0   ,   6e-06   ,    2.08   ,  100000   ,   2.487e-02 , 1.330e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_e_massiveAndCKM_LO'          ),
    HNLSample(    8.0   ,   6e-06   ,    2.09   ,  100000   ,   2.444e-02 , 1.311e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_mu_massiveAndCKM_LO'         ),
    HNLSample(    8.0   ,   6e-06   ,    2.68   ,  100000   ,   2.463e-02 , 1.392e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_tau_massiveAndCKM_LO'        ),
    HNLSample(    8.0   ,   8e-06   ,    1.56   ,  100000   ,   3.314e-02 , 1.772e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_e_massiveAndCKM_LO'          ),
    HNLSample(    8.0   ,   8e-06   ,    1.56   ,  100000   ,   3.286e-02 , 1.766e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_mu_massiveAndCKM_LO'         ),
    HNLSample(    8.0   ,   8e-06   ,    2.01   ,  100000   ,   3.273e-02 , 1.805e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_tau_massiveAndCKM_LO'        ),
    HNLSample(    8.0   ,   1e-05   ,    1.25   ,  100000   ,   4.113e-02 , 2.160e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_e_massiveAndCKM_LO'          ),
    HNLSample(    8.0   ,   1e-05   ,    1.25   ,   98000   ,   4.117e-02 , 2.227e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_mu_massiveAndCKM_LO'         ),
    HNLSample(    8.0   ,   1e-05   ,    1.61   ,  100000   ,   4.149e-02 , 2.244e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_tau_massiveAndCKM_LO'        ),
    HNLSample(    8.0   ,   2e-05   ,    0.62   ,   73000   ,   8.083e-02 , 4.344e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_e_massiveAndCKM_LO'            ),
    HNLSample(    8.0   ,   2e-05   ,    0.63   ,  100000   ,   8.243e-02 , 4.458e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_mu_massiveAndCKM_LO'           ),
    HNLSample(    8.0   ,   2e-05   ,    0.80   ,  100000   ,   8.257e-02 , 4.412e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_tau_massiveAndCKM_LO'          ),
    HNLSample(    8.0   ,   3e-05   ,    0.42   ,   72000   ,   1.238e-01 , 6.620e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_e_massiveAndCKM_LO'          ),
    HNLSample(    8.0   ,   3e-05   ,    0.42   ,  100000   ,   1.240e-01 , 6.705e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_mu_massiveAndCKM_LO'         ),
    HNLSample(    8.0   ,   3e-05   ,    0.54   ,  100000   ,   1.242e-01 , 6.634e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_tau_massiveAndCKM_LO'        ),
    
#############################################################################################    
#############################################################################################    
## NOT RECOMMENDED BY TOM!
#############################################################################################    
#############################################################################################    
#     HNLSample(    2.0   ,   1e-05   , 1943.42   ,   95000   ,   4.205e+00 , 2.507e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-2_V-0.00316227766017_mu_massiveAndCKM_LO'                    ),
#     HNLSample(    2.0   ,   2e-05   ,  971.70   ,   11000   ,   2.976e+00 , 2.003e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_mu_massiveAndCKM_LO'                      ),
#     HNLSample(    2.0   ,  0.0002   ,   97.17   ,   18000   ,   2.471e+00 , 2.277e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-2_V-0.0141421356237_mu_massiveAndCKM_LO'                     ),
#     HNLSample(    2.0   ,  0.0005   ,   38.44   ,    5000   ,   1.263e+00 , 1.485e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_e_massiveAndCKM_LO'                       ),
#     HNLSample(    2.0   ,  0.0005   ,  111.47   ,    1000   ,   1.144e+00 , 1.269e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_tau_massiveAndCKM_LO'                     ),
#     HNLSample(    5.0   ,   5e-05   ,    2.94   ,   42000   ,   1.870e-02 , 8.931e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_e_massiveAndCKM_LO'                     ),
#     HNLSample(    8.0   ,   6e-06   ,    2.08   ,   81000   ,   2.354e-03 , 6.779e-06 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_e_massiveAndCKM_LO'                     ),
#     HNLSample(    8.0   ,   8e-06   ,    1.56   ,   85000   ,   3.135e-03 , 9.564e-06 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_mu_massiveAndCKM_LO'                    ),
#     HNLSample(    8.0   ,   1e-05   ,    1.61   ,   64000   ,   4.207e-03 , 1.102e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_tau_massiveAndCKM_LO'                   ),
#     HNLSample(    8.0   ,   3e-05   ,    0.42   ,   99000   ,   1.363e-02 , 3.123e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_e_massiveAndCKM_LO'                     ),
#     HNLSample(    8.0   ,   3e-05   ,    0.42   ,   82000   ,   1.150e-02 , 3.212e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_mu_massiveAndCKM_LO'                    ),
#     HNLSample(    8.0   ,   3e-05   ,    0.54   ,   58000   ,   1.410e-02 , 3.121e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_tau_massiveAndCKM_LO'                   ),
#     HNLSample(   10.0   ,   6e-06   ,    0.59   ,  181000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.00244948974278_e_onshell_pre2017_NLO'              ),
#     HNLSample(   10.0   ,   6e-06   ,    0.59   ,  165000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.00244948974278_mu_onshell_pre2017_NLO'             ),
#     HNLSample(   10.0   ,   8e-06   ,    0.44   ,  176000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.00282842712475_e_onshell_pre2017_NLO'              ),
#     HNLSample(   10.0   ,   8e-06   ,    0.44   ,  176000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.00282842712475_mu_onshell_pre2017_NLO'             ),
#     HNLSample(   10.0   ,   1e-05   ,    0.35   ,  183000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.00316227766017_e_onshell_pre2017_NLO'              ),
#     HNLSample(   10.0   ,   1e-05   ,    0.35   ,  167000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.00316227766017_mu_onshell_pre2017_NLO'             ),
#     HNLSample(   10.0   ,   2e-05   ,    0.18   ,  170000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.004472135955_e_onshell_pre2017_NLO'                ),
#     HNLSample(   10.0   ,   2e-05   ,    0.18   ,  166000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.004472135955_mu_onshell_pre2017_NLO'               ),
#     HNLSample(   10.0   ,  0.0001   ,    0.04   ,  164000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.01_e_onshell_pre2017_NLO'                          ),
#     HNLSample(   10.0   ,  0.0001   ,    0.04   ,  164000   ,   3.212e+11 , 3.559e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-10_V-0.01_mu_onshell_pre2017_NLO'                         ),
#     HNLSample(    1.0   ,   8e-06   ,44479.30   ,    1000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    1.0   ,   1e-05   ,35584.44   ,    5000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    1.0   ,   2e-05   ,17792.11   ,    2000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    1.0   ,   2e-05   ,17792.11   ,    6000   ,   3.313e+16 , 3.670e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    1.0   ,   3e-05   ,11861.34   ,    6000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    1.0   ,   3e-05   ,11861.34   ,    4000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    1.0   ,   5e-05   , 7116.81   ,    4000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00707106781187_e_onshell_pre2017_NLO'               ),
#     HNLSample(    1.0   ,   5e-05   , 7116.81   ,    8000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00707106781187_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    1.0   ,   7e-05   , 5083.43   ,    3000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00836660026534_e_onshell_pre2017_NLO'               ),
#     HNLSample(    1.0   ,   7e-05   , 5083.43   ,    7000   ,   3.314e+16 , 3.613e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.00836660026534_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    1.0   ,    0.36   ,    1.00   ,  364000   ,   3.314e+16 , 3.633e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.59587618054_e_onshell_pre2017_NLO'                  ),
#     HNLSample(    1.0   ,    0.36   ,    1.00   ,  386000   ,   3.314e+16 , 3.633e+13 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-1_V-0.59587618054_mu_onshell_pre2017_NLO'                 ),
#     HNLSample(    2.1   ,   6e-06   , 1449.13   ,   13000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00244948974278_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,   6e-06   , 1449.13   ,   13000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00244948974278_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.1   ,   8e-06   , 1086.85   ,    9000   ,   8.090e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00282842712475_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,   8e-06   , 1086.85   ,   11000   ,   8.090e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00282842712475_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.1   ,   1e-05   ,  869.48   ,    9000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00316227766017_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,   1e-05   ,  869.48   ,   11000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00316227766017_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.1   ,   2e-05   ,  434.73   ,   10000   ,   8.090e+14 , 8.840e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.004472135955_e_onshell_pre2017_NLO'               ),
#     HNLSample(    2.1   ,   2e-05   ,  434.73   ,   10000   ,   8.090e+14 , 8.840e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.004472135955_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    2.1   ,   3e-05   ,  289.83   ,   12000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00547722557505_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,   3e-05   ,  289.83   ,   10000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00547722557505_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.1   ,   5e-05   ,  173.90   ,   11000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00707106781187_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,   5e-05   ,  173.90   ,   13000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00707106781187_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.1   ,   7e-05   ,  124.21   ,   33000   ,   8.090e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00836660026534_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,   7e-05   ,  124.21   ,   29000   ,   8.090e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.00836660026534_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.1   ,  0.0002   ,   43.47   ,   41000   ,   8.090e+14 , 8.840e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.0141421356237_e_onshell_pre2017_NLO'              ),
#     HNLSample(    2.1   ,  0.0002   ,   43.47   ,   44000   ,   8.090e+14 , 8.840e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.0141421356237_mu_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,  0.0003   ,   28.98   ,   52000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.0173205080757_e_onshell_pre2017_NLO'              ),
#     HNLSample(    2.1   ,  0.0003   ,   28.98   ,   53000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.0173205080757_mu_onshell_pre2017_NLO'             ),
#     HNLSample(    2.1   ,  0.0001   ,   86.95   ,    7000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.01_e_onshell_pre2017_NLO'                         ),
#     HNLSample(    2.1   ,  0.0001   ,   86.95   ,   10000   ,   8.091e+14 , 8.841e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.1_V-0.01_mu_onshell_pre2017_NLO'                        ),
#     HNLSample(    2.5   ,   2e-05   ,  182.26   ,  214000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.004472135955_e_onshell_pre2017_NLO'               ),
#     HNLSample(    2.5   ,   2e-05   ,  182.26   ,  218000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.004472135955_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    2.5   ,   3e-05   ,  121.51   ,  225000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.00547722557505_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.5   ,   3e-05   ,  121.51   ,  230000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.00547722557505_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.5   ,   5e-05   ,   72.91   ,  246000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.00707106781187_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.5   ,   5e-05   ,   72.91   ,  247000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.00707106781187_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.5   ,   7e-05   ,   52.08   ,  250000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.00836660026534_e_onshell_pre2017_NLO'             ),
#     HNLSample(    2.5   ,   7e-05   ,   52.08   ,  250000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.00836660026534_mu_onshell_pre2017_NLO'            ),
#     HNLSample(    2.5   ,  0.0002   ,   18.23   ,  250000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.0141421356237_e_onshell_pre2017_NLO'              ),
#     HNLSample(    2.5   ,  0.0002   ,   18.23   ,  249000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.0141421356237_mu_onshell_pre2017_NLO'             ),
#     HNLSample(    2.5   ,  0.0003   ,   12.15   ,  249000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.0173205080757_e_onshell_pre2017_NLO'              ),
#     HNLSample(    2.5   ,  0.0003   ,   12.15   ,  250000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.0173205080757_mu_onshell_pre2017_NLO'             ),
#     HNLSample(    2.5   ,  0.0001   ,   36.45   ,  248000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.01_e_onshell_pre2017_NLO'                         ),
#     HNLSample(    2.5   ,  0.0001   ,   36.45   ,  250000   ,   3.392e+14 , 3.717e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2.5_V-0.01_mu_onshell_pre2017_NLO'                        ),
#     HNLSample(    2.0   ,   6e-06   , 1853.47   ,    8000   ,   1.035e+15 , 1.121e+12 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    2.0   ,   6e-06   , 1853.47   ,  124000   ,   1.035e+15 , 1.121e+12 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    2.0   ,  0.0001   ,  111.21   ,  245000   ,   1.035e+15 , 1.121e+12 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_e_onshell_pre2017_NLO'                           ),
#     HNLSample(    2.0   ,  0.0001   ,  111.21   ,  242000   ,   1.035e+15 , 1.121e+12 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_mu_onshell_pre2017_NLO'                          ),
#     HNLSample(    3.0   ,   6e-06   ,  243.87   ,  244000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,   6e-06   ,  243.87   ,  247000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    3.0   ,   8e-06   ,  182.90   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,   8e-06   ,  182.90   ,  246000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    3.0   ,   1e-05   ,  146.32   ,  249000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,   1e-05   ,  146.32   ,  249000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    3.0   ,   2e-05   ,   73.16   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    3.0   ,   2e-05   ,   73.16   ,  249000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    3.0   ,   3e-05   ,   48.77   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,   3e-05   ,   48.77   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    3.0   ,   5e-05   ,   29.26   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00707106781187_e_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,   5e-05   ,   29.26   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00707106781187_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    3.0   ,   7e-05   ,   20.90   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00836660026534_e_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,   7e-05   ,   20.90   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.00836660026534_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    3.0   ,  0.0002   ,    7.32   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.0141421356237_mu_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,  0.0003   ,    4.88   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.0173205080757_e_onshell_pre2017_NLO'                ),
#     HNLSample(    3.0   ,  0.0003   ,    4.88   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.0173205080757_mu_onshell_pre2017_NLO'               ),
#     HNLSample(    3.0   ,  0.0001   ,   14.63   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.01_e_onshell_pre2017_NLO'                           ),
#     HNLSample(    3.0   ,  0.0001   ,   14.63   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.01_mu_onshell_pre2017_NLO'                          ),
#     HNLSample(    3.0   ,  0.0015   ,    1.00   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.03823254899_e_onshell_pre2017_NLO'                  ),
#     HNLSample(    3.0   ,  0.0015   ,    1.00   ,  250000   ,   1.361e+14 , 1.484e+11 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-3_V-0.03823254899_mu_onshell_pre2017_NLO'                 ),
#     HNLSample(    4.0   ,   6e-06   ,   57.83   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   ,   6e-06   ,   57.83   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,   8e-06   ,   43.37   ,  250000   ,   3.221e+13 , 3.495e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   ,   8e-06   ,   43.37   ,  250000   ,   3.221e+13 , 3.495e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,   1e-05   ,   34.70   ,  250000   ,   3.221e+13 , 3.495e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   ,   1e-05   ,   34.70   ,  250000   ,   3.221e+13 , 3.495e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,   2e-05   ,   17.35   ,  250000   ,   3.221e+13 , 3.495e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    4.0   ,   2e-05   ,   17.35   ,  250000   ,   3.221e+13 , 3.495e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    4.0   ,   3e-05   ,   11.57   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   ,   3e-05   ,   11.57   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,   5e-05   ,    6.94   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00707106781187_e_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   ,   5e-05   ,    6.94   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00707106781187_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,   7e-05   ,    2.47   ,  200000   ,   3.213e+13 , 3.469e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00836660026534_2l_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,   7e-05   ,    4.96   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00836660026534_e_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   ,   7e-05   ,    4.96   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.00836660026534_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    4.0   ,  0.0002   ,    1.73   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.0141421356237_e_onshell_pre2017_NLO'                ),
#     HNLSample(    4.0   ,  0.0002   ,    1.73   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.0141421356237_mu_onshell_pre2017_NLO'               ),
#     HNLSample(    4.0   , 0.00035   ,    1.00   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.01860689426_e_onshell_pre2017_NLO'                  ),
#     HNLSample(    4.0   , 0.00035   ,    1.00   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.01860689426_mu_onshell_pre2017_NLO'                 ),
#     HNLSample(    4.0   ,  0.0001   ,    3.47   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.01_e_onshell_pre2017_NLO'                           ),
#     HNLSample(    4.0   ,  0.0001   ,    3.47   ,  250000   ,   3.221e+13 , 3.496e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-4_V-0.01_mu_onshell_pre2017_NLO'                          ),
#     HNLSample(    5.0   ,   6e-06   ,   18.94   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    5.0   ,   6e-06   ,   18.94   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    5.0   ,   8e-06   ,   14.20   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    5.0   ,   8e-06   ,   14.20   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    5.0   ,   1e-05   ,   11.36   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    5.0   ,   1e-05   ,   11.36   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    5.0   ,   2e-05   ,    5.68   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    5.0   ,   2e-05   ,    5.68   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    5.0   ,   3e-05   ,    3.79   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    5.0   ,   3e-05   ,    3.79   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    5.0   ,   5e-05   ,    2.27   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_e_onshell_pre2017_NLO'               ),
#     HNLSample(    5.0   ,   5e-05   ,    2.27   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00707106781187_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    5.0   ,   7e-05   ,    1.62   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_e_onshell_pre2017_NLO'               ),
#     HNLSample(    5.0   ,   7e-05   ,    1.62   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    5.0   , 0.00011   ,    1.00   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.01065503443_e_onshell_pre2017_NLO'                  ),
#     HNLSample(    5.0   , 0.00011   ,    1.00   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.01065503443_mu_onshell_pre2017_NLO'                 ),
#     HNLSample(    5.0   ,  0.0001   ,    1.14   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_e_onshell_pre2017_NLO'                           ),
#     HNLSample(    5.0   ,  0.0001   ,    1.14   ,  250000   ,   1.052e+13 , 1.137e+10 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-5_V-0.01_mu_onshell_pre2017_NLO'                          ),
#     HNLSample(    6.0   , 2.2e-06   ,   20.85   ,  248000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.001479_e_onshell_pre2017_NLO'                       ),
#     HNLSample(    6.0   , 2.2e-06   ,   20.85   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.001479_mu_onshell_pre2017_NLO'                      ),
#     HNLSample(    6.0   ,   6e-06   ,    7.60   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    6.0   ,   6e-06   ,    7.60   ,  249000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    6.0   ,   8e-06   ,    5.70   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    6.0   ,   8e-06   ,    5.70   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    6.0   ,   1e-05   ,    4.56   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    6.0   ,   1e-05   ,    4.56   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    6.0   ,   2e-05   ,    2.28   ,  249000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    6.0   ,   2e-05   ,    2.28   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    6.0   ,   3e-05   ,    1.52   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    6.0   ,   3e-05   ,    1.52   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    6.0   , 4.6e-05   ,    1.00   ,  427000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00675244664_e_onshell_pre2017_NLO'                  ),
#     HNLSample(    6.0   , 4.6e-05   ,    1.00   ,  441000   ,   1.185e-01 , 1.274e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00675244664_e_pre2017_NLO'                          ),
#     HNLSample(    6.0   , 4.6e-05   ,    1.00   ,  415000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00675244664_mu_onshell_pre2017_NLO'                 ),
#     HNLSample(    6.0   , 4.6e-05   ,    1.00   ,  416000   ,   1.171e-01 , 1.259e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00675244664_mu_pre2017_NLO'                         ),
#     HNLSample(    6.0   ,   5e-05   ,    0.91   ,  249000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00707106781187_e_onshell_pre2017_NLO'               ),
#     HNLSample(    6.0   ,   5e-05   ,    0.91   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00707106781187_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    6.0   ,   7e-05   ,    0.65   ,  250000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00836660026534_e_onshell_pre2017_NLO'               ),
#     HNLSample(    6.0   ,   7e-05   ,    0.65   ,  249000   ,   4.212e+12 , 4.527e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-6_V-0.00836660026534_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    7.0   , 4.7e-06   ,    4.46   ,  236000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.002174_e_onshell_pre2017_NLO'                       ),
#     HNLSample(    7.0   , 5.3e-06   ,    4.00   ,  223000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.002296_mu_onshell_pre2017_NLO'                      ),
#     HNLSample(    7.0   ,   6e-06   ,    3.52   ,  245000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    7.0   ,   6e-06   ,    3.52   ,  250000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    7.0   ,   8e-06   ,    2.64   ,  244000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    7.0   ,   8e-06   ,    2.64   ,  244000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    7.0   ,   1e-05   ,    2.11   ,  248000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    7.0   ,   1e-05   ,    2.11   ,  250000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    7.0   ,   2e-05   ,    1.05   ,  249000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    7.0   ,   2e-05   ,    1.05   ,  248000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    7.0   , 2.1e-05   ,    1.00   ,  416000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00459211224_e_onshell_pre2017_NLO'                  ),
#     HNLSample(    7.0   , 2.1e-05   ,    1.00   ,  218000   ,   5.449e-02 , 5.797e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00459211224_e_pre2017_NLO'                          ),
#     HNLSample(    7.0   , 2.1e-05   ,    1.00   ,  421000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00459211224_mu_onshell_pre2017_NLO'                 ),
#     HNLSample(    7.0   , 2.1e-05   ,    1.00   ,  213000   ,   5.473e-02 , 5.822e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00459211224_mu_pre2017_NLO'                         ),
#     HNLSample(    7.0   ,   3e-05   ,    0.70   ,  246000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    7.0   ,   3e-05   ,    0.70   ,  249000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    7.0   ,   5e-05   ,    0.42   ,  244000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00707106781187_e_onshell_pre2017_NLO'               ),
#     HNLSample(    7.0   ,   5e-05   ,    0.42   ,  248000   ,   1.941e+12 , 2.065e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-7_V-0.00707106781187_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    8.0   ,   6e-06   ,    1.80   ,  250000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    8.0   ,   6e-06   ,    1.80   ,  247000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    8.0   ,   8e-06   ,    1.35   ,  240000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    8.0   ,   8e-06   ,    1.35   ,  244000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    8.0   ,   1e-05   ,    1.08   ,  247000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    8.0   ,   1e-05   ,    1.08   ,  247000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    8.0   ,   2e-05   ,    0.54   ,  247000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    8.0   ,   2e-05   ,    0.54   ,  247000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    8.0   ,   3e-05   ,    0.36   ,  243000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_e_onshell_pre2017_NLO'               ),
#     HNLSample(    8.0   ,   3e-05   ,    0.36   ,  249000   ,   9.910e+11 , 1.070e+09 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    9.0   ,   6e-06   ,    1.00   ,  150000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.00244948974278_e_onshell_pre2017_NLO'               ),
#     HNLSample(    9.0   ,   6e-06   ,    1.00   ,  122000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.00244948974278_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    9.0   ,   8e-06   ,    0.75   ,  117000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.00282842712475_e_onshell_pre2017_NLO'               ),
#     HNLSample(    9.0   ,   8e-06   ,    0.75   ,  116000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.00282842712475_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    9.0   ,   1e-05   ,    0.60   ,  162000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.00316227766017_e_onshell_pre2017_NLO'               ),
#     HNLSample(    9.0   ,   1e-05   ,    0.60   ,  224000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.00316227766017_mu_onshell_pre2017_NLO'              ),
#     HNLSample(    9.0   ,   2e-05   ,    0.30   ,  167000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.004472135955_e_onshell_pre2017_NLO'                 ),
#     HNLSample(    9.0   ,   2e-05   ,    0.30   ,  242000   ,   5.471e+11 , 5.919e+08 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_trilepton_M-9_V-0.004472135955_mu_onshell_pre2017_NLO'                ),
#     HNLSample(    2.0   ,   6e-06   , 3239.05   ,   21000   ,   3.647e+00 , 2.257e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.00244948974278_mu_massiveAndCKM_LO'            ),
#     HNLSample(    2.0   ,   2e-05   ,  960.89   ,   45000   ,   3.163e+00 , 2.429e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_e_massiveAndCKM_LO'               ),
#     HNLSample(    2.0   ,   2e-05   , 2786.85   ,   49000   ,   7.591e+00 , 5.579e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.004472135955_tau_massiveAndCKM_LO'             ),
#     HNLSample(    2.0   ,  0.0003   ,  185.79   ,   39000   ,   3.871e+00 , 4.233e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.0173205080757_tau_massiveAndCKM_LO'            ),
#     HNLSample(    2.0   ,  0.0005   ,   38.44   ,    6000   ,   1.375e+00 , 1.715e-02 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-2_V-0.022360679775_e_massiveAndCKM_LO'               ),
#     HNLSample(    5.0   ,   2e-05   ,    7.35   ,    6000   ,   9.590e-03 , 6.733e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.004472135955_e_massiveAndCKM_LO'               ),
#     HNLSample(    5.0   ,   7e-05   ,    2.10   ,  104000   ,   2.778e-02 , 1.049e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_e_massiveAndCKM_LO'             ),
#     HNLSample(    5.0   ,   7e-05   ,    2.11   ,  103000   ,   2.701e-02 , 1.005e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_mu_massiveAndCKM_LO'            ),
#     HNLSample(    5.0   ,   7e-05   ,    3.80   ,   72000   ,   2.979e-02 , 1.635e-04 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-5_V-0.00836660026534_tau_massiveAndCKM_LO'           ),
#     HNLSample(    8.0   ,   6e-06   ,    2.08   ,   76000   ,   2.794e-03 , 7.878e-06 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00244948974278_e_massiveAndCKM_LO'             ),
#     HNLSample(    8.0   ,   8e-06   ,    1.56   ,   62000   ,   3.095e-03 , 8.102e-06 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00282842712475_mu_massiveAndCKM_LO'            ),
#     HNLSample(    8.0   ,   1e-05   ,    1.25   ,   60000   ,   4.328e-03 , 1.120e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_e_massiveAndCKM_LO'             ),
#     HNLSample(    8.0   ,   1e-05   ,    1.25   ,   60000   ,   3.845e-03 , 1.284e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_mu_massiveAndCKM_LO'            ),
#     HNLSample(    8.0   ,   1e-05   ,    1.61   ,   58000   ,   4.173e-03 , 1.072e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316227766017_tau_massiveAndCKM_LO'           ),
#     HNLSample(    8.0   ,   2e-05   ,    0.80   ,   37000   ,   8.399e-03 , 1.784e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.004472135955_tau_massiveAndCKM_LO'             ),
#     HNLSample(    8.0   ,   3e-05   ,    0.42   ,   59000   ,   1.152e-02 , 2.414e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_e_massiveAndCKM_LO'             ),
#     HNLSample(    8.0   ,   3e-05   ,    0.42   ,  243000   ,   1.401e-02 , 3.217e-05 , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_2018/displaced/HeavyNeutrino_trilepton_M-8_V-0.00547722557505_mu_massiveAndCKM_LO'            ),
#     HNLSample(   10.0   , 3.5e-06   ,    1.00   ,  520000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-10_V-0.00188259708_e_NLO'                                           ),
#     HNLSample(   10.0   , 3.5e-06   ,    1.00   ,  133000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-10_V-0.00188259708_mu_NLO'                                          ),
#     HNLSample(   11.0   , 2.2e-06   ,    0.99   ,  396000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-11_V-0.00148345941_e_NLO'                                           ),
#     HNLSample(   11.0   , 2.2e-06   ,    0.99   ,  365000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-11_V-0.00148345941_mu_NLO'                                          ),
#     HNLSample(   12.0   , 1.4e-06   ,    0.99   ,  531000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-12_V-0.0011934501_e_NLO'                                            ),
#     HNLSample(   12.0   , 1.4e-06   ,    0.99   ,  239000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-12_V-0.0011934501_mu_NLO'                                           ),
#     HNLSample(    1.0   ,  0.0001   , 1775.34   ,  146000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.01_2l_NLO'                                                    ),
#     HNLSample(    1.0   ,   0.013   ,   26.82   ,  567000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.11505_mu_NLO'                                                 ),
#     HNLSample(    1.0   ,   0.013   ,   26.57   ,  775000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.11557_e_NLO'                                                  ),
#     HNLSample(    1.0   ,    0.15   ,    2.37   ,  150000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.3872_e_NLO'                                                   ),
#     HNLSample(    1.0   ,    0.15   ,    2.37   ,  157000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.3872_mu_NLO'                                                  ),
#     HNLSample(    1.0   ,    0.25   ,    0.71   ,  149000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.5_2l_NLO'                                                     ),
#     HNLSample(    1.0   ,    0.25   ,    1.42   ,  362000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.5_e_NLO'                                                      ),
#     HNLSample(    1.0   ,    0.25   ,    1.42   ,  366000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-1_V-0.5_mu_NLO'                                                     ),
#     HNLSample(    2.0   ,  0.0001   ,   55.60   ,  146000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-2_V-0.01_2l_NLO'                                                    ),
#     HNLSample(    2.0   ,   0.005   ,    2.22   ,  524000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-2_V-0.07071_e_NLO'                                                  ),
#     HNLSample(    2.0   ,   0.005   ,    2.22   ,  426000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-2_V-0.07071_mu_NLO'                                                 ),
#     HNLSample(    3.0   ,  0.0001   ,    7.31   ,  145000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-3_V-0.01_2l_NLO'                                                    ),
#     HNLSample(    3.0   ,  0.0006   ,    2.44   ,  535000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-3_V-0.0245_e_NLO'                                                   ),
#     HNLSample(    3.0   ,  0.0006   ,    2.44   ,  478000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-3_V-0.0245_mu_NLO'                                                  ),
#     HNLSample(    4.0   , 0.00015   ,    2.31   ,  501000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-4_V-0.01225_e_NLO'                                                  ),
#     HNLSample(    4.0   , 0.00015   ,    2.31   ,  491000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-4_V-0.01225_mu_NLO'                                                 ),
#     HNLSample(    4.0   ,  0.0001   ,    1.73   ,  149000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-4_V-0.01_2l_NLO'                                                    ),
#     HNLSample(    5.5   ,   1e-05   ,    3.53   ,   49000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-5.5_V-0.00316_2l_NLO'                                               ),
#     HNLSample(    5.0   ,   1e-05   ,    5.69   ,  239000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316_2l_NLO'                                                 ),
#     HNLSample(    5.0   ,   1e-05   ,   11.37   ,  133000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316_e_NLO'                                                  ),
#     HNLSample(    5.0   ,   1e-05   ,   11.37   ,  155000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-5_V-0.00316_mu_NLO'                                                 ),
#     HNLSample(    5.0   , 0.00012   ,    0.92   ,  687000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-5_V-0.0111_e_NLO'                                                   ),
#     HNLSample(    5.0   , 0.00012   ,    0.92   ,  360000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-5_V-0.0111_mu_NLO'                                                  ),
#     HNLSample(    6.0   ,   1e-05   ,    2.28   ,   50000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-6_V-0.00316_2l_NLO'                                                 ),
#     HNLSample(    6.0   ,   1e-05   ,    4.56   ,  198000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-6_V-0.00316_e_NLO'                                                  ),
#     HNLSample(    6.0   ,   1e-05   ,    4.56   ,  199000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-6_V-0.00316_mu_NLO'                                                 ),
#     HNLSample(    6.0   , 4.6e-05   ,    1.00   ,  400000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-6_V-0.00675244664_e_NLO'                                            ),
#     HNLSample(    6.0   , 4.6e-05   ,    1.00   ,  358000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-6_V-0.00675244664_mu_NLO'                                           ),
#     HNLSample(    7.0   ,   1e-05   ,    1.06   ,   50000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-7_V-0.00316_2l_NLO'                                                 ),
#     HNLSample(    7.0   ,   1e-05   ,    2.11   ,  179000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-7_V-0.00316_e_NLO'                                                  ),
#     HNLSample(    7.0   ,   1e-05   ,    2.11   ,  244000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-7_V-0.00316_mu_NLO'                                                 ),
#     HNLSample(    7.0   , 2.1e-05   ,    1.00   ,  465000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-7_V-0.00459211224_e_NLO'                                            ),
#     HNLSample(    7.0   , 2.1e-05   ,    1.00   ,  416000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-7_V-0.00459211224_mu_NLO'                                           ),
#     HNLSample(    8.0   ,   1e-05   ,    0.54   ,   49000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-8_V-0.00316_2l_NLO'                                                 ),
#     HNLSample(    8.0   , 1.1e-05   ,    1.00   ,  525000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-8_V-0.00328876176_e_NLO'                                            ),
#     HNLSample(    8.0   , 1.1e-05   ,    1.00   ,  452000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-8_V-0.00328876176_mu_NLO'                                           ),
#     HNLSample(    9.0   ,   6e-06   ,    1.00   ,  509000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-9_V-0.00244991552_e_NLO'                                            ),
#     HNLSample(    9.0   ,   6e-06   ,    1.00   ,  457000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-9_V-0.00244991552_mu_NLO'                                           ),
#     HNLSample(    9.0   ,   1e-05   ,    0.30   ,   50000   ,        -99. ,      -99. , '/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/displaced/HeavyNeutrino_trilepton_M-9_V-0.00316_2l_NLO'                                                 ),
]

samplesdict = OrderedDict()

with open('heavyNeutrinoFileList.txt') as ff:
# with open('test.txt') as ff:
    content = ff.readlines()

current_key = ''
for ii, line in enumerate(content):
    line = line.rstrip()
    if line.startswith('/pnfs/iihe/cms/'):
        current_key = line.replace(':','')
    if current_key not in samplesdict.keys():
        samplesdict[current_key] = []
    elif line.startswith('heavyNeutrino'):
        samplesdict[current_key].append(line)
    else:
        pass
#         print 'finished with', current_key
#     import pdb; pdb.set_trace()

print '\n\n\n\n\n'

# toread = toread[:3]

for sample in toread:
    if sample.path not in samplesdict.keys():
#         print sample.path, 'missing'
        continue
    sample.files = samplesdict[sample.path]
    sample._prependPath()




for sample in toread:
    print "{0:50} = creator.makeMCComponentFromLocal({1:50}, 'XXX', path=os.environ['CMSSW_BASE']+'/src/CMGTools/HNL/python/samples', pattern='.*dummy')".format(sample.title, "'"+sample.title+"'")

print '\n\n'

for sample in toread:
    print sample.title + '.files = ['
    for ii in sample.files:
        print "    {0:200},".format("'"+ii+"'")
    print ']'

print '\n\n'

for sample in toread:
    print "{0:50}.ctau = {1:10} ; {2:50}.v2 = {3:10} ; {4:50}.mass = {5:10} ; {6:50}.nGenEvents = {7:10} ; {6:50}.xs = {8:10} ; {6:50}.xse = {9:10}".format(sample.title, sample.ctau, sample.title, sample.v2, sample.title, sample.mass, sample.title, sample.nevents, sample.xs, sample.xse)





