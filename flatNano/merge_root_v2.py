#Script that merges the flat root files from the same collection
import os
import subprocess
import pandas as pd
from personal_settings import *
import ROOT
import math
from root_pandas import to_root, read_root

path_or = personal_tier_path+'dataframes_2023Feb09/'

#dataset = 'HbToJPsiMuMu_3MuFilter/'
#dataset = 'HbToJPsiMuMu/'
#dataset = 'BcToJPsiMuMu/'
dataset ='data/'

if not ("BcToJPsiMuMu") in dataset:
    flag_names = [''] # ['ptmax']

else:
    flag_names = ['is_jpsi_tau','is_jpsi_mu','is_jpsi_pi','is_psi2s_mu','is_chic0_mu','is_chic1_mu','is_chic2_mu','is_hc_mu','is_psi2s_tau','is_jpsi_3pi','is_jpsi_hc']
    #flag_names = ['is_jpsi_mu','is_jpsi_pi']
for flag in flag_names:
    path = path_or

    #Print the file names
    if ("BcToJPsiMuMu") in dataset:
        lsOut = subprocess.getoutput('ls ' + path + dataset + flag)
    else:
        lsOut = subprocess.getoutput('ls ' + path + dataset )
    #print(lsOut)
    files = lsOut.split('\n')
    
    print("%s files are going to be merged" %(len(files)))
    
    #we need to check that the first file that we put as Source is ok, otherwise the fnal merged fie will nto be ok (I know frome xperience, i.e. psi2s_tau)
    print ("path to file "+ path + dataset + flag)
    for file in files:
        #if '3m' in file:
        print ("file ", path + dataset + flag + '/' +file)
        #f = read_root(path + dataset + flag + '/' +file)
        f = read_root(path + dataset + flag + '/' +file, "BTo3Mu")
        #f = read_root(path + dataset + '/' +file,"BTo3Mu")
        #g = read_root(path + dataset + '/' +file,"BTo2Mu3P")
        if  math.isnan(f.jpsi_mass[0]):       
            print (f)
#        if not math.isnan(f.jpsi_mass[0]): 
        #if not math.isnan(f.jpsi_pt):          
            #if (not math.isnan(f.jpsi_mass[0])) and (not math.isnan(g.jpsi_mass[0])):
        else:
            first_file = file
            #break
    print ("moving "+ path + dataset + flag + '/' +first_file+' '+path + dataset+'.')
    tmp_folder= path + dataset + flag + '/tmp/'
    #os.system('mkdir -p '+ tmp_folder)
    print ("moving "+ path + dataset + flag + '/' +first_file+' '+tmp_folder)   
    #os.system('mv '+ path + dataset + flag + '/' +first_file+' '+tmp_folder)
    print ("hadding -k -n 100 "+ path + dataset.strip('/') + '_'+flag + '_merged_v11_3Mu.root '+tmp_folder+ first_file +' '+path + dataset + flag + '/*.root')
    #os.system('hadd -k -n 100 '+ path + dataset.strip('/') + '_'+flag + '_merged_v11_3Mu.root '+tmp_folder+ first_file +' '+path + dataset + flag + '/*.root')        
    print ("moving " +tmp_folder+ first_file +' ' + path + dataset + flag+'/' )
    #os.system('mv '+tmp_folder+ first_file +' ' + path + dataset + flag+'/' )
    #os.sytem('rm '+ tmp_folder)
