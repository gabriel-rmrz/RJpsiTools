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
    df_hb = read_root(path_hb,'BTo3Mu',where = 'mu1_isFromMuT & mu2_isFromMuT & mu1_isFromJpsi_MuT & mu2_isFromJpsi_MuT & k_isFromMuT & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)')
    # Save Hb again
    df_hb.to_root(out_dir + "HbToJPsiMuMu_trigger_bcclean.root",key = 'BTo3Mu')

    print("######################################")
    print("#### Clean Hb 3Mu Filter ############")
    print("######################################")
    
    #clean from trigger and from bc
    df_hbmu = read_root(path_hb3mu,'BTo3Mu',where = 'mu1_isFromMuT & mu2_isFromMuT & mu1_isFromJpsi_MuT & mu2_isFromJpsi_MuT & k_isFromMuT & (abs(mu2_grandmother_pdgId) != 421 | abs(mu1_grandmother_pdgId) != 421)')
    
    # Save it again
    df_hbmu.to_root(out_dir + "/HbToJPsiMuMu_3MuFilter_trigger_bcclean.root",key = 'BTo3Mu')

print("######################################")
print("#### Clean data and Bc ###############")
print("######################################")

for sample in sample_names:
    if sample == 'data':
        path = path_data 
    else:
        path = path_bc + "BcToJPsiMuMu_is_"+sample+"_merged.root"

    df = read_root(path,'BTo3Mu',where = 'mu1_isFromDoubleMuT & mu2_isFromDoubleMuT & mu1_isFromJpsi_DoubleMuT & mu2_isFromJpsi_DoubleMuT ', warn_missing_tree=True)

    if sample == 'data':
        df.to_root(out_dir+'/data_trigger.root', key='BTo3Mu')
    else:
        df.to_root(out_dir+'BcToJPsiMuMu_is_'+sample+'trigger.root', key='BTo3Mu')



