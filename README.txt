###########
 ### 2018 ###
###########

cmsrel CMSSW_10_4_0_patch1
cd CMSSW_10_4_0_patch1/src
cmsenv

git config --global user.github vinzenzstampf
git config --global user.name 'cesare borgia'
git config --global user.email 'prinzvinz@gmx.at'

git cms-init

vim .git/info/sparse-checkout
#replace everything by

/.clang-format
/.clang-tidy
/.gitignore
/EgammaAnalysis/ElectronTools/
/PhysicsTools/
/RecoEgamma/EgammaTools/
/RecoEgamma/ElectronIdentification/
/RecoEgamma/PhotonIdentification/
/RecoTauTag/RecoTau/


git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git  -f  -t heppy_104X_dev
git remote add vstampf https://github.com/vinzenzstampf/cmg-cmssw.git -f -t hnl_104X
git checkout -b hnl_104X vstampf/hnl_104X
git checkout -b heppy_104X_dev cmg-central/heppy_104X_dev

git cms-addpkg /EgammaAnalysis/ElectronTools/
git cms-addpkg /PhysicsTools/
git cms-addpkg /RecoEgamma/EgammaTools/
git cms-addpkg /RecoEgamma/ElectronIdentification/
git cms-addpkg /RecoEgamma/PhotonIdentification/
git cms-addpkg /RecoTauTag/RecoTau/


# now get the CMGTools subsystem from the cmgtools-lite repository
git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 104X_dev CMGTools
cd CMGTools

# add your fork
git remote add vstampf https://github.com/vinzenzstampf/cmgtools-lite.git -f -t 104X_HNL
git checkout -b 104X_HNL vstampf/104X_HNL
git checkout 104X_dev

# update certain files from other branches
# git checkout 104X_HNL H2TauTau/python/proto/physicsobjects/BTagSF.py

# add HNL
git remote add HNL https://github.com/HNLETHZ/HNL.git 
git clone -o HNL https://github.com/HNLETHZ/HNL.git -b HNL_18 HNL
cd HNL
cp /afs/cern.ch/work/d/dwinterb/public/MSSM2016/tagging_efficiencies_Moriond2017.root data/.

# update certain files from other branches
cd ../..
#git checkout hnl_102X PhysicsTools/Heppy/python/analyzers/core/PileUpAnalyzer.py
git checkout hnl_104X PhysicsTools/Heppy/python/physicsobjects/Electron.py
git checkout hnl_104X PhysicsTools/Heppy/python/physicsobjects/Muon.py
git checkout hnl_104X PhysicsTools/Heppy/python/physicsobjects/Lepton.py


cd ..
scram b -j 8

cd src
scram b -j 8

cd CMGTools
scram b -j 8

cd HNL
scram b -j 8
