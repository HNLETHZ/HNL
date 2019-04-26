import ROOT
ff = ROOT.TFile.Open('bfield.root', 'read')
tt = ff.Get("IdealMagneticFieldRecord")
tt.Scan()
tt.GetEntries()
aa = ROOT.GlobalPoint(10, 10, 0)
tt.MagneticField__IdealMagneticFieldRecord.inTesla(aa)
