import os
from glob import glob
# from CMGTools.HNL.samples.signal import HN3L_M_2p5_V_0p0173205080757_e_onshell, HN3L_M_2p5_V_0p00707106781187_e_onshell
# from CMGTools.HNL.samples.signal import HN3L_M_2_V_0p00282842712475_e_massiveAndCKM_LO     
# from CMGTools.HNL.samples.signal import HN3L_M_2_V_0p00836660026534_e_massiveAndCKM_LO
from CMGTools.HNL.samples.signal import HN3L_M_2_V_0p00244948974278_e_massiveAndCKM_LO
from CMGTools.HNL.samples.samples_data_2017_noskim import Single_mu_2017B

# HN3L_M_2p5_V_0p0173205080757_e_onshell .files = glob('/eos/user/d/dezhu/HNL/miniAOD/20180710_miniAOD/heavyNeutrino*.root')
# HN3L_M_2_V_0p00282842712475_e_massiveAndCKM_LO.files = glob('/eos/user/d/dezhu/HNL/miniAOD/20180710_miniAOD/heavyNeutrino_99.root')
# HN3L_M_2_V_0p00836660026534_e_massiveAndCKM_LO.files = glob('/afs/cern.ch/work/d/dezhu/HNL/CMSSW_9_4_6_patch1/src/CMGTools/HNL/test/HN3L_M_2_V_0p00836660026534_e.root')
# N3L_M_2_V_0p00282842712475_e_massiveAndCKM_LO.files = glob('/eos/user/d/dezhu/HNL/miniAOD/20180710_miniAOD/heavyNeutrino_99.root')
# HN3L_M_2p5_V_0p00707106781187_e_onshell.files = glob('/eos/user/v/vstampf/miniaod/HN3L_M2p5_V0p007_eos_pre2017_NLO/heavyNeutrino*.root')
# TTJets_amcat.files = glob('/eos/user/v/vstampf/miniaod/TTJets_amcat/miniAOD_skim*.root')

Single_mu_2017B.files = glob('/work/dezhu/1_MiniAODs/Single_mu_2017B/54F30BE9-423C-E811-A315-0CC47A7C3410.root')
HN3L_M_2_V_0p00244948974278_e_massiveAndCKM_LO.files = glob ('/work/dezhu/1_MiniAODs/HN3L_M_2_V_0p00244948974278_e_massiveAndCKM_LO.root')
HN3L_M_2_V_0p00244948974278_e_massiveAndCKM_LO.files = glob ('/work/dezhu/1_MiniAODs/HN3L_M_2_V_0p00244948974278_e_massiveAndCKM_LO.root')
