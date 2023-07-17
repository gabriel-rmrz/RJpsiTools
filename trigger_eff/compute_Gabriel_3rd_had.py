#!/bin/env python

import ROOT
from ROOT import TTree, TEfficiency, TH1D, gPad, TPad, TAxis, TH1
from array import array
from selections import preselection, preselection_had
from copy import copy
 

#outdir  = "plots_dimoun0_no_vertex"
outdir = "plots_doubleMu4_3_jpsi_3rd_had" 

def get_efficiency(df, var_name, bins, cuts, is_mc):
  c1 = ROOT.TCanvas('c1', '', 800, 800)

  #df = df.Define("weight","(float)0.5")
  #  histo_num = df.Filter(cuts[0]).Histo1D((var_name, 'Numerator', len(bins) -1, array('d',bins)), var_name, 'weight')
  df = df.Define("weight",'mu2_isFromDoubleMuT_HLTps')
  histo_num = df.Filter(cuts[0]).Histo1D((var_name, 'Numerator', len(bins) -1, array('d',bins)), var_name, "weight") 
  histo_den = df.Filter(cuts[1]).Histo1D((var_name, 'Denominator', len(bins) -1, array('d',bins)), var_name, "weight")

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

  histo_num.SetBinErrorOption(TH1.kPoisson)
  histo_den.SetBinErrorOption(TH1.kPoisson)


  histo_num.Draw('e')
  gPad.BuildLegend(0.68,0.795,0.980,0.935,"","f")
  c1.SaveAs(outdir + '/num_'+var_name+sufix)
  histo_den.Draw('e')
  gPad.BuildLegend(0.68,0.795,0.980,0.935,"","f")
  c1.SaveAs(outdir + '/den_'+var_name+sufix)
  histo_num.Draw('e same')
  gPad.BuildLegend(0.68,0.745,0.980,0.935,"","f")
  c1.SaveAs(outdir + '/both_'+var_name+sufix)

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
  c1.SaveAs(outdir + '/eff_'+var_name+'.png')

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
  c1.SaveAs(outdir + '/eff_ratio_'+var_name+'.png')

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
  #print(eff_ratio.GetYaxis().GetLabelSize())
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
  c2.SaveAs(outdir + '/eff_with_ratio_'+var_name+'.png')

  return 0


def main():
  trigger_sel_3Mu = ' & '.join([
    'mu1_isFromMuT > 0.5',
    'mu2_isFromMuT>0.5', 
    'k_isFromMuT>0.5'
  ])

  trigger_sel_Had = ' & '.join([  
    'mu1_isFromTrkT',
    'mu2_isFromTrkT',
#    'k_isFromTrkT>0.5'
    'k_trg >0.5' 
 ])
  #ref_trigger_sel = 'mu1_isDimuon0_jpsi_Trg & mu2_isDimuon0_jpsi_Trg & HLT_Dimuon0_Jpsi_NoVertexing '
  #ref_trigger_sel = 'mu1_isDimuon0_jpsi_Trg & mu2_isDimuon0_jpsi_Trg '
  #ref_trigger_sel = ' HLT_Dimuon0_Jpsi_NoVertexing==1 '
  ref_trigger_sel = ' HLT_DoubleMu4_3_Jpsi==1 & mu1_isDoubleMuT>0.5 &mu2_isFromDoubleMuT>0.5'

  preselection_data = ' & '.join([
    preselection_had,
    ref_trigger_sel
    ])
  
  num_selection_3Mu = ' & '.join([
#      trigger_sel_3Mu,
    trigger_sel_Had,
    preselection_data
  ])
  
  cuts_3Mu_data = [num_selection_3Mu, preselection_data]
  

  #ref_trigger_sel_mc = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)'
  #ref_trigger_sel_mc = ref_trigger_sel 
  #preselection_mc = ' & '.join([
  #  preselection,
  #  ref_trigger_sel_mc
  #  ])
  #num_selection_3Mu = ' & '.join([
  #    trigger_sel_3Mu,
  #    preselection_mc
  #    ])
  
  #cuts_3Mu_mc = [num_selection_3Mu, preselection_mc]
  cuts_3Mu_mc= cuts_3Mu_data
  bins_pt = [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
  bins_eta = [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4] 
  abseta = [0.0, 0.9, 1.2, 2.4]
  '''  
  binning = {

      'jpsivtx_dR': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0,1.2,1.4],
      'mu1pt': [4.0, 4.5, 5, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 40.0],
      'mu2pt': [4.0, 4.5, 5, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 40.0],
      'Bpt': [5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0],
      'kpt': [1,1.5,2,2.5,3,3.5,4,5.0, 5.5, 6.0, 8.0, 10.0, 15.0, 20.0, 25.0, 40.0],
      'jpsi_pt': [6.8,7.0,8.0, 10.0, 12.0, 15.0, 20.0, 25, 30.0],
      'mu1eta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.4, -0.2, 0, 0.2, 0.4, 0.9, 1.2, 1.6, 2.1, 2.4],
      'mu2eta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.4, -0.2,0, 0.2, 0.4, 0.9, 1.2, 1.6, 2.1, 2.4],
      'Beta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.4, -0.2,0, 0.2, 0.4, 0.9, 1.2, 1.6, 2.1, 2.4],
      'keta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.4, -0.2,0, 0.2, 0.4, 0.9, 1.2, 1.6, 2.1, 2.4],
      'jpsi_eta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.4, -0.2,0, 0.2, 0.4, 0.9, 1.2, 1.6, 2.1, 2.4],
      'jpsi_mass': [2.8, 2.9, 3.0, 3.05, 3.1, 3.15, 3.2, 3.3],
      'Bmass': [3.0, 3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6.0,6.2,6.4,6.6,6.8,7.,8.0, 10.0],
      'mu1phi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'mu2phi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'Bphi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'kphi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'jpsi_phi': [-3.3, -3.0, -2.7,  -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.3],
      'jpsivtx_svprob': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0],
      'jpsivtx_lxy_sig': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0,1.2, 1.6, 2.1, 2.4, 2.7, 3.0, 3.5,4,5,6],
       'jpsivtx_cos2D':[ 0.8,0.9,0.92,0.94,0.96, 0.98, 1.0], 
       'jpsivtx_maxdoca':[ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0], 
       'bvtx_lxy_sig':[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0,1.2, 1.6, 2.1, 2.4,2.7, 3.0, 3.5,4,5,6],
       'k_d0sig':[2, 2.1, 2.4,2.7,3.0, 3.5,4,5,6],
  } 
  '''
  binning = {
      'dr12': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0],
      'dr23': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0,1.2,1.4,1.6,1.8,2,2.2],
      'dr13': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0,1.2,1.4,1.6,1.8,2,2.2],
    }

#  ntuples_dir = "/pnfs/psi.ch/cms/trivcat/store/user/cgalloni/dataframes_2023Feb09/" #plots_dimoun0_no_vertex
#  ntuples_dir = "/pnfs/psi.ch/cms/trivcat/store/user/cgalloni/dataframes_2023Mar12/" plots_doubleMu4_3_jpsi

  ntuples_dir = "/pnfs/psi.ch/cms/trivcat/store/user/cgalloni/dataframes_2023Jul04/" 
  #df_3Mu = ROOT.RDataFrame("BTo3Mu", ntuples_dir + "data_merged_v11.root")
  df_3Mu = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "data__merged_v11.root")

  #df_2MuP = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "data_trigger.root")
  #df_2Mu3P = ROOT.RDataFrame("BTo2Mu3P", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")

  df_3Mu_mc = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "HbToJPsiMuMu__merged_v11.root")
  #df_3Mu_mc = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_merged_v11.root")

  #df_3Mu_mc = ROOT.RDataFrame("BTo3Mu", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")
  #df_2MuP_mc = ROOT.RDataFrame("BTo2MuP", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")
  #df_2Mu3P_mc = ROOT.RDataFrame("BTo2Mu3P", ntuples_dir + "BcToJPsiMuMu_is_jpsi_mu_trigger.root")
  
  for var_name, bins in binning.items(): 
    print ("var_name " , var_name)
    eff = get_efficiency(df_3Mu, var_name, bins, cuts_3Mu_data, is_mc = False)
    eff_mc = get_efficiency(df_3Mu_mc, var_name, bins, cuts_3Mu_mc,is_mc = True)
    plot_efficiencies(eff, eff_mc, var_name, bins)

if __name__ == '__main__':
  ROOT.gROOT.SetBatch()
  ROOT.TH1.SetDefaultSumw2()
  ROOT.gStyle.SetOptStat(0)
  main()