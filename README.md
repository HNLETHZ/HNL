#install HNL software (25/4/19)


cmsrel CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv

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


git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git  -f  -t heppy_94X_dev
git remote add vstampf git@github.com:vinzenzstampf/cmg-cmssw.git -f -t hnl
git checkout -b hnl vstampf/hnl
git checkout -b heppy_94X_dev cmg-central/heppy_94X_dev

git cms-addpkg /EgammaAnalysis/ElectronTools/
git cms-addpkg /PhysicsTools/
git cms-addpkg /RecoEgamma/EgammaTools/
git cms-addpkg /RecoEgamma/ElectronIdentification/
git cms-addpkg /RecoEgamma/PhotonIdentification/
git cms-addpkg /RecoTauTag/RecoTau/


# now get the CMGTools subsystem from the cmgtools-lite repository
git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 94X_dev CMGTools
# add your fork
git remote add vstampf https://github.com/vinzenzstampf/cmgtools-lite.git -f -t 94X_HNL
git checkout -b 94X_HNL vstampf/94X_HNL
git checkout 94X_dev
# update certain files from other branches (conflict for CRAB)
git checkout 94X_HNL H2TauTau/python/proto/physicsobjects/BTagSF.py

cd CMGTools
#add HNL
#git remote add david https://github.com/dehuazhu/HNL.git 
#git remote add riccardo https://github.com/rmanzoni/HNL.git 
#git remote add vince https://github.com/vinzenzstampf/HNL.git
git remote add ethz  https://github.com/HNLETHZ/HNL.git
git clone -o ethz https://github.com/HNLETHZ/HNL.git -b master HNL


# update certain files from other branches
cd ../..
git checkout hnl PhysicsTools/Heppy/python/analyzers/core/PileUpAnalyzer.py
git checkout hnl PhysicsTools/Heppy/python/physicsobjects/Electron.py
git checkout hnl PhysicsTools/Heppy/python/physicsobjects/Muon.py
git checkout hnl PhysicsTools/Heppy/python/physicsobjects/Lepton.py

cd ../../..
scram b -j 8

cd src
scram b -j 8

cd CMGTools
scram b -j 8

cd HNL
scram b -j 8

# there might be some errors with some ML packages, just remove them not needed:
rm -r $CMSSW_BASE/src/PhysicsTools/MXNet/
rm $CMSSW_BASE/src/PhysicsTools/PythonAnalysis/test/test_PyMVA.cpp
