#!/bin/env python

import ROOT
from ROOT import TTree, TEfficiency, TH1D, gPad, TPad, TAxis
from array import array
from selections import preselection
from copy import copy


def get_efficiency(df, var_name, bins, cuts, is_mc):
  c1 = ROOT.TCanvas('c1', '', 800, 800)
  print(" cuts [0]:", cuts[0], ", cuts[1] :", cuts[1])
  histo_num = df.Filter(cuts[0]).Histo1D((var_name, 'Numerator', len(bins) -1, array('d',bins)), var_name)
  histo_den = df.Filter(cuts[1]).Histo1D((var_name, 'Denominator', len(bins) -1, array('d',bins)), var_name)

  histo_num.SetLineColor(3)
  histo_num.SetMarkerColor(3)
  histo_num.SetMarkerSize(1.0)
  histo_num.SetLineWidth(2)
  histo_num.SetMarkerStyle(20)
  histo_den.SetLineColor(6)
  histo_den.SetMarkerColor(6)
  histo_den.SetLineWidth(2)
  histo_den.SetMarkerSize(1.0)
  histo_den.SetMarkerStyle(20)

  sufix= ".png"
  if(is_mc):
    sufix= "_mc.png"


  histo_num.Draw('e')
  gPad.BuildLegend(0.68,0.795,0.980,0.935,"","f")
  c1.SaveAs('plots/num_'+var_name+sufix)
  histo_den.Draw('e')
  gPad.BuildLegend(0.68,0.795,0.980,0.935,"","f")
  c1.SaveAs('plots/den_'+var_name+sufix)
  histo_num.Draw('e same')
  gPad.BuildLegend(0.68,0.745,0.980,0.935,"","f")
  c1.SaveAs('plots/both_'+var_name+sufix)

  eff = TEfficiency(histo_num.GetValue(), histo_den.GetValue())

  return eff

def plot_efficiencies(eff, eff_mc, var_name, bins):
  min_x = bins[0] - 0.05*(bins[-1] - bins[0])
  max_x = bins[-1] + 0.05*(bins[-1] - bins[0])
  c1 = ROOT.TCanvas('c1', '', 800, 800)
  eff.SetStatisticOption(TEfficiency.kFCP)
  eff_mc.SetStatisticOption(TEfficiency.kFCP)

  eff.SetTitle(';'.join(['',var_name, 'HLT efficiency']))
  eff.SetMarkerSize(0.5)
  eff.SetMarkerStyle(20)

  eff_mc.SetLineColor(4)
  eff_mc.SetMarkerColor(4)
  eff_mc.SetMarkerSize(0.5)
  eff_mc.SetMarkerStyle(20)

  gPad.DrawFrame(min_x, 0.0, max_x,1.05)
  eff.Draw("P")

  eff_mc.SetStatisticOption(TEfficiency.kFCP)
  eff_mc.SetTitle(';'.join(['',var_name, 'HLT efficiency']))
  eff_mc.Draw("same")
  ROOT.gPad.Update()
  eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)
  eff.GetPaintedGraph().GetXaxis().SetLabelSize(0.04)
  eff.GetPaintedGraph().GetYaxis().SetLabelSize(0.04)
  eff.GetPaintedGraph().GetXaxis().SetTitleSize(0.04)
  eff.GetPaintedGraph().GetYaxis().SetTitleSize(0.04)
  eff.GetPaintedGraph().GetXaxis().SetTitleOffset(1.2)
  eff.GetPaintedGraph().GetYaxis().SetTitleOffset(1.2)

  eff_mc.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)
  eff_mc.GetPaintedGraph().GetXaxis().SetLabelSize(0.04)
  eff_mc.GetPaintedGraph().GetYaxis().SetLabelSize(0.04)
  eff_mc.GetPaintedGraph().GetXaxis().SetTitleSize(0.04)
  eff_mc.GetPaintedGraph().GetYaxis().SetTitleSize(0.04)
  eff_mc.GetPaintedGraph().GetXaxis().SetTitleOffset(1.2)
  eff_mc.GetPaintedGraph().GetYaxis().SetTitleOffset(1.2)

  c1.Update()
  c1.SaveAs('plots_v1/eff_'+var_name+'.png')

  eff_histo = TH1D(var_name+'_eff_histo', '', len(bins) -1, array('d',bins))
  eff_mc_histo = TH1D(var_name+'_eff_mc_histo', '', len(bins) -1, array('d',bins))
  
  eff_ratio_den = TH1D(var_name+'_eff_ratio_den', '', len(bins) -1, array('d',bins))
  eff_ratio_num = TH1D(var_name+'_eff_ratio_num', '', len(bins) -1, array('d',bins))
  eff_ratio = TH1D(var_name+'_eff_ratio', '', len(bins) -1, array('d',bins))
  eff_ratio.SetTitle(';'.join(['',var_name, '#epsilon_{Data}/#epsilon_{MC}']))
  eff_dummy = TH1D(var_name+'_eff_dummy', '', len(bins) -1, array('d',bins))
  eff_dummy.SetTitle(';'.join(['',var_name, 'HLT efficiency']))

  eff_den = eff.GetTotalHistogram()
  eff_num = eff.GetPassedHistogram()

  eff_mc_den = eff_mc.GetTotalHistogram()
  eff_mc_num = eff_mc.GetPassedHistogram()

  eff_ratio_num.Multiply( eff_num, eff_mc_den )
  eff_ratio_den.Multiply( eff_den, eff_mc_num )


  #eff_ratio.Divide(eff_ratio_num, eff_ratio_den,1.,1., "cl=0.683 b(1,1) mode")
  eff_ratio.Divide(eff_ratio_num, eff_ratio_den,1.,1.)

  '''
  for i in range(len(bins) -1):
    eff_i = eff.GetEfficiency(i+1)
    eff_mc_i = eff_mc.GetEfficiency(i+1)

    eff_histo.SetBinContent(i+1, eff_i)   
    eff_mc_histo.SetBinContent(i+1, eff_mc_i)   
    eff_ratio.SetBinContent(i+1, 0)
    if(eff_mc_i != 0):
      eff_ratio.SetBinContent(i+1, eff_i/eff_mc_i)
  '''

  eff_ratio.SetBins(len(bins) -1, array('d',bins))
  eff_dummy.SetBins(len(bins) -1, array('d',bins))
  #eff_dummy.GetXaxis().SetRangeUser(min_x, max_x)
  #eff_ratio.GetXaxis().SetRangeUser(min_x, max_x)
  eff_dummy.GetXaxis().SetLimits(min_x, max_x)
  eff_ratio.GetXaxis().SetLimits(min_x, max_x)
  eff_dummy.GetYaxis().SetRangeUser(0.0, 1.2)
  eff_ratio.Draw('e')
  c1.SaveAs('plots_v1/eff_ratio_'+var_name+'.png')

  c2 = ROOT.TCanvas("c2", "",800, 1000)
  upPad = TPad("upPad", "", 0.005,0.25, .995, .995)
  loPad = TPad("upPad", "", 0.005,0.005, .995, .25)
  upPad.SetBottomMargin(0)
  loPad.SetBottomMargin(0.3)
  loPad.SetTopMargin(0)
  upPad.Draw()
  loPad.Draw()
  upPad.cd()
  
  eff_dummy.Draw('axis')
  eff.Draw("same")
  eff_mc.Draw("same")
  upPad.Update()
  eff.GetPaintedGraph().GetXaxis().SetRangeUser(min_x, max_x)
  eff.GetPaintedGraph().GetXaxis().SetLabelSize(0.01)
  eff.GetPaintedGraph().GetXaxis().SetTitleSize(0.04)
  eff.GetPaintedGraph().GetXaxis().SetTitleOffset(0.0)
  eff.GetPaintedGraph().GetYaxis().SetLabelSize(0.03)
  eff.GetPaintedGraph().GetYaxis().SetTitleSize(0.03)
  eff_mc.GetPaintedGraph().GetXaxis().SetLabelSize(0.0)
  eff_mc.GetPaintedGraph().GetXaxis().SetTitleSize(0.0)
  eff_mc.GetPaintedGraph().GetXaxis().SetTitleOffset(0.0)
  eff.SetTitle(';'.join(['',var_name, 'HLT efficiency']))
  upPad.Modified()
  c2.Update()

  loPad.cd()
  eff_ratio.Draw('e')
  loPad.Update()
  #print(eff_ratio.GetYaxis().GetTitleSize())
  print(eff_ratio.GetYaxis().GetLabelSize())
  eff_ratio.GetYaxis().SetLabelSize(0.1)
  eff_ratio.GetYaxis().SetTitleSize(0.13)
  eff_ratio.GetYaxis().SetTitleOffset(0.4)

  eff_ratio.GetXaxis().SetLabelSize(0.1)
  eff_ratio.GetXaxis().SetTitleSize(0.13)
  eff_ratio.GetXaxis().SetTitleOffset(0.8)
  eff_ratio.GetYaxis().SetRangeUser(0.6, 1.2)
  eff_ratio.SetLineColor(8)
  eff_ratio.SetMarkerColor(8)
  eff_ratio.SetMarkerSize(0.5)
  eff_ratio.SetMarkerStyle(20)
  loPad.Modified()
  loPad.Update()
  c2.Update()
  c2.SaveAs('plots_v1/eff_with_ratio_'+var_name+'.png')

  return 0


def main():

  trigger_sel_3Mu = ' && '.join([
    'mu1_isFromMuT > 0.5',
    'mu2_isFromMuT>0.5', 
    'k_isFromMuT>0.5'
  ])
  num_selection_3Mu = ' && '.join([
      preselection,
      trigger_sel_3Mu
      ])
  #num_selection_3Mu = preselection 
  cuts_3Mu = [num_selection_3Mu, preselection]
  
  bins_pt = [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
  bins_eta = [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4] 
  abseta = [0.0, 0.9, 1.2, 2.4]
  
  binning = {
      'mu1pt': [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0],
      'mu2pt': [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0],
      'Bpt': [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0],
      'kpt': [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0],
      'jpsi_pt': [6.0, 8.0, 10.0, 12.0, 15.0, 20.0, 30.0, 40.0],
      'mu1eta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4],
      'mu2eta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4],
      'Beta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4],
      'keta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4],
      'jpsi_eta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4],
      'mu1phi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'mu2phi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'Bphi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'kphi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'jpsi_phi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3]
      }

  ntuples_dir = "../forCamilla/dataframes_2022Nov07_prepared/"
  df_3Mu = ROOT.RDataFrame("BTo3Mu", ntuples_dir + "data_trigger.root")
  #df_2MuP = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "data_trigger.root")
  #df_2Mu3P = ROOT.RDataFrame("BTo2Mu3P", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")

  df_3Mu_mc = ROOT.RDataFrame("BTo3Mu", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")
  #df_3Mu_mc = ROOT.RDataFrame("BTo3Mu", ntuples_dir + "HbToJPsiMuMu_3MuFilter_trigger_bcclean.root")
  #df_2MuP_mc = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")
  #df_2Mu3P_mc = ROOT.RDataFrame("BTo2Mu3P", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")
  
  for var_name, bins in binning.items(): 
    eff = get_efficiency(df_3Mu, var_name, bins, cuts_3Mu, is_mc = False)
    print("first eff on data for var:", var_name)
    eff_mc = get_efficiency(df_3Mu_mc, var_name, bins, cuts_3Mu,is_mc = True)
    print("first eff on mc for var:", var_name)
    plot_efficiencies(eff, eff_mc, var_name, bins)
    print("eff plotted:", var_name)
if __name__ == '__main__':
  ROOT.gROOT.SetBatch()
  ROOT.TH1.SetDefaultSumw2()
  ROOT.gStyle.SetOptStat(0)
  main()
