'''
This script cleans the flat nano aods:
- cancels Bc events in the Hb samples (to avoid overlapping)
- Only considers the 3Mu triggers, to make the computation of the analysis faster.
'''
import os
from root_pandas import read_root
from root_pandas import to_root

only_data = True

wdir = '/home/users/sanchez/RPJpsi/scale_factors/orthogonal/RJpsiTools/flatNano'
dfdir = 'dataframes_2021Oct26'
path_hb = wdir + '/' + dfdir + '/HbToJPsiMuMu_ptmax_merged.root'
path_hb3mu = wdir + '/' + dfdir + '/HbToJPsiMuMu_3MuFilter_ptmax_merged.root'
path_data = wdir + '/' + dfdir + '/data_ptmax_merged.root'
path_bc = wdir + '/' + dfdir 

out_dir = wdir + '/' + dfdir + '_prepared' 

sample_names = [
    'data'     
]

if not only_data:
    sample_names.extend([
        'jpsi_tau' ,
        'jpsi_mu'  ,
        'chic0_mu' ,
        'chic1_mu' ,
        'chic2_mu' ,
        'jpsi_hc'  ,
        'hc_mu'    ,
        'psi2s_mu' ,
        'psi2s_tau'
    ])
    
if not os.path.exists(out_dir):
    os.makedirs(out_dir)



if not only_data:
    print("######################################")
    print("#### Clean Hb ########################")
    print("######################################")
    #clean from trigger and from bc
    df_3Mu_hb = read_root(path_hb,'BTo3Mu',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT & (abs(mu2_grandmother_pdgId) != 421 |
        abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree)
    df_2MuP_hb = read_root(path_hb,'BTo2MuP',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT & (abs(mu2_grandmother_pdgId) != 421 |
        abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree)
    df_2Mu3P_hb = read_root(path_hb,'BTo2Mu3P',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT & (abs(mu2_grandmother_pdgId) != 421 |
        abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree)
    # Save Hb again
    df_3Mu_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo3Mu')
    df_2MuP_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo2MuP', mode='a')
    df_2Mu3P_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo2Mu3P', mode='a')

    print("######################################")
    print("#### Clean Hb 3Mu Filter ############")
    print("######################################")
    
    #clean from trigger and from bc
    df_3Mu_hbmu = read_root(path_hb3mu,'BTo3Mu',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree)
    df_2MuP_hbmu = read_root(path_hb3mu,'BTo2MuP',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree)
    df_2Mu3P_hbmu = read_root(path_hb3mu,'BTo2Mu3P',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree)
    
    # Save it again
    df_3Mu_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo3Mu')
    df_2MuP_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo2MuP', mode='a')
    df_2Mu3P_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo2Mu3P', mode='a')

print("######################################")
print("#### Clean data and Bc ###############")
print("######################################")

for sample in sample_names:
    if sample == 'data':
        path = path_data 
    else:
        path = path_bc + "BcToJPsiMuMu_is_"+sample+"_merged.root"

    print("---- Reading BTo3Mu tree ----")
    df_3Mu = read_root(path,'BTo3Mu',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT ', warn_missing_tree=True)
    print("---- Reading BTo2MuP tree ----")
    df_2MuP = read_root(path,'BTo2MuP',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT ', warn_missing_tree=True)
    print("---- Reading BTo2Mu3P tree ----")
    df_2Mu3P = read_root(path,'BTo2Mu3P',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT ', warn_missing_tree=True)

    if sample == 'data':
        print("++++ Writing BTo3Mu tree ++++")
        df_3Mu.to_root(out_dir+'/data_trigger.root', key='BTo3Mu')
        print("++++ Writing BTo2MuP tree ++++")
        df_2MuP.to_root(out_dir+'/data_trigger.root', key='BTo2MuP', mode='a')
        print("++++ Writing BTo2Mu3P tree ++++")
        df_2Mu3P.to_root(out_dir+'/data_trigger.root', key='BTo2Mu3P', mode='a')
    else:
        df.to_root(out_dir+'BcToJPsiMuMu_is_'+sample+'trigger.root', key='BTo3Mu')



