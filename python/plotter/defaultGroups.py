def createDefaultGroups(plot):
    plot.Group('di-boson' , ['VVTo2L2Nu', 'ZZTo2L2Q', 'WWTo1L1Nu2Q', 'WZTo1L3Nu', 'ZZTo4L', 'WZTo3L', 'WZTo3LNu', 'WZTo2L2Q', 'WZTo1L1Nu2Q', 'WWTo2L2Nu', 'ZZTo4L_ext', 'WW_DoubleScattering', 'WLLJJ_WToLNu_EWK', 'WGGJets'], silent=False)
    plot.Group('tri-boson', ['ZZZ', 'WZZ', 'WWZ', 'WWW'], silent=False)
#     plot.Group('data_obs' , ['data_2017B_e', 'data_2017C_e', 'data_2017D_e', 'data_2017E_e', 'data_2017F_e'], silent=False)
    plot.Group('data_obs' , ['data_2017B', 'data_2017C', 'data_2017D', 'data_2017E', 'data_2017F'], silent=False)
    plot.Group('single-t' , ['ST_sch_lep', 'STbar_tch_inc', 'ST_tch_inc', 'STbar_tW_inc', 'ST_tW_inc'], silent=False)
    plot.Group('DY'       , ['DYJetsToLL_M5to50', 'DYJets', 'DYJets_ext'], silent=False)
    plot.Group('WJets'    , ['W3JetsToLNu', 'W4JetsToLNu', 'WJetsToLNu'], silent=False)
    plot.Group('ttV'      , ['TTWJetsToLNu', 'TTZToLL_M10', 'TTZToLL_M1to10'], silent=False)


# 
# 'data_obs'
# 'single t'
# 'Diboson' 
# 'Triboson'
# 'ttV'     
# 'DY'      
