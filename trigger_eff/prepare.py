'''
This script cleans the flat nano aods:
- cancels Bc events in the Hb samples (to avoid overlapping)
- Only considers the 3Mu triggers, to make the computation of the analysis faster.
'''
import os
from root_pandas import read_root
from root_pandas import to_root

do_data = True
do_mc_mix = False
do_mc_hb = False

sufix='_merged_v11' 

dfdir = '../flatNano/dataframes_2023Jan25'
path_hb =  dfdir + '/HbToJPsiMuMu_ptmax'+sufix+'.root'
path_hb3mu =  dfdir + '/HbToJPsiMuMu_3MuFilter'+sufix+'.root'
path_data =  dfdir + '/data_ptmax'+sufix+'.root'
path_bc =  dfdir 
out_dir = dfdir + '_prepared' 

#ref_trigger_sel = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT'
#ref_trigger_sel = '(mu1_isDimuon0_jpsi_Trg & mu2_isDimuon0_jpsi_Trg) | (mu1_isDimuon43_jpsi_displaced_Trg & mu1_isDimuon43_jpsi_displaced_Trg)'
ref_trigger_sel = 'mu1_isDimuon0_jpsi_Trg & mu2_isDimuon0_jpsi_Trg & HLT_Dimuon0_Jpsi_NoVertexing '

sample_names = ['data']
if do_mc_mix:
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



if do_mc_hb:
    print("######################################")
    print("#### Clean Hb ########################")
    print("######################################")

    #clean from trigger and from bc
    df_3Mu_hb = read_root(path_hb,'BTo3Mu',where = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree=True)
    df_2MuP_hb = read_root(path_hb,'BTo2MuP',where = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree=True)
    df_2Mu3P_hb = read_root(path_hb,'BTo2Mu3P',where = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree = True)
    # Save Hb again
    df_3Mu_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo3Mu')
    df_2MuP_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo2MuP', mode='a')
    df_2Mu3P_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo2Mu3P', mode='a')

    print("######################################")
    print("#### Clean Hb 3Mu Filter ############")
    print("######################################")
    
    #clean from trigger and from bc
    df_3Mu_hbmu = read_root(path_hb3mu,'BTo3Mu',where = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree=True)
    df_2MuP_hbmu = read_root(path_hb3mu,'BTo2MuP',where = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree=True)
    df_2Mu3P_hbmu = read_root(path_hb3mu,'BTo2Mu3P',where = ref_trigger_sel + ' & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)', warn_missing_tree=True)
    
    # Save it again
    df_3Mu_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo3Mu')
    df_2MuP_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo2MuP', mode='a')
    df_2Mu3P_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo2Mu3P', mode='a')

print("######################################")
print("#### Clean data and Bc ###############")
print("######################################")

for sample in sample_names:
    exit()
    if sample == 'data':
        path = path_data 
    else:
        path = path_bc + "/BcToJPsiMuMu_is_"+sample+sufix+".root"

    print("---- Reading BTo3Mu tree ----")
    df_3Mu = read_root(path,'BTo3Mu',where = ref_trigger_sel, warn_missing_tree=True)
    print("---- Reading BTo2MuP tree ----")
    df_2MuP = read_root(path,'BTo2MuP',where = ref_trigger_sel, warn_missing_tree=True)
    print("---- Reading BTo2Mu3P tree ----")
    df_2Mu3P = read_root(path,'BTo2Mu3P',where = ref_trigger_sel , warn_missing_tree=True)

    if sample == 'data':
        print("++++ Writing BTo3Mu tree ++++")
        df_3Mu.to_root(out_dir+'/data_trigger.root', key='BTo3Mu')
        print("++++ Writing BTo2MuP tree ++++")
        df_2MuP.to_root(out_dir+'/data_trigger.root', key='BTo2MuP', mode='a')
        print("++++ Writing BTo2Mu3P tree ++++")
        df_2Mu3P.to_root(out_dir+'/data_trigger.root', key='BTo2Mu3P', mode='a')
    else:
        print("++++ Writing BTo3Mu tree ++++")
        df_3Mu.to_root(out_dir+'/BcToJPsiMuMu_is_'+sample+'_trigger.root', key='BTo3Mu')
        print("++++ Writing BTo2MuP tree ++++")
        df_2MuP.to_root(out_dir+'/BcToJPsiMuMu_is_'+sample+'_trigger.root', key='BTo2MuP', mode='a')
        print("++++ Writing BTo2Mu3P tree ++++")
        df_2Mu3P.to_root(out_dir+'/BcToJPsiMuMu_is_'+sample+'_trigger.root', key='BTo2Mu3P', mode='a')
