leading = '((mu1pt)*(mu1pt > mu2pt & mu1pt > kpt) + (mu2pt)*(mu2pt > mu1pt & mu2pt > kpt) + (kpt)*(kpt > mu2pt & kpt > mu1pt))'
trailing = '((mu1pt)*(mu1pt < mu2pt & mu1pt < kpt) + (mu2pt)*(mu2pt < mu1pt & mu2pt < kpt) + (kpt)*(kpt < mu2pt & kpt < mu1pt))'
subleading = '((mu1pt)*(mu1pt != '+leading+' && mu1pt != '+trailing+') + (mu2pt)*(mu2pt != '+leading+' && mu2pt != '+trailing+') + (kpt)*(kpt != '+leading+' && kpt != '+trailing+'))'
prepreselection_3mu = ' & '.join([
   leading +' > 6',
    subleading +' > 4',
    trailing + ' > 4',
    'abs(mu1eta)<1.3',
    'abs(mu2eta)<1.3', 
    #'abs(keta)<1.3',
    #   'bvtx_svprob>1e-4',
    'jpsivtx_svprob>1.1e-1',
    'mu1_mediumID>0.5',
    'mu2_mediumID>0.5',
    'dr12>0.01',
    'dr13>0.01',
    'dr23>0.01',
    'abs(mu1_dz-mu2_dz)<0.2',
    'abs(mu1_dz-k_dz)<0.2',
    'abs(mu2_dz-k_dz)<0.2',
    'abs(k_dxy)<0.05',
    'abs(mu1_dxy)<0.05',
    'abs(mu2_dxy)<0.05',
     #'k_mediumID>0.5',
    'k_softMvaId>0.5',
    'k_raw_db_corr_iso03_rel<0.2',
    'jpsi_pt>6.9', 
    'jpsi_mass>2.9',
    'jpsi_mass<3.3',
    'jpsivtx_cos2D>0.95'
])


prepreselection_had = ' & '.join([
    'mu1pt > 4',
    'mu2pt> 4',
    'kpt>1.2',
    'abs(mu1eta)<1.4',
    'abs(mu2eta)<1.4',
    'jpsivtx_svprob>1.1e-1',
    'mu1_mediumID>0.5',
    'mu2_mediumID>0.5',
    'dr12>0.01',
    'dr13>0.01',
    'dr23>0.01',
    'abs(mu1_dz-mu2_dz)<0.2',
    'abs(mu1_dz-k_dz)<0.2',
    'abs(mu2_dz-k_dz)<0.2',
    'abs(mu1_dxy)<0.05',
    'abs(mu2_dxy)<0.05',
    'jpsi_pt>6.9',                                                                        
    'jpsivtx_cos2D>0.9',
    'k_d0sig>2',
    'jpsi_mass>2.9',
    'jpsi_mass<3.3',
    'jpsivtx_lxy_sig>3',
    'Bmass>5', 
    'Bmass<5.6'
])




#prepreselection = ' && '.join([
#    'mu1pt>6',
#    'mu2pt>4',
#    'kpt>4',
#    'abs(keta)<2.5',
#    'abs(mu1eta)<2.5',
#    'abs(mu2eta)<2.5',
#    'bvtx_svprob>1e-4',
#    'jpsivtx_svprob>1e-2',
#    'mu1_mediumID>0.5',
#    'mu2_mediumID>0.5',
#    'k_mediumID>0.5',
#])

#prepreselection = ' & '.join([
#    'mu1pt>6',
#])
triggerselection = ' & '.join([
    'mu1_isFromMuT > 0.5',
    'mu2_isFromMuT>0.5',
    'mu1_isFromJpsi_MuT>0.5',
    'mu2_isFromJpsi_MuT>0.5',
    'k_isFromMuT>0.5',
])

etaselection = '(((((abs(mu1eta)<1) & (abs(mu2eta)>1)) || ((abs(mu1eta)>1) & (abs(mu2eta)<1))) & (abs(jpsivtx_fit_mass-3.0969)<0.07)) || ((abs(mu1eta)<1) & (abs(mu2eta)<1) & (abs(jpsivtx_fit_mass-3.0969)<0.05)) || ((abs(mu1eta)>1) & (abs(mu2eta)>1) & (abs(jpsivtx_fit_mass-3.0969)<0.1)))'


#preselection = ' & '.join([prepreselection, triggerselection, etaselection, 'Bmass<6.3 & Q_sq>5.5'])
#preselection = ' & '.join([prepreselection, etaselection, 'Bmass<6.3 & Q_sq>5.5'])
preselection = ' & '.join([prepreselection_3mu, etaselection])#, 'Bmass<6.3'])
preselection_had = ' & '.join([prepreselection_had, 'abs(jpsi_mass-3.069)<0.12'])#, 'Bmass<6.3'])   
#preselection_mc = ' & '.join([preselection, 'abs(k_genpdgId)==13'])
#preselection = prepreselection

#preselection_hm = ' & '.join([prepreselection, triggerselection, etaselection, 'Bmass>6.3'])
#preselection_hm = ' & '.join([prepreselection,  etaselection, 'Bmass>6.3'])
#preselection_hm_mc = ' & '.join([preselection_hm, 'abs(k_genpdgId)==13'])


#pass_id = 'k_mediumID>0.5 & k_raw_db_corr_iso03_rel<0.2'
#pass_id = 'k_mediumID>0.5'
pass_id = 'k_raw_db_corr_iso03_rel<0.2'
#pass_id = 'k_softMvaId>0.5 & k_raw_db_corr_iso03_rel<0.2'
fail_id = '(!(%s))' % pass_id
#fail_id = 'k_mediumID<0.5'
