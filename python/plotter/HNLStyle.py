from ROOT import TColor, kViolet, kBlue, kRed, kCyan, kAzure

class Style:

    def __init__(self,
                 markerStyle=8,
                 markerColor=1,
                 markerSize=1,
                 lineStyle=1,
                 lineColor=1,
                 lineWidth=2,
                 fillColor=None,
                 fillStyle=1001,
                 drawAsData=False):
        self.markerStyle = markerStyle
        self.markerColor = markerColor
        self.markerSize = markerSize
        self.lineStyle = lineStyle
        self.lineColor = lineColor
        self.lineWidth = lineWidth
        if fillColor is None:
            self.fillColor = lineColor
        else:
            self.fillColor = fillColor
        self.fillStyle = fillStyle
        self.drawAsData = drawAsData

    def formatHisto(self, hist, title=None):
        hist.SetMarkerStyle(self.markerStyle)
        hist.SetMarkerColor(self.markerColor)
        hist.SetMarkerSize(self.markerSize)
        hist.SetLineStyle(self.lineStyle)
        hist.SetLineColor(self.lineColor)
        hist.SetLineWidth(self.lineWidth)
        hist.SetFillColor(self.fillColor)
        hist.SetFillStyle(self.fillStyle)
        if title != None:
            hist.SetTitle(title)
        return hist

# the following standard files are defined and ready to be used.
# more standard styles can be added on demand.
# user defined styles can be created in the same way in any python module

sBlack = Style()
sData = Style(fillStyle=0, markerSize=1.3, drawAsData=True)
sBlue = Style(markerColor=4, fillColor=4)
sGreen = Style(markerColor=8, fillColor=8)
sRed = Style(markerColor=2, fillColor=2)
sYellow = Style(lineColor=1, markerColor=5, fillColor=5)
sViolet = Style(lineColor=1, markerColor=kViolet, fillColor=kViolet)

# John's colours
qcdcol      = TColor.GetColor(250,202,255)
dycol       = TColor.GetColor(248,206,104)
wcol        = TColor.GetColor(222,90,106)
ttcol       = TColor.GetColor(155,152,204)
stcol       = TColor.GetColor(154,124,204)
zlcol       = TColor.GetColor(100,182,232)
dibosoncol  = kBlue+2 
tribosoncol = kCyan   
ttvcol      = kCyan+2 

# Backgrounds
sHNL_QCD    = Style(lineColor=1, markerColor=qcdcol     , fillColor=qcdcol     )
sHNL_DYJets = Style(lineColor=1, markerColor=dycol      , fillColor=dycol      )
sHNL_WJets  = Style(lineColor=1, markerColor=wcol       , fillColor=wcol       )
sHNL_TTJets = Style(lineColor=1, markerColor=ttcol      , fillColor=ttcol      )
sHNL_ST     = Style(lineColor=1, markerColor=stcol      , fillColor=stcol      )
sHNL_ZL     = Style(lineColor=1, markerColor=zlcol      , fillColor=zlcol      )
sHNL_VV     = Style(lineColor=1, markerColor=dibosoncol , fillColor=dibosoncol )
sHNL_TTV    = Style(lineColor=1, markerColor=ttvcol     , fillColor=ttvcol     )
sHNL_rare   = Style(lineColor=1, markerColor=tribosoncol, fillColor=tribosoncol)

# Signals
sHNL_HN  = Style(lineColor=kBlue   , markerColor=0, lineStyle=2, fillColor=0, lineWidth=3)
sHNL_HN2 = Style(lineColor=kAzure+8, markerColor=0, lineStyle=3, fillColor=0, lineWidth=3)


sBlackSquares = Style(markerStyle=21)
sBlueSquares  = Style(lineColor=4, markerStyle=21, markerColor=4)
sGreenSquares = Style(lineColor=8, markerStyle=21, markerColor=8)
sRedSquares   = Style(lineColor=2, markerStyle=21, markerColor=2)


styleSet = [sBlue, sGreen, sRed, sYellow, sViolet, sBlackSquares, sBlueSquares, sGreenSquares, sRedSquares]
iStyle = 0


def nextStyle():
    global iStyle
    style = styleSet[iStyle]
    iStyle = iStyle+1
    if iStyle >= len(styleSet):
        iStyle = 0
    return style

histPref = {}
histPref['Data'       ] = {'style':sData      , 'layer':2999, 'legend':'Observed'}
histPref['data_*'     ] = {'style':sData      , 'layer':2999, 'legend':'Observed'}
histPref['data_obs'   ] = {'style':sData      , 'layer':2999, 'legend':'Observed'}
histPref['ZTT*'       ] = {'style':sHNL_DYJets, 'layer':4   , 'legend':'Z#rightarrow#tau#tau'}
histPref['DY*'        ] = {'style':sHNL_DYJets, 'layer':4   , 'legend':'DY'}#Z#rightarrow#tau#tau'}
histPref['embed_*'    ] = {'style':sViolet    , 'layer':4.1 , 'legend':None}
histPref['TTJets*'    ] = {'style':sHNL_TTJets, 'layer':1   , 'legend':'t#bar{t}'} 
histPref['T*tW*'      ] = {'style':sHNL_ST    , 'layer':1   , 'legend':'Single t'} 
histPref['TTo*'       ] = {'style':sHNL_ST    , 'layer':1   , 'legend':'Single t'} 
histPref['TBarTo*'    ] = {'style':sHNL_ST    , 'layer':1   , 'legend':'Single t'} 
histPref['Single t'   ] = {'style':sHNL_ST    , 'layer':1   , 'legend':'Single t'} 
histPref['single-t'   ] = {'style':sHNL_ST    , 'layer':1   , 'legend':'Single t'} 
histPref['WW*'        ] = {'style':sHNL_VV    , 'layer':0.9 , 'legend':'Diboson'} 
histPref['WZ*'        ] = {'style':sHNL_VV    , 'layer':0.8 , 'legend':'Diboson'} 
histPref['ZZ*'        ] = {'style':sHNL_VV    , 'layer':0.7 , 'legend':'Diboson'} 
histPref['Diboson'    ] = {'style':sHNL_VV    , 'layer':0.7 , 'legend':'Diboson'} 
histPref['di-boson'   ] = {'style':sHNL_VV    , 'layer':0.7 , 'legend':'Diboson'} 
histPref['VV*'        ] = {'style':sHNL_VV    , 'layer':0.7 , 'legend':'Diboson'} 
histPref['TTZ*'       ] = {'style':sHNL_TTV   , 'layer':1   , 'legend':'t#bar{t}Z'} 
histPref['TTW*'       ] = {'style':sHNL_TTV   , 'layer':1   , 'legend':'t#bar{t}W'} 
histPref['ttV'        ] = {'style':sHNL_TTV   , 'layer':1   , 'legend':'t#bar{t}V'} 
histPref['WGG*'       ] = {'style':sHNL_rare  , 'layer':0.7 , 'legend':'Triboson'} 
histPref['WWW*'       ] = {'style':sHNL_rare  , 'layer':0.7 , 'legend':'Triboson'} 
histPref['ZZZ*'       ] = {'style':sHNL_rare  , 'layer':0.7 , 'legend':'Triboson'} 
histPref['Triboson'   ] = {'style':sHNL_rare  , 'layer':0.7 , 'legend':'Triboson'} 
histPref['tri-boson'  ] = {'style':sHNL_rare  , 'layer':0.7 , 'legend':'Triboson'} 
histPref['Electroweak'] = {'style':sHNL_VV    , 'layer':0.7 , 'legend':'Electroweak'} 
histPref['QCD*'       ] = {'style':sHNL_QCD   , 'layer':2   , 'legend':'QCD multijet'}
histPref['W'          ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
histPref['WJ*'        ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
histPref['W1J*'       ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
histPref['W2J*'       ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
histPref['W3J*'       ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
histPref['W4J*'       ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
# histPref['W*Jets*'    ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'W+jets'}  
histPref['EWK'        ] = {'style':sHNL_WJets , 'layer':3   , 'legend':'EWK'}  
histPref['ElectroWeak'] = {'style':sHNL_WJets , 'layer':3   , 'legend':'ElectroWeak'}  
histPref['ZJ*'        ] = {'style':sHNL_DYJets, 'layer':3.1 , 'legend':'Z#rightarrow#tau#tau/Z#rightarrow ll, j#rightarrow#tau'}
histPref['ZL*'        ] = {'style':sHNL_ZL    , 'layer':3.2 , 'legend':'Z#rightarrow ll'}
histPref['WLL*'       ] = {'style':sHNL_ZL    , 'layer':3.2 , 'legend':'W#rightarrow ll'}
histPref['Zl0jet*'    ] = {'style':sHNL_ZL    , 'layer':3.2 , 'legend':'Z#rightarrow ll + 0 jets'}
histPref['Zl1jet*'    ] = {'style':sHNL_DYJets, 'layer':3.2 , 'legend':'Z#rightarrow ll + 1 jet'}
histPref['ZLL'        ] = {'style':sHNL_ZL    , 'layer':3.2 , 'legend':'Z#rightarrow ll'}
histPref['Ztt_TL'     ] = {'style':sViolet    , 'layer':4.1 , 'legend':'Z#rightarrow#tau#tau/Z#rightarrow ll, j#rightarrow#tau'}
histPref['HN*'        ] = {'style':sHNL_HN    , 'layer':2999, 'legend':'Sig @ 200pb'}

