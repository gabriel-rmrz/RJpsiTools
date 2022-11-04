
import ROOT
from ROOT import TTree, TEfficiency
ROOT.gROOT.SetBatch()
from pyspark.ml.feature import Bucketizer
from array import array

def main():
   cuts_den = ' & '.join([
       'mu1pt > 5.',
       'mu2pt > 5.'
       ])
   cuts_num = ' & '.join([
     cuts_den,
     'mu1_isFromJpsi_MuT > 0.',
     'mu2_isFromJpsi_MuT > 0.',
     'k_isFromJpsi_MuT > 0.'
     ])
   
   bins_pt = array('d',[3.25, 3.5, 3.75, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0])
   #bins_pt = [3.25, 3.5, 3.75, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
   bins_eta = [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4] 
   abseta = [0.0, 0.9, 1.2, 2.4]
   
   
   
   var_names= 'Bpt' #TODO:Change this variable into an array
   #TODO: Add the arrays for the binning and ranges.
   df = ROOT.RDataFrame("BTo3Mu", "/home/users/sanchez/RPJpsi/scale_factors/orthogonal/RJpsiTools/flatNano/dataframes_2021Oct26_prepared/data_trigger.root")
   
   selection = ' & '.join([
         'Bpt > 0.0',
               'Bmass > 0.0'
                       ])
   
   nBins = 20
   

   
   histo_den = df.Filter(cuts_den).Histo1D((var_names, '', len(bins_pt) -1, bins_pt), var_names)
   histo_num = df.Filter(cuts_num).Histo1D((var_names, '', len(bins_pt) -1, bins_pt), var_names)
   
   print(type(histo_den))
   print(type(histo_num))

   eff_pt = TEfficiency(histo_num.GetPtr(), histo_den.GetPtr())

   #histo_den = df.Filter(cuts_den).Histo1D((var_names, '', 64, 0., 40.), var_names)
   #histo_num = df.Filter(cuts_num).Histo1D((var_names, '', 64, 0., 40.), var_names)
   c1 = ROOT.TCanvas('c1', '', 800, 800)
   
   histo_den.Draw('e')
   c1.SaveAs('histo_den.pdf')
   histo_num.Draw('e')
   c1.SaveAs('histo_num.pdf')

   eff_pt.SetStatisticOption(TEfficiency.kFCP)
   eff_pt.SetTitle(';'.join(['','Bc_pT', 'HLT efficiency']))
   eff_pt.Draw()
   ROOT.gPad.Update()

   eff_pt.GetPaintedGraph().GetYaxis().SetRangeUser(0., 1.05)
   eff_pt.GetPaintedGraph().GetXaxis().SetLabelSize(0.04)
   eff_pt.GetPaintedGraph().GetYaxis().SetLabelSize(0.04)
   eff_pt.GetPaintedGraph().GetXaxis().SetTitleSize(0.04)
   eff_pt.GetPaintedGraph().GetYaxis().SetTitleSize(0.04)
   eff_pt.GetPaintedGraph().GetXaxis().SetTitleOffset(1.2)
   eff_pt.GetPaintedGraph().GetYaxis().SetTitleOffset(1.2)
   ROOT.gPad.Update()
   c1.SaveAs('eff_pt.pdf')



if __name__ == '__main__':
  main()
