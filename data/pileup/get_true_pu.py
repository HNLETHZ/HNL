import ROOT
import numpy as np
from DataFormats.FWLite import Events, Handle
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
from PhysicsTools.Heppy.physicsutils.PileUpSummaryInfo import PileUpSummaryInfo
from pdb import set_trace

ROOT.gROOT.SetBatch()        # don't pop up canvases

creator = ComponentCreator()

TTJets_amcat = creator.makeMCComponent(
    name    = 'TTJets_amcat', 
    dataset = '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 831.76, 
    useAAA  = True
)

ZZZ = creator.makeMCComponent(
    name    = 'ZZZ', 
    dataset = '/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.01398, 
    useAAA  = True
)

WZZ = creator.makeMCComponent(
    name    = 'WZZ', 
    dataset = '/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.05565, 
    useAAA  = True
)

WWZ = creator.makeMCComponent(
    name    = 'WWZ', 
    dataset = '/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.1651, 
    useAAA  = True
)

WWW = creator.makeMCComponent(
    name    = 'WWW', 
    dataset = '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.2086, 
    useAAA  = True
)

WWTo2L2Nu = creator.makeMCComponent(
    name    = 'WWTo2L2Nu', 
    dataset = '/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.1729, 
    useAAA  = True
)

WGGJets = creator.makeMCComponent(
    name    = 'WGGJets', 
    dataset = '/WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.03711, 
    useAAA  = True
)

TTWJetsToLNu = creator.makeMCComponent(
    name    = 'TTWJetsToLNu', 
    dataset = '/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.2043, 
    useAAA  = True
)

TTZToLLNuNu = creator.makeMCComponent(
    name    = 'TTZToLLNuNu', 
    dataset = '/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.2529, 
    useAAA  = True
)

TTZToLL = creator.makeMCComponent(
    name    = 'TTZToLL', 
    dataset = '/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    # xSec    = #FIXME 
    useAAA  = True
)

ST_s_channel_4f_leptonDecays = creator.makeMCComponent(
    name    = 'ST_s-channel_4f_leptonDecyas', 
    dataset = '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 3.68, 
    useAAA  = True
)

ST_t_channel_antitop_4f_inclusiveDecays = creator.makeMCComponent(
    name    = 'ST_t-channel_antitop_4f_inclusiveDecays', 
    dataset = '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 26.23, 
    useAAA  = True
)

ST_t_channel_top_4f_inclusiveDecays = creator.makeMCComponent(
    name    = 'ST_t-channel_top_4f_inclusiveDecays', 
    dataset = '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 44.07, 
    useAAA  = True
)

ST_tW_antitop_5f_inclusiveDecays = creator.makeMCComponent(
    name    = 'ST_tW_antitop_5f_inclusiveDecays', 
    dataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 35.6, 
    useAAA  = True
)

ST_tW_top_5f_inclusiveDecays = creator.makeMCComponent(
    name    = 'ST_tW_top_5f_inclusiveDecays', 
    dataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 35.6, 
    useAAA  = True
)

samples =  [
            ZZZ, 
            WZZ, 
            WWZ, 
            WWW, 
            WWTo2L2Nu, 
            WGGJets, 
            TTWJetsToLNu, 
            TTZToLLNuNu, 
            TTZToLL, 
            ST_s_channel_4f_leptonDecays, 
            ST_t_channel_antitop_4f_inclusiveDecays, 
            ST_t_channel_top_4f_inclusiveDecays, 
            ST_tW_antitop_5f_inclusiveDecays, 
            ST_tW_top_5f_inclusiveDecays 
]

for sample in samples:
    print '#######################################'
    print '#### computing pileup for %s'%(sample.name)
    print '#######################################'
    # outfile = ROOT.TFile.Open('pileup_TEST.root', 'recreate')
    outfile = ROOT.TFile.Open('pileup_%s.root'%(sample.name), 'recreate')

    # fill with true interactions
    h_ti = ROOT.TH1F('pileup', 'pileup', 200, 0, 200)

    handle  = Handle ('std::vector<PileupSummaryInfo>')
    label = ("slimmedAddPileupInfo")

    totevents = 0
    nfiles = len(TTJets_amcat.files)
    # nfiles = 1
    batch = 20
    maxend = (nfiles - nfiles%batch) / batch + 1

    for i in range(maxend):
    # for i in range(1):
        
        begin  = batch * (i)
        end    = batch * (i+1)
        
        print 'running of %d-th batch of %d files out of %d total batches' %(i+1, batch, maxend)

        events = Events(TTJets_amcat.files[begin:end])
        # events = Events(samples.files[:10])
        for j, event in enumerate(events):
            # if j%100000==0:
                # print '\t\tprocessing the %d-th event of the %d-th batch' %(j, i+1)
            event.getByLabel(label, handle)
            puinfos = map(PileUpSummaryInfo, handle.product())
            for pu in puinfos:
                if pu.getBunchCrossing()==0:
                    h_ti.Fill(pu.nTrueInteractions())
                    break

        totevents += events.size()
        print '\tprocessed %d events so far' %(totevents)

    outfile.cd()
    h_ti.Write()
    outfile.Close()
