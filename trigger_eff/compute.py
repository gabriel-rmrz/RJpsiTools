#!/bin/env python

import ROOT
from ROOT import TTree, TEfficiency
from array import array
from selections import preselection

def getEffHisto(df, var_name, bins, cuts):
  c1 = ROOT.TCanvas('c1', '', 800, 800)
  histo_num = df.Filter(cuts[0]).Histo1D((var_name, '', len(bins) -1, array('d',bins)), var_name)
  histo_den = df.Filter(cuts[1]).Histo1D((var_name, '', len(bins) -1, array('d',bins)), var_name)

  histo_num.Draw('e')
  c1.SaveAs('num_'+var_name+'_histo.pdf')

  histo_den.Draw('e')
  c1.SaveAs('den_'+var_name+'_histo.pdf')

  eff_histo = TEfficiency(histo_num.GetPtr(), histo_den.GetPtr())

  eff_histo.SetStatisticOption(TEfficiency.kFCP)
  eff_histo.SetTitle(';'.join(['',var_name, 'HLT efficiency']))
  eff_histo.Draw()
  ROOT.gPad.Update()

  eff_histo.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)
  eff_histo.GetPaintedGraph().GetXaxis().SetLabelSize(0.04)
  eff_histo.GetPaintedGraph().GetYaxis().SetLabelSize(0.04)
  eff_histo.GetPaintedGraph().GetXaxis().SetTitleSize(0.04)
  eff_histo.GetPaintedGraph().GetYaxis().SetTitleSize(0.04)
  eff_histo.GetPaintedGraph().GetXaxis().SetTitleOffset(1.2)
  eff_histo.GetPaintedGraph().GetYaxis().SetTitleOffset(1.2)
  ROOT.gPad.Update()
  c1.SaveAs('eff_'+var_name+'_histo.pdf')
  return eff_histo


def main():

  trigger_sel = ' & '.join([
    'mu1_isFromMuT > 0.5',
    'mu2_isFromMuT>0.5', 
    'k_isFromMuT>0.5'
  ])
  num_selection = ' & '.join([
      trigger_sel,
      preselection
      ])
  cuts = [num_selection, preselection]
  
  bins_pt = [3.25, 3.5, 3.75, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
  bins_eta = [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4] 
  abseta = [0.0, 0.9, 1.2, 2.4]
  
  binning = {
      'Bpt': [3.25, 3.5, 3.75, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0],
      'Beta': [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4]
      }
  df = ROOT.RDataFrame("BTo3Mu", "../flatNano/dataframes_2021Oct26_prepared/data_trigger.root")


  
  for var_name, bins in binning.items(): 
    eff_histo = getEffHisto(df, var_name, bins, cuts)


if __name__ == '__main__':
  ROOT.gROOT.SetBatch()
  main()
