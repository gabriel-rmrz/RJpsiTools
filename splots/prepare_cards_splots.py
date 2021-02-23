#! /bin/env python

# https://roostatsworkbook.readthedocs.io/en/latest/docs-factoryunbinned.html

import ROOT
import os
from math import pi, sqrt
from glob import glob
from pdb import set_trace
from array import array 
import math
import argparse
from cmsstyle import CMS_lumi

from officialStyle import officialStyle
officialStyle(ROOT.gStyle)
ROOT.gStyle.SetTitleOffset(1.3, 'Y')
ROOT.gStyle.SetTitleOffset(0.85, 'X')
ROOT.gStyle.SetPadLeftMargin(0.20)

# ROOT.EnableImplicitMT()
# ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)   

ROOT.gStyle.SetOptStat(True)
ROOT.TH1.SetDefaultSumw2()

### important
ROOT.RooAbsData.setDefaultStorageType(ROOT.RooAbsData.Tree)

##########################################################################################
##      Pick up the observed tree
##########################################################################################

# data_files = ['data_ul.root']
# data_files = ['/Users/manzoni/Documents/RJPsi/samples_20_novembre/samples/data_bc_pmm.root']
data_files = ['/Users/manzoni/Documents/RJPsi/dataframes_december_2020/BcToXToJpsi_is_data_merged.root']

data_tree = ROOT.TChain('BTopmm')
for fname in data_files:
   data_tree.AddFile(fname)


# signal_files = ['/Users/manzoni/Documents/RJPsi/samples_20_novembre/samples/BcToXToJpsi_is_jpsi_pi_merged.root']
signal_files = ['/Users/manzoni/Documents/RJPsi/dataframes_december_2020/BcToXToJpsi_is_jpsi_pi_merged.root']
signal_tree = ROOT.TChain('BTopmm')
for fname in signal_files:
   signal_tree.AddFile(fname)

##########################################################################################
#      Mass type: choose whether bare or post vertex fit
##########################################################################################
# mass_type = 'Bmass'
mass_type = 'bvtx_fit_mass'

##########################################################################################
#      Variables and PDFs
##########################################################################################
myvars = dict()

myvars['mass'       ] = ROOT.RooRealVar(mass_type              , 'J/#psi#pi^{#pm} mass',   6.0,    6.6, 'GeV')
myvars['jpsi_mass'  ] = ROOT.RooRealVar('jpsivtx_fit_mass'     , 'J/#psi mass'         ,   0. ,    6.6, 'GeV')
myvars['jpsi_eta'   ] = ROOT.RooRealVar('jpsivtx_fit_eta'      , 'J/#psi #eta'         ,  -10 ,   10  ,)
myvars['mu1pt'      ] = ROOT.RooRealVar('mu1pt'                , 'mu1pt'               ,   0. , 1000. , 'GeV')
myvars['mu2pt'      ] = ROOT.RooRealVar('mu2pt'                , 'mu2pt'               ,   0. , 1000. , 'GeV')
myvars['mu1eta'     ] = ROOT.RooRealVar('mu1eta'               , 'mu1eta'              , -10. ,   10. )
myvars['mu2eta'     ] = ROOT.RooRealVar('mu2eta'               , 'mu2eta'              , -10. ,   10. )
myvars['bpt'        ] = ROOT.RooRealVar('Bpt'                  , 'Bpt'                 ,   0. , 9000. )
myvars['blxy'       ] = ROOT.RooRealVar('bvtx_lxy'             , 'bvtx_lxy'            ,   0. , 9000. )
myvars['blovers'    ] = ROOT.RooRealVar('bvtx_lxy_sig'         , 'bvtx_lxy_sig'        ,   0. , 9000. )
myvars['bsvprob'    ] = ROOT.RooRealVar('bvtx_svprob'          , 'bvtx_svprob'         ,   0. ,    1. )
myvars['bcos'       ] = ROOT.RooRealVar('bvtx_cos2D'           , 'bvtx_cos2D'          ,   0. ,    1. )
myvars['bchi2'      ] = ROOT.RooRealVar('bvtx_chi2'            , 'bvtx_chi2'           ,   0. , 1000. )
myvars['blxy_unc'   ] = ROOT.RooRealVar('bvtx_lxy_unc'         , 'bvtx_lxy_unc'        ,   0. , 1000. )
myvars['jpsilxy'    ] = ROOT.RooRealVar('jpsivtx_lxy'          , 'bvtx_lxy'            ,   0. , 9000. )
myvars['jpsilovers' ] = ROOT.RooRealVar('jpsivtx_lxy_sig'      , 'bvtx_lxy_sig'        ,   0. , 9000. )
myvars['jpsisvprob' ] = ROOT.RooRealVar('jpsivtx_svprob'       , 'bvtx_svprob'         ,   0. ,    1. )
myvars['jpsicos2D'  ] = ROOT.RooRealVar('jpsivtx_cos2D'        , 'jpsivtx_cos2D'       ,   0. ,    1. )
myvars['jpsichi2'   ] = ROOT.RooRealVar('jpsivtx_chi2'         , 'jpsivtx_chi2'        ,   0. , 1000. )
myvars['jpsilxy_unc'] = ROOT.RooRealVar('jpsivtx_lxy_unc'      , 'jpsivtx_lxy_unc'     ,   0. , 1000. )
# myvars['jpsicos'    ] = ROOT.RooRealVar('jpsivtx_log10_svprob' , 'jpsivtx_cos2D'       ,   0. ,    1. )
# myvars['jpsicos'    ] = ROOT.RooRealVar('jpsivtx_log10_lxy'    , 'jpsivtx_cos2D'       ,   0. ,    1. )
# myvars['jpsicos'    ] = ROOT.RooRealVar('jpsivtx_log10_lxy_sig', 'jpsivtx_cos2D'       ,   0. ,    1. )
myvars['pipt'       ] = ROOT.RooRealVar('kpt'                  , 'kpt'                 ,   0. , 1000. , 'GeV')
myvars['pieta'      ] = ROOT.RooRealVar('keta'                 , 'keta'                , -10. ,   10. )
myvars['mu1id'      ] = ROOT.RooRealVar('mu1_mediumID'         , 'mu1_mediumID'        ,   0. ,    2. )
myvars['mu2id'      ] = ROOT.RooRealVar('mu2_mediumID'         , 'mu2_mediumID'        ,   0. ,    2. )
myvars['mu1dxy'     ] = ROOT.RooRealVar('mu1_dxy'              , 'mu1_dxy'             ,  -5. ,    5. , 'cm')
myvars['mu2dxy'     ] = ROOT.RooRealVar('mu2_dxy'              , 'mu2_dxy'             ,  -5. ,    5. , 'cm')
myvars['pidxy'      ] = ROOT.RooRealVar('k_dxy'                , 'k_dxy'               ,  -5. ,    5. , 'cm')
myvars['mu1dz'      ] = ROOT.RooRealVar('mu1_dz'               , 'mu1_dz'              , -25. ,   25. , 'cm')
myvars['mu2dz'      ] = ROOT.RooRealVar('mu2_dz'               , 'mu2_dz'              , -25. ,   25. , 'cm')
myvars['pidz'       ] = ROOT.RooRealVar('k_dz'                 , 'k_dz'                , -25. ,   25. , 'cm')

# histos['jpsivtx_chi2'         ] = (ROOT.RDF.TH1DModel('jpsivtx_chi2'         , '', 50,      0,    50), 'vtx(#mu_{1}, #mu_{2}) #chi^{2}'                                , 1)
# histos['jpsivtx_lxy_unc'      ] = (ROOT.RDF.TH1DModel('jpsivtx_lxy_unc'      , '',100,      0,  0.02), '#sigma_{L_{xy}} (cm)'                                          , 1)
# histos['jpsivtx_svprob'       ] = (ROOT.RDF.TH1DModel('jpsivtx_svprob'       , '', 50,      0,     1), 'vtx(#mu_{1}, #mu_{2}) probability'                             , 0)
# histos['jpsivtx_log10_svprob' ] = (ROOT.RDF.TH1DModel('jpsivtx_log10_svprob' , '', 51,     -8,     1), 'log_{10} vtx(#mu_{1}, #mu_{2}) probability'                    , 1)
# histos['jpsivtx_log10_lxy'    ] = (ROOT.RDF.TH1DModel('jpsivtx_log10_lxy'    , '', 51,     -4,     1), 'log_{10} vtx(#mu_{1}, #mu_{2}) L_{xy}'                         , 1)
# histos['jpsivtx_log10_lxy_sig'] = (ROOT.RDF.TH1DModel('jpsivtx_log10_lxy_sig', '', 51,     -2,     2), 'log_{10} vtx(#mu_{1}, #mu_{2}) L_{xy}/#sigma_{L_{xy}}'         , 1)

# only MC
myvarsmc = dict()
myvarsmc['k_genpdgId'           ] = ROOT.RooRealVar('k_genpdgId'           , 'k_genpdgId'           , -1e6  , 1e6  )
myvarsmc['k_mother_pdgId'       ] = ROOT.RooRealVar('k_mother_pdgId'       , 'k_mother_pdgId'       , -1e6  , 1e6  )
myvarsmc['mu1_genpdgId'         ] = ROOT.RooRealVar('mu1_genpdgId'         , 'mu1_genpdgId'         , -1e6  , 1e6  )
myvarsmc['mu1_mother_pdgId'     ] = ROOT.RooRealVar('mu1_mother_pdgId'     , 'mu1_mother_pdgId'     , -1e6  , 1e6  )
myvarsmc['mu1_grandmother_pdgId'] = ROOT.RooRealVar('mu1_grandmother_pdgId', 'mu1_grandmother_pdgId', -1e6  , 1e6  )
myvarsmc['mu2_genpdgId'         ] = ROOT.RooRealVar('mu2_genpdgId'         , 'mu2_genpdgId'         , -1e6  , 1e6  )
myvarsmc['mu2_mother_pdgId'     ] = ROOT.RooRealVar('mu2_mother_pdgId'     , 'mu2_mother_pdgId'     , -1e6  , 1e6  )
myvarsmc['mu2_grandmother_pdgId'] = ROOT.RooRealVar('mu2_grandmother_pdgId', 'mu2_grandmother_pdgId', -1e6  , 1e6  )

##########################################################################################
#      mass ranges
##########################################################################################
fit_range_lo   = 5.5
mass_window_lo = 6.275 - 0.15
mass_window_hi = 6.275 + 0.15 
fit_range_hi   = 7.

mass = myvars['mass']
mass.setRange('left' , fit_range_lo  , mass_window_lo)
mass.setRange('right', mass_window_hi, fit_range_hi  )

##########################################################################################
#      PDFs
##########################################################################################
#    1  argpar      -1.95759e+00   1.03831e+01   2.11846e-03  -1.97032e-01
#    2  broad_width   5.62194e-02   5.57457e-03   7.32458e-05  -1.09202e+00
#    3  frac_bkg     4.20044e-01   7.16860e-02   1.56468e-04  -1.60601e-01
#    4  frac_pi      6.31013e-01   6.77992e-02   2.64847e-04   2.65121e-01
#    5  frac_sig     2.67041e-01   2.28339e-01   5.99349e-04  -4.84672e-01
#    6  maxM         6.20639e+00   2.25169e-01   8.23578e-04   7.09100e-01
#    7  mean         6.26774e+00   8.02151e-03   7.24866e-05   1.18543e-01
#    8  narrow_width   2.44845e-02   4.83913e-03   3.78671e-04  -5.35545e-01
#    9  p1          -5.23507e-02   1.16627e-01   4.07071e-06  -5.23507e-04
#   10  sg           1.14919e-02   1.00958e-02   1.07686e-03   2.99617e+00

# combinatorial background poly
pol_c1 = ROOT.RooRealVar('pol_c1', 'coefficient of x^0 term', -5.23507e-02, -100, 100)
# pol_c2 = ROOT.RooRealVar('pol_c2', 'coefficient of x^1 term', 0.6, -10, 10)
# pol_c3 = ROOT.RooRealVar('pol_c3', 'coefficient of x^2 term', 0.5, -10, 10)
bkg = ROOT.RooChebychev('bkg_pol', '1st order poly', mass, ROOT.RooArgList(pol_c1))
# bkg = ROOT.RooChebychev('bkg_pol', '2nd order poly', mass, ROOT.RooArgList(pol_c1, pol_c2))
# bkg = ROOT.RooChebychev('bkg_pol', '3rd order poly', mass, ROOT.RooArgList(pol_c1, pol_c2, pol_c3))

# expo
# slope = ROOT.RooRealVar('slope', 'slope', -0.001, -1e6, 1e6)
# bkg   = ROOT.RooExponential('bkg_expo', 'bkg_expo', mass, slope)

# argus function, partially reconstructed decays
argpar = ROOT.RooRealVar('argpar','argus shape parameter',-1.95759e+00, -20, 20) 
maxM   = ROOT.RooRealVar('maxM'  ,'argus max m'          , 6.20639e+00, 6.0, 6.275) #6.2)
argus  = ROOT.RooArgusBG('argus' ,'Argus PDF', mass, maxM, argpar)

# detector response function
mg       = ROOT.RooRealVar('mg', 'mg', 0)#, -0.01, 0.01)
sg       = ROOT.RooRealVar('sg', 'sg', 1.14919e-02, 0.0001, 0.03)#, 0.001,0.2)
resGauss = ROOT.RooGaussian('resGauss', 'resGauss', mass, mg, sg)
# construct convolution
mass.setBins(10000, 'fft')
lxg = ROOT.RooFFTConvPdf('lxg', 'argus (X) gauss', mass, argus, resGauss)

# Bc->Jpsi K crystal ball
jpsik_mean  = ROOT.RooRealVar('jpsik_mean' , 'mean'    , 6.17, 6.10, 6.25  )
jpsik_sigma = ROOT.RooRealVar('jpsik_sigma', 'sigma'   , 0.03, 0.01, 0.1   )
jpsik_func = ROOT.RooGaussian('jpsik_func', 'jpsik_func', mass, jpsik_mean, jpsik_sigma)
# jpsik_n     = ROOT.RooRealVar('jpsik_n'    , 'jpsik_n'    , 0.1 , 0.01,   3.  )
# jpsik_alpha = ROOT.RooRealVar('jpsik_alpha', 'jpsik_alpha', 2   ,  0.1,   4.  )
# jpsik_func = ROOT.RooCBShape('jpsik_func', 'jpsik_func', mass, jpsik_mean, jpsik_sigma, jpsik_alpha, jpsik_n)

# signal narrow gaussian
mean = ROOT.RooRealVar('mean', 'mean', 6.26774e+00,  6.1, 6.4)
narrow_width = ROOT.RooRealVar('narrow_width', 'narrow_width', 2.44845e-02,  0. , 0.1)
narrow_gaus = ROOT.RooGaussian('sig_narrow_gaus', 'sig_narrow_gaus', mass, mean, narrow_width)

# signal broad gaussian
broad_width = ROOT.RooRealVar('broad_width', 'broad_width', 5.62194e-02,  0. , 1.)
broad_gaus = ROOT.RooGaussian('sig_broad_gaus', 'sig_broad_gaus', mass, mean, broad_width)

# absolute yields
# nsig        = ROOT.RooRealVar('signal_yield'       , 'signal_yield'       ,  800, 0., 10000.)
# nsig_narrow = ROOT.RooRealVar('signal_yield_narrow', 'signal_yield_narrow',  700, 0., 10000.)
# nsig_broad  = ROOT.RooRealVar('signal_yield_broad' , 'signal_yield_broad' ,  100, 0., 10000.)
# nbkgtot     = ROOT.RooRealVar('nbkgtot'            , 'nbkgtot'            , 2000, 0., 10000.)
# nbkg        = ROOT.RooRealVar('nbkg'               , 'nbkg'               , 7000, 0., 10000.)
# nPi         = ROOT.RooRealVar('nPi'                , 'nPi'                , 1000, 0., 10000.)
# nK          = ROOT.RooRealVar('nK'                 , 'nK'                 ,  200, 0., 10000.)

# fractional yields
# you need these and not absolute yields in combine
# don't fit with Extended!
frac_sig = ROOT.RooRealVar('frac_sig', 'frac_sig', 2.67041e-01, 0., 1.)
frac_pi  = ROOT.RooRealVar('frac_pi' , 'frac_pi' , 6.31013e-01, 0., 1.)
frac_bkg = ROOT.RooRealVar('frac_bkg', 'frac_bkg', 4.20044e-01, 0., 1.)
# fixed to PDG (Jpsi K) / (Jpsi pi) value https://pdglive.lbl.gov/BranchingRatio.action?desig=14&parCode=S091
frac_k_value = 0.079/(1.+0.079)
frac_k   = ROOT.RooRealVar('frac_k'  , 'frac_k'  , frac_k_value) 

# signal function
signal_fit_function = ROOT.RooAddPdf(
    'signal_fit_function', 
    'signal_fit_function', 
    ROOT.RooArgList(narrow_gaus, broad_gaus), 
    ROOT.RooArgList(frac_sig)
)

# signal Jpsi pi plus Jpsi K
# RooAddPdf::pi_plus_k_fit_function[ frac_k * jpsik_func + [%] * signal_fit_function ]
pi_plus_k_fit_function = ROOT.RooAddPdf(
    'pi_plus_k_fit_function', 
    'pi_plus_k_fit_function', 
    ROOT.RooArgList(jpsik_func, signal_fit_function), # order matters for coefficients in next line https://www.nikhef.nl/~vcroft/SignalAndBackground-CompositeModels.html
    ROOT.RooArgList(frac_k)
)

# background function
bkg_fit_function = ROOT.RooAddPdf(
    'bkg_fit_function', 
    'bkg_fit_function', 
#     ROOT.RooArgList(bkg, lxg, jpsik_func), 
#     ROOT.RooArgList(frac_pi, frac_k)
    ROOT.RooArgList(lxg, bkg), 
    ROOT.RooArgList(frac_pi)
)

# total function
fit_function = ROOT.RooAddPdf(
    'fit_function', 
    'fit_function', 
    ROOT.RooArgList(bkg_fit_function, pi_plus_k_fit_function), 
    ROOT.RooArgList(frac_bkg)
)

# MC signal narrow gaussian
mc_mean         = ROOT.RooRealVar('mc_mean'        , 'mc_mean'        , 6.275,  5.5, 7.)
mc_narrow_width = ROOT.RooRealVar('mc_narrow_width', 'mc_narrow_width', 0.038,  0. , 1.)
mc_narrow_gaus  = ROOT.RooGaussian('mc_sig_narrow_gaus', 'mc_sig_narrow_gaus', mass, mc_mean, mc_narrow_width)

# MC signal broad gaussian
mc_broad_width = ROOT.RooRealVar('mc_broad_width', 'mc_broad_width',   0.06,  0. , 1.)
mc_broad_gaus  = ROOT.RooGaussian('mc_sig_broad_gaus', 'mc_sig_broad_gaus', mass, mc_mean, mc_broad_width)

mc_nsig        = ROOT.RooRealVar('mc_signal_yield'       , 'mc_signal_yield'       , 800, 0, 10000000)
mc_nsig_narrow = ROOT.RooRealVar('mc_signal_yield_narrow', 'mc_signal_yield_narrow', 700, 0, 10000000)
mc_nsig_broad  = ROOT.RooRealVar('mc_signal_yield_broad' , 'mc_signal_yield_broad' , 100, 0, 10000000)

# MC signal function
mc_signal_fitFunction = ROOT.RooAddPdf(
    'mc_signal_fit_function', 
    'mc_signal_fit_function', 
    ROOT.RooArgList(mc_narrow_gaus, mc_broad_gaus), 
    ROOT.RooArgList(mc_nsig_narrow, mc_nsig_broad)
)

thevars = ROOT.RooArgSet()
for k, v in myvars.items():
    thevars.add(v)
    
thevars_mc = thevars
for k, v in myvarsmc.items():
    thevars_mc.add(v)

##########################################################################################
# selection on data, plotting, fitting
##########################################################################################
# HLT_DoubleMu4_JpsiTrk_Displaced_v14
selection = ' & '.join([
    '%s>6' %mass_type       ,
    '%s<6.6' %mass_type     ,
    'mu1pt>4.5'             ,
    'mu2pt>4.5'             ,
#     'mu1pt>5'               ,
#     'mu2pt>5'               ,
    'abs(mu1eta)<2.4'       ,
    'abs(mu2eta)<2.4'       ,
#     'mu1pt>3.5'             ,
#     'mu2pt>3.5'             ,
#     'Bpt>15'                ,
#     'Blxy>0.01'             , # 100 micron
#     'Blxy_sig>3'            ,
#     'Bsvprob>0.005'         ,
#     'Bsvprob>0.001'         ,
#     'Bsvprob>0.1'           ,
    'kpt>2.5'                 ,
#     'kpt>3.5'               ,
    'abs(keta)<2.4'         ,
    'bvtx_cos2D>0.999'          ,
    'mu1_mediumID>0.5'      ,
    'mu2_mediumID>0.5'      ,
    'abs(mu1_dz-mu2_dz)<0.2', # *
    'abs(mu1_dz-k_dz)<0.2'  , # *
    'abs(mu2_dz-k_dz)<0.2'  , # *
    'abs(k_dxy)<0.05'       , # *
    'abs(mu1_dxy)<0.05'     , # *
    'abs(mu2_dxy)<0.05'     , # *
    '(((abs(mu1eta)<1. & abs(mu1eta)<1.) & abs(jpsivtx_fit_mass-3.0969)<0.1) | (!(abs(mu1eta)<1. & abs(mu1eta)<1.) & abs(jpsivtx_fit_mass-3.0969)<0.15))', # *

#     'abs(mu1eta)<1.2'       ,
#     'abs(mu2eta)<1.2'       ,
#     'abs(keta)<1.2'         ,

])
# add gen matching
selection_mc = ' & '.join([
    selection                        ,
    'abs(k_genpdgId)==211'           ,
    'abs(k_mother_pdgId)==541'       ,
    'abs(mu1_genpdgId)==13'          ,
    'abs(mu1_mother_pdgId)==443'     ,
    'abs(mu2_genpdgId)==13'          ,
    'abs(mu2_mother_pdgId)==443'     ,
    'abs(mu1_grandmother_pdgId)==541',
    'abs(mu2_grandmother_pdgId)==541',
])


fulldata   = ROOT.RooDataSet('data', 'data', data_tree, thevars, selection)
fullsignal = ROOT.RooDataSet('signal', 'signal', signal_tree, thevars_mc, selection_mc)

# plot
c1 = ROOT.TCanvas('c1', '', 700, 700)
c1.Draw()
frame = mass.frame()
frame.SetTitle('')
nbins = 80
fulldata.plotOn(frame, ROOT.RooFit.Binning(nbins), ROOT.RooFit.MarkerSize(1.5))

# fit
# results_data = fit_function.fitTo(fulldata, ROOT.RooFit.Extended(True), ROOT.RooFit.Save()) 
results_data = fit_function.fitTo(fulldata, ROOT.RooFit.Save()) 

fit_function.plotOn(frame);
fit_function.plotOn(frame, ROOT.RooFit.Components('bkg_pol')            , ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kBlue  ))
fit_function.plotOn(frame, ROOT.RooFit.Components('lxg')                , ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kOrange))
# fit_function.plotOn(frame, ROOT.RooFit.Components('argus')              , ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kViolet))
fit_function.plotOn(frame, ROOT.RooFit.Components('signal_fit_function'), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kRed   ))
fit_function.plotOn(frame, ROOT.RooFit.Components('jpsik_func')         , ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kGreen ))

frame.Draw()
CMS_lumi(c1, 4, 0, cmsText = 'CMS', extraText = '   Preliminary', lumi_13TeV = '60 fb^{-1}')

leg = ROOT.TLegend(0.58,.65,.90,.90)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
# leg.SetNColumns(3)

# RooFit demmerda 
leg.AddEntry(c1.GetPrimitive('fit_function_Norm[%s]_Comp[lxg]'%mass_type)                , 'B_{c}#rightarrowJ/#Psi#pi + X', 'L')
leg.AddEntry(c1.GetPrimitive('fit_function_Norm[%s]_Comp[bkg_pol]'%mass_type)            , 'combinatorial bkg'            , 'L')
leg.AddEntry(c1.GetPrimitive('fit_function_Norm[%s]_Comp[signal_fit_function]'%mass_type), 'B_{c}#rightarrowJ/#Psi#pi'    , 'L')
leg.AddEntry(c1.GetPrimitive('fit_function_Norm[%s]_Comp[jpsik_func]'%mass_type)         , 'B_{c}#rightarrowJ/#PsiK'      , 'L')
leg.AddEntry(c1.GetPrimitive('h_data')                                                   , 'observed'                     , 'EP')
leg.Draw('SAME')

# ROOT.gPad.SaveAs('sideband_fit.pdf')
c1.SaveAs('sideband_fit.pdf')


##########################################################################################
#  Fit the mc
###########################################################################################
fullsignal.plotOn(frame, ROOT.RooFit.Binning(nbins), ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.MarkerColor(ROOT.kRed))
results_mc = mc_signal_fitFunction.fitTo(fullsignal, ROOT.RooFit.Extended(True), ROOT.RooFit.Save()) 
mc_signal_fitFunction.plotOn(frame, ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.MarkerColor(ROOT.kRed))
frame.Draw()
CMS_lumi(c1, 4, 0, cmsText = 'CMS', extraText = '   Preliminary', lumi_13TeV = '60 fb^{-1}')
leg.AddEntry(c1.GetPrimitive('mc_signal_fit_function_Norm[%s]'%mass_type), 'B_{c}#rightarrowJ/#Psi#pi MC', 'LP')
leg.Draw('SAME')
c1.SaveAs('sideband_fit_with_mc.pdf')


##########################################################################################
#  Fit the data sidebands with an extended pdf
##########################################################################################
# # number of background events
# extrapolated_nbkg = ROOT.RooRealVar('extrapolated_nbkg', 'extrapolated_nbkg', 1000, 0, 550000)
# # see this https://root-forum.cern.ch/t/fit-only-the-sidebands-yield-on-full-range-using-rooextendpdf/31868
# bkgmodel = ROOT.RooAddPdf('bkg_extended_model', 'bkg_extended_model', ROOT.RooArgList(bkg_fit_function), ROOT.RooArgList(extrapolated_nbkg))
# 
# fulldata.plotOn(frame, ROOT.RooFit.Binning(nbins), ROOT.RooFit.MarkerSize(1.))
# results_bkgmodel = bkgmodel.fitTo(fulldata, ROOT.RooFit.Range('left,right'), ROOT.RooFit.Save())
# # expo.plotOn(frame, ROOT.RooFit.LineColor(ROOT.kBlack))
# expomodel.plotOn(frame, ROOT.RooFit.LineColor(ROOT.kBlue))

##########################################################################################
#  Dump the RooFit Workspace
##########################################################################################
# create output file
output = ROOT.TFile.Open('datacard.root', 'recreate')

print('dumping data')
data =  ROOT.RooDataSet(
    'data_obs', 
    'data_obs',
    fulldata, 
    ROOT.RooArgSet(mass)
)

# create workspace
print('creating workspace')
ws = ROOT.RooWorkspace('w')

# mass variable
ws.factory('%s[%f, %f]' %(mass_type, fit_range_lo, fit_range_hi))

getattr(ws, 'import')(data)
# getattr(ws, 'import')(signal_fit_function)
getattr(ws, 'import')(bkg_fit_function)
# getattr(ws, 'import')(jpsik_func)
getattr(ws, 'import')(pi_plus_k_fit_function)

# in order to fix the ratio jpsi K / jpsi pi, loop over the variables and fix frac_k 
it = ws.allVars().createIterator()
all_vars = [it.Next() for _ in range( ws.allVars().getSize())]
for var in all_vars:
    if var.GetName() in ['mg']: #, 'jpsik_mean', 'jpsik_sigma']:
        var.setConstant()

ws.Write()
output.Close()

# dump the datacard
with open('datacard.txt', 'w') as card:
   card.write(
'''
imax 1 number of bins
jmax * number of processes minus 1
kmax * number of nuisance parameters
--------------------------------------------------------------------------------
shapes background    jpsipi       datacard.root w:bkg_fit_function
shapes bc            jpsipi       datacard.root w:pi_plus_k_fit_function
shapes data_obs      jpsipi       datacard.root w:data_obs
--------------------------------------------------------------------------------
bin               jpsipi
observation       {obs:d}
-----------------------------------------------------------------------------------
bin                                     jpsipi                 jpsipi
process                                 bc                     background
process                                 0                      1
rate                                    {signal:.4f}           {bkg:.4f}
-----------------------------------------------------------------------------------
# lumi          lnN                       1.025                  -   
# here you should put all the needed uncertainties
-----------------------------------------------------------------------------------
bkgNorm      rateParam     jpsipi              background      1.

frac_k        param  {frac_k}        0.00762 # fixed to pdg
argpar        param  {argpar}        {argpar_err}       
broad_width   param  {broad_width}   {broad_width_err}  
# frac_bkg      param  {frac_bkg}      {frac_bkg_err}     
frac_pi       param  {frac_pi}       {frac_pi_err}      
frac_sig      param  {frac_sig}      {frac_sig_err}     
jpsik_mean    param  {jpsik_mean}    {jpsik_mean_err}   
jpsik_sigma   param  {jpsik_sigma}   {jpsik_sigma_err}  
maxM          param  {maxM}          {maxM_err}         
mean          param  {mean}          {mean_err}         
# mg            param  {mg}            {mg_err}           
narrow_width  param  {narrow_width}  {narrow_width_err} 
pol_c1        param  {pol_c1}        {pol_c1_err}           
sg            param  {sg}            {sg_err}           
'''.format(
         obs          = fulldata.numEntries(),
         signal       = (1.+0.079)*(mc_nsig_narrow.getVal() + mc_nsig_broad.getVal()), 
         bkg          = frac_bkg.getVal() * fulldata.numEntries(),
         frac_k       = frac_k_value, 
         argpar       = argpar      .getVal(), 
         broad_width  = broad_width .getVal(), 
         frac_bkg     = frac_bkg    .getVal(), 
         frac_pi      = frac_pi     .getVal(), 
         frac_sig     = frac_sig    .getVal(), 
         jpsik_mean   = jpsik_mean  .getVal(), 
         jpsik_sigma  = jpsik_sigma .getVal(), 
         maxM         = maxM        .getVal(), 
         mean         = mean        .getVal(), 
         mg           = mg          .getVal(), 
         narrow_width = narrow_width.getVal(), 
         pol_c1       = pol_c1      .getVal(), 
         sg           = sg          .getVal(), 
         argpar_err       = argpar      .getError(), 
         broad_width_err  = broad_width .getError(), 
         frac_bkg_err     = frac_bkg    .getError(), 
         frac_pi_err      = frac_pi     .getError(), 
         frac_sig_err     = frac_sig    .getError(), 
         jpsik_mean_err   = jpsik_mean  .getError(), 
         jpsik_sigma_err  = jpsik_sigma .getError(), 
         maxM_err         = maxM        .getError(), 
         mean_err         = mean        .getError(), 
         mg_err           = mg          .getError(), 
         narrow_width_err = narrow_width.getError(), 
         pol_c1_err       = pol_c1      .getError(), 
         sg_err           = sg          .getError(), 
         )
)








##########################################################################################
##             SPlots now
##########################################################################################
## Now we use the SPlot class to add SWeights to our data set based on our model and our yield variables
# for extended pdf fit --> get the yields
nsig = ROOT.RooRealVar('nsig', 'nsig',  800, 0., 10000.)
nbkg = ROOT.RooRealVar('nbkg', 'nbkg', 7000, 0., 10000.)

fit_function_extended = ROOT.RooAddPdf(
    'fit_function_extended', 
    'fit_function_extended', 
    ROOT.RooArgList(bkg_fit_function, pi_plus_k_fit_function), 
    ROOT.RooArgList(nbkg, nsig)
)
results_data_extended = fit_function_extended.fitTo(fulldata, ROOT.RooFit.Extended(True)) 
sData = ROOT.RooStats.SPlot('sData', 'An SPlot', fulldata, fit_function_extended, ROOT.RooArgList(nsig, nbkg) )

output = ROOT.TFile.Open('jpsi_pi_splots.root', 'recreate')
tree = fulldata.GetClonedTree() ### was .tree()
tree.SetName('tree')
tree.Write()

treemc = fullsignal.GetClonedTree() ### was .tree()
treemc.SetName('treemc')
treemc.Write()
# ws = ROOT.RooWorkspace('w')
# getattr(ws, 'import')(sData)
# ws.Write()
output.Close()