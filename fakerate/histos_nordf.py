import ROOT
import numpy as np

histos = dict()   
            
histos['mu1pt'                     ] = ['mu1pt'                     , '', 50,      0,    40, '#mu_{1} p_{T} (GeV)']                                           
histos['mu2pt'                     ] = ['mu2pt'                     , '', 50,      0,    20, '#mu_{2} p_{T} (GeV)']                                           
histos['kpt'                       ] = ['kpt'                       , '', 50,      0,    30, '#mu_{3} p_{T} (GeV)']                                           
histos['mu1phi'                    ] = ['mu1phi'                    , '', 20, -np.pi, np.pi, '#mu_{1} #phi'       ]                                                  
histos['mu2phi'                    ] = ['mu2phi'                    , '', 20, -np.pi, np.pi, '#mu_{1} #phi'       ]                                                 
histos['kphi'                      ] = ['kphi'                      , '', 20, -np.pi, np.pi, '#mu_{1} #phi'       ]                                                
histos['mu1eta'                    ] = ['mu1eta'                    , '', 30,     -3,     3, '#mu_{1} #eta'       ]                                               
histos['mu2eta'                    ] = ['mu2eta'                    , '', 30,     -3,     3, '#mu_{1} #eta'       ]                                              
histos['keta'                      ] = ['keta'                      , '', 30,     -3,     3, '#mu_{1} #eta'       ]                                              
histos['Bpt'                       ] = ['Bpt'                       , '', 50,      0,    50, '3#mu p_{T} (GeV)'   ]                                              
histos['Bmass'                     ] = ['Bmass'                     , '', 60,      3,    10, '3#mu mass (GeV)'    ]                                               
histos['m12'                     ] = ['m12'                     , '', 100,      2.5,    3.5, 'm12 (GeV)'    ]                                               
histos['m13'                     ] = ['m13'                     , '', 100,      2.5,    3.5, 'm13 (GeV)'    ]                                               
histos['m23'                     ] = ['m23'                     , '', 100,      2.5,    3.5, 'm23 (GeV)'    ]                                               
histos['Beta'                      ] = ['Beta'                      , '', 30,     -3,     3, '3#mu eta' ]                                                     
histos['Bphi'                      ] = ['Bphi'                      , '', 20, -np.pi, np.pi, '3#mu #phi']                                                     
histos['Bpt_reco'                  ] = ['Bpt_reco'                  , '', 50,      0,    80, 'corrected 3#mu p_{T} (GeV)']                                    
histos['abs_mu1_dxy'               ] = ['mu1_dxy'                   , '', 50,      0,   0.2, '#mu_{1} |d_{xy}| (cm)']                                         
histos['mu1_dxy_sig'               ] = ['mu1_dxy_sig'               , '', 50,      0,    10, '#mu_{1} |d_{xy}|/#sigma_{d_{xy}}']
histos['abs_mu2_dxy'               ] = ['mu2_dxy'                   , '', 50,      0,   0.2, '#mu_{2} |d_{xy}| (cm)']                                         
histos['mu2_dxy_sig'               ] = ['mu2_dxy_sig'               , '', 50,      0,    10, '#mu_{2} |d_{xy}|/#sigma_{d_{xy}}' ]                             
histos['abs_k_dxy'                 ] = ['k_dxy'                     , '', 50,      0,   0.2, '#mu_{3} |d_{xy}| (cm)']                                         
histos['k_dxy_sig'                 ] = ['k_dxy_sig'                 , '', 50,      0,    10, '#mu_{3} |d_{xy}|/#sigma_{d_{xy}}'  ]                            
histos['abs_mu1_dz'                ] = ['mu1_dz'                    , '', 50,      0,   0.4, '#mu_{1} |d_{z}| (cm)']                                          
histos['mu1_dz_sig'                ] = ['mu1_dz_sig'                , '', 50,      0,    10, '#mu_{1} |d_{z}|/#sigma_{d_{z}}'     ]                           
histos['abs_mu2_dz'                ] = ['mu2_dz'                    , '', 50,      0,   0.4, '#mu_{2} |d_{z}| (cm)']                                          
histos['mu2_dz_sig'                ] = ['mu2_dz_sig'                , '', 50,      0,    10, '#mu_{2} |d_{z}|/#sigma_{d_{z}}'     ]                           
histos['abs_k_dz'                  ] = ['k_dz'                      , '', 50,      0,   0.4, '#mu_{3} |d_{z}| (cm)']                                          
histos['k_dz_sig'                  ] = ['k_dz_sig'                  , '', 50,      0,    10, '#mu_{3} |d_{z}|/#sigma_{d_{z}}'     ]                           
#histos['Blxy_sig'                  ] = ['Blxy_sig'                  , '', 50,      0,    60, 'L_{xy}/#sigma_{L_{xy}}']                                        
#histos['Blxy'                      ] = ['Blxy'                      , '',100,      0,     2, 'L_{xy} (cm)']                                                   
#histos['Blxy_unc'                  ] = ['Blxy_unc'                  , '',100,      0,  0.02, '#sigma_{L_{xy}} (cm)']                                          
#histos['Bsvprob'                   ] = ['Bsvprob'                   , '', 50,      0,     1, 'vtx(#mu_{1}, #mu_{2}, #mu_{3}) probability'                    ]
histos['bvtx_chi2'                 ] = ['bvtx_chi2'                 , '', 50,      0,    50, 'vtx(#mu_{1}, #mu_{2}, #mu_{3}) #chi^{2}']                       
histos['bvtx_lxy'                  ] = ['bvtx_lxy'                  , '',100,      0,     2, 'L_{xy} (cm)']                                                   
histos['bvtx_lxy_sig'              ] = ['bvtx_lxy_sig'              , '', 50,      0,    60, 'L_{xy}/#sigma_{L_{xy}}'                  ]                      
histos['bvtx_lxy_unc'              ] = ['bvtx_lxy_unc'              , '', 60,      0,  0.02, '#sigma_{L_{xy}} (cm)']                                          
#histos['bvtx_lxy_sig_corr'         ] = ['bvtx_lxy_sig_corr'         , '', 50,      0,    60, 'corrected L_{xy}/#sigma_{L_{xy}}'         ]                     
#histos['bvtx_lxy_unc_corr'         ] = ['bvtx_lxy_unc_corr'         , '', 60,      0,  0.02, 'corrected #sigma_{L_{xy}} (cm)']                                
#histos['bvtx_log10_lxy_sig_corr'   ] = ['bvtx_log10_lxy_sig_corr'   , '', 51,     -2,     2, 'corrected log_{10} vtx(#mu_{1}, #mu_{2}, #mu_{3}) L_{xy}/#sigma_{L_{xy}}']
histos['bvtx_svprob'               ] = ['bvtx_svprob'               , '', 50,      0,     1, 'vtx(#mu_{1}, #mu_{2}, #mu_{3}) probability'                    ]
#histos['bvtx_log10_svprob'         ] = ['bvtx_log10_svprob'         , '', 51,     -8,     1, 'log_{10} vtx(#mu_{1}, #mu_{2}, #mu_{3}) probability'           ]
#histos['bvtx_log10_lxy'            ] = ['bvtx_log10_lxy'            , '', 51,     -4,     1, 'log_{10} vtx(#mu_{1}, #mu_{2}, #mu_{3}) L_{xy}'                ]
#histos['bvtx_log10_lxy_sig'        ] = ['bvtx_log10_lxy_sig'        , '', 51,     -2,     2, 'log_{10} vtx(#mu_{1}, #mu_{2}, #mu_{3}) L_{xy}/#sigma_{L_{xy}}']
histos['bvtx_cos2D'                ] = ['bvtx_cos2D'                , '',100,    0.9,     1, '2D cos#alpha'                                                  ]
histos['jpsivtx_chi2'              ] = ['jpsivtx_chi2'              , '', 50,      0,    50, 'vtx(#mu_{1}, #mu_{2}) #chi^{2}'                                ]
histos['jpsivtx_lxy_sig'           ] = ['jpsivtx_lxy_sig'           , '', 50,      0,    60, 'L_{xy}/#sigma_{L_{xy}}'                                        ]
histos['jpsivtx_lxy'               ] = ['jpsivtx_lxy'               , '',100,      0,     2, 'L_{xy} (cm)']                                                   
histos['jpsivtx_lxy_unc'           ] = ['jpsivtx_lxy_unc'           , '', 60,      0,  0.02, '#sigma_{L_{xy}} (cm)']                                          
#histos['jpsivtx_lxy_unc_corr'      ] = ['jpsivtx_lxy_unc_corr'      , '', 60,      0,  0.02, 'corrected #sigma_{L_{xy}} (cm)']                                          
#histos['jpsivtx_lxy_sig_corr'      ] = ['jpsivtx_lxy_sig_corr'      , '', 50,      0,    60, 'corrected L_{xy}/#sigma_{L_{xy}}'                               ]         
#histos['jpsivtx_log10_lxy_sig_corr'] = ['jpsivtx_log10_lxy_sig_corr', '', 51,     -2,     2, 'corrected log_{10} vtx(#mu_{1}, #mu_{2}) L_{xy}/#sigma_{L_{xy}}' ]        
histos['jpsivtx_svprob'            ] = ['jpsivtx_svprob'            , '', 50,      0,     1, 'vtx(#mu_{1}, #mu_{2}) probability'                             ]
#histos['jpsivtx_log10_svprob'      ] = ['jpsivtx_log10_svprob'      , '', 51,     -8,     1, 'log_{10} vtx(#mu_{1}, #mu_{2}) probability'                    ]
#histos['jpsivtx_log10_lxy'         ] = ['jpsivtx_log10_lxy'         , '', 51,     -4,     1, 'log_{10} vtx(#mu_{1}, #mu_{2}) L_{xy}'                         ]
#histos['jpsivtx_log10_lxy_sig'     ] = ['jpsivtx_log10_lxy_sig'     , '', 51,     -2,     2, 'log_{10} vtx(#mu_{1}, #mu_{2}) L_{xy}/#sigma_{L_{xy}}'         ]
histos['jpsivtx_cos2D'             ] = ['jpsivtx_cos2D'             , '',100,    0.9,     1, '2D cos#alpha'                                                  ]

histos['m_miss_sq'                 ] = ['m_miss_sq'                 , '', 50,      0,    9, 'm^{2}_{miss} (GeV^{2})']                                        
#histos['m2missjpsik'               ] = ['m2missjpsik'               , '', 50,      0,    12, 'm^{2}_{miss} (GeV^{2})']                                        
#histos['m2missjpsipi'              ] = ['m2missjpsipi'              , '', 50,      0,    12, 'm^{2}_{miss} (GeV^{2})']                                        
# histos['Q_sq'                      ] = ['Q_sq'                      , '', 50,      0,    12, 'q^{2} (GeV^{2})']                                               
histos['Q_sq'                      ] = ['Q_sq'                      , '', 24,      3,    10.5, 'q^{2} (GeV^{2})']                                               
#histos['Q_sq'                      ] = ['Q_sq'                      , '', 24,      -50,    50, 'q^{2} (GeV^{2})']                                               
#histos['Q_sq'                      ] = ['Q_sq'                      , '', 24,      4.5,    10.5, 'q^{2} (GeV^{2})']                                               
#histos['q2jpsik'                   ] = ['q2jpsik'                   , '', 50,      0,    12, 'q^{2} (GeV^{2})']                                               
#histos['q2jpsipi'                  ] = ['q2jpsipi'                  , '', 50,      0,    12, 'q^{2} (GeV^{2})']                                               
histos['pt_var'                    ] = ['pt_var'                    , '', 50,      0,    50, 'p_{T}^{var} (GeV)']                                             
histos['pt_miss_vec'               ] = ['pt_miss_vec'               , '', 50,      0,    50, 'vector p_{T}^{miss} (GeV)']                                     
histos['pt_miss_scal'              ] = ['pt_miss_scal'              , '', 60,    -10,    50, 'scalar p_{T}^{miss} (GeV)']                                     
histos['E_mu_star'                 ] = ['E_mu_star'                 , '', 50,      0.3,   2.3, 'E_{#mu_{3}}* (GeV)']                                            
histos['E_mu_canc'                 ] = ['E_mu_canc'                 , '', 50,      0,     6, 'E_{#mu_{3}}^{#} (GeV)']                                         
histos['mu1_mediumID'              ] = ['mu1_mediumID'              , '',  2,      0,     2, '#mu_{1} mediumID'                                              ]
histos['mu2_mediumID'              ] = ['mu2_mediumID'              , '',  2,      0,     2, '#mu_{2} mediumID'                                              ]
histos['k_mediumID'                ] = ['k_mediumID'                , '',  2,      0,     2, '#mu_{3} mediumID'                                              ]
histos['mu1_tightID'               ] = ['mu1_tightID'               , '',  2,      0,     2, '#mu_{1} tightID'                                               ]
histos['mu2_tightID'               ] = ['mu2_tightID'               , '',  2,      0,     2, '#mu_{2} tightID'                                               ]
histos['k_tightID'                 ] = ['k_tightID'                 , '',  2,      0,     2, '#mu_{3} tightID'                                               ]
histos['mu1_softID'                ] = ['mu1_softID'                , '',  2,      0,     2, '#mu_{1} softID'                                                ]
histos['mu2_softID'                ] = ['mu2_softID'                , '',  2,      0,     2, '#mu_{2} softID'                                                ]
histos['k_softID'                  ] = ['k_softID'                  , '',  2,      0,     2, '#mu_{3} softID'                                                ]
histos['b_iso03'                   ] = ['b_iso03'                   , '', 50,      0,    20, '3-#mu bpark I^{abs}_{R=0.3}'                                   ]
histos['b_iso04'                   ] = ['b_iso04'                   , '', 50,      0,    20, '3-#mu bpark I^{abs}_{R=0.4}'                                   ]
histos['k_iso03'                   ] = ['k_iso03'                   , '', 50,      0,    20, '#mu_{3} bpark I^{abs}_{R=0.3}'                                 ]
histos['k_iso04'                   ] = ['k_iso04'                   , '', 50,      0,    20, '#mu_{3} bpark I^{abs}_{R=0.4}'                                 ]
histos['mu1_iso03'                 ] = ['mu1_iso03'                 , '', 50,      0,    20, '#mu_{1} bpark I^{abs}_{R=0.3}'                                 ]
histos['mu1_iso04'                 ] = ['mu1_iso04'                 , '', 50,      0,    20, '#mu_{1} bpark I^{abs}_{R=0.4}'                                 ]
histos['mu2_iso03'                 ] = ['mu2_iso03'                 , '', 50,      0,    20, '#mu_{2} bpark I^{abs}_{R=0.3}'                                 ]
histos['mu2_iso04'                 ] = ['mu2_iso04'                 , '', 50,      0,    20, '#mu_{2} bpark I^{abs}_{R=0.4}'                                 ]
histos['k_raw_db_corr_iso03'       ] = ['k_raw_db_corr_iso03'       , '', 50,      0,    20, '#mu_{3} #Delta#beta-corr. I^{abs}_{R=0.3}'                     ]
histos['k_raw_db_corr_iso04'       ] = ['k_raw_db_corr_iso04'       , '', 50,      0,    20, '#mu_{3} #Delta#beta-corr. I^{abs}_{R=0.4}'                     ]
histos['k_raw_ch_pfiso03'          ] = ['k_raw_ch_pfiso03'          , '', 50,      0,    20, '#mu_{3} PF charged I^{abs}_{R=0.3}'                            ]
histos['k_raw_ch_pfiso04'          ] = ['k_raw_ch_pfiso04'          , '', 50,      0,    20, '#mu_{3} PF charged I^{abs}_{R=0.4}'                            ]
histos['k_raw_n_pfiso03'           ] = ['k_raw_n_pfiso03'           , '', 50,      0,    20, '#mu_{3} PF neutral I^{abs}_{R=0.3}'                            ]
histos['k_raw_n_pfiso04'           ] = ['k_raw_n_pfiso04'           , '', 50,      0,    20, '#mu_{3} PF neutral I^{abs}_{R=0.4}'                            ]
histos['k_raw_pho_pfiso03'         ] = ['k_raw_pho_pfiso03'         , '', 50,      0,    20, '#mu_{3} PF #gamma I^{abs}_{R=0.3}'                             ]
histos['k_raw_pho_pfiso04'         ] = ['k_raw_pho_pfiso04'         , '', 50,      0,    20, '#mu_{3} PF #gamma I^{abs}_{R=0.4}'                             ]
histos['k_raw_pu_pfiso03'          ] = ['k_raw_pu_pfiso03'          , '', 50,      0,    20, '#mu_{3} PF PU I^{abs}_{R=0.3}'                                 ]
histos['k_raw_pu_pfiso04'          ] = ['k_raw_pu_pfiso04'          , '', 50,      0,    20, '#mu_{3} PF PU I^{abs}_{R=0.4}'                                 ]
histos['k_raw_trk_iso03'           ] = ['k_raw_trk_iso03'           , '', 50,      0,    20, '#mu_{3} track I^{abs}_{R=0.3}'                                 ]
histos['k_raw_trk_iso05'           ] = ['k_raw_trk_iso05'           , '', 50,      0,    20, '#mu_{3} track I^{abs}_{R=0.5}'                                 ]
# histos['raw_rho_corr_iso03'        ] = ['raw_rho_corr_iso03'        , '', 50,      0,    20, '#mu_{1} I^{abs}_{R=0.3}'                                      ]           
# histos['raw_rho_corr_iso04'        ] = ['raw_rho_corr_iso04'        , '', 50,      0,    20, '#mu_{1} I^{abs}_{R=0.4}'                                       ]          

histos['b_iso03_rel'               ] = ['b_iso03_rel'               , '', 50,      0,     2, '3-#mu bpark I^{rel}_{R=0.3}'                                   ]
histos['b_iso04_rel'               ] = ['b_iso04_rel'               , '', 50,      0,     2, '3-#mu bpark I^{rel}_{R=0.4}'                                   ]
histos['k_iso03_rel'               ] = ['k_iso03_rel'               , '', 50,      0,     2, '#mu_{3} bpark I^{rel}_{R=0.3}'                                 ]
histos['k_iso04_rel'               ] = ['k_iso04_rel'               , '', 50,      0,     2, '#mu_{3} bpark I^{rel}_{R=0.4}'                                 ]
histos['mu1_iso03_rel'             ] = ['mu1_iso03_rel'             , '', 50,      0,     2, '#mu_{1} bpark I^{rel}_{R=0.3}'                                 ]
histos['mu1_iso04_rel'             ] = ['mu1_iso04_rel'             , '', 50,      0,     2, '#mu_{1} bpark I^{rel}_{R=0.4}'                                 ]
histos['mu2_iso03_rel'             ] = ['mu2_iso03_rel'             , '', 50,      0,     2, '#mu_{2} bpark I^{rel}_{R=0.3}'                                 ]
histos['mu2_iso04_rel'             ] = ['mu2_iso04_rel'             , '', 50,      0,     2, '#mu_{2} bpark I^{rel}_{R=0.4}'                                 ]
histos['k_raw_db_corr_iso03_rel'   ] = ['k_raw_db_corr_iso03_rel'   , '', 50,      0,     2, '#mu_{3} #Delta#beta-corr. I^{rel}_{R=0.3}'                     ]
histos['k_raw_db_corr_iso04_rel'   ] = ['k_raw_db_corr_iso04_rel'   , '', 50,      0,     2, '#mu_{3} #Delta#beta-corr. I^{rel}_{R=0.4}'                     ]
histos['k_raw_ch_pfiso03_rel'      ] = ['k_raw_ch_pfiso03_rel'      , '', 50,      0,     2, '#mu_{3} PF charged I^{rel}_{R=0.3}'                            ]
histos['k_raw_ch_pfiso04_rel'      ] = ['k_raw_ch_pfiso04_rel'      , '', 50,      0,     2, '#mu_{3} PF charged I^{rel}_{R=0.4}'                            ]
histos['k_raw_n_pfiso03_rel'       ] = ['k_raw_n_pfiso03_rel'       , '', 50,      0,     2, '#mu_{3} PF neutral I^{rel}_{R=0.3}'                            ]
histos['k_raw_n_pfiso04_rel'       ] = ['k_raw_n_pfiso04_rel'       , '', 50,      0,     2, '#mu_{3} PF neutral I^{rel}_{R=0.4}'                            ]
histos['k_raw_pho_pfiso03_rel'     ] = ['k_raw_pho_pfiso03_rel'     , '', 50,      0,     2, '#mu_{3} PF #gamma I^{rel}_{R=0.3}'                             ]
histos['k_raw_pho_pfiso04_rel'     ] = ['k_raw_pho_pfiso04_rel'     , '', 50,      0,     2, '#mu_{3} PF #gamma I^{rel}_{R=0.4}'                             ]
histos['k_raw_pu_pfiso03_rel'      ] = ['k_raw_pu_pfiso03_rel'      , '', 50,      0,     2, '#mu_{3} PF PU I^{rel}_{R=0.3}'                                 ]
histos['k_raw_pu_pfiso04_rel'      ] = ['k_raw_pu_pfiso04_rel'      , '', 50,      0,     2, '#mu_{3} PF PU I^{rel}_{R=0.4}'                                 ]
histos['k_raw_trk_iso03_rel'       ] = ['k_raw_trk_iso03_rel'       , '', 50,      0,     2, '#mu_{3} track I^{rel}_{R=0.3}'                                 ]
histos['k_raw_trk_iso05_rel'       ] = ['k_raw_trk_iso05_rel'       , '', 50,      0,     2, '#mu_{3} track I^{rel}_{R=0.5}'                                 ]
# histos['raw_rho_corr_iso03_rel   ' ] = ['raw_rho_corr_iso03_rel'    , '', 50,      0,     2, '#mu_{1} I^{rel}_{R=0.3}'                                      ] 
# histos['raw_rho_corr_iso04_rel   ' ] = ['raw_rho_corr_iso04_rel'    , '', 50,      0,     2, '#mu_{1} I^{rel}_{R=0.4}'                                       ]

histos['Bcharge'                   ] = ['Bcharge'                   , '',  3,     -1,     2, 'B charge'                                                      ]
# histos['mll_raw'                   ] = ['mll_raw'                   , '', 50,    2.5,   3.5, 'm(#mu_{1}, #mu_{2}) (GeV)']                                   ]  
histos['DR_mu1mu2'                 ] = ['DR_mu1mu2'                 , '', 50,      0,   1.2, '#DeltaR(#mu_{1}, #mu_{2})']                                     
# histos['jpsi_chi2'                 ] = ['jpsi_chi2'                 , '', 80,      0,  20. , 'vtx(#mu_{1}, #mu_{2}) #chi^{2}'                                ]
# histos['Bchi2'                     ] = ['b_chi2'                    , '', 80,      0,  35. , 'vtx(#mu_{1}, #mu_{2}, #mu_{3}) #chi^{2}'                       ]
histos['jpsi_mass'                 ] = ['jpsi_mass'                 , '', 50,    2.5,   3.5, 'm(#mu_{1}, #mu_{2}) (GeV)']                                     
histos['jpsi_pt'                   ] = ['jpsi_pt'                   , '', 50,      0,    50, '(#mu_{1}, #mu_{2}) p_{T} (GeV)']                                
histos['jpsi_eta'                  ] = ['jpsi_eta'                  , '', 30,     -3,     3, '(#mu_{1}, #mu_{2}) #eta'                                       ]
histos['jpsi_phi'                  ] = ['jpsi_phi'                  , '', 20, -np.pi, np.pi, '(#mu_{1}, #mu_{2}) #phi'                                       ]
histos['dr12'                      ] = ['dr12'                      , '', 50,      0,   1.2, '#DeltaR(#mu_{1}, #mu_{2})']                                     
histos['dr13'                      ] = ['dr13'                      , '', 50,      0,   1.2, '#DeltaR(#mu_{1}, #mu_{3})']                                     
histos['dr23'                      ] = ['dr23'                      , '', 50,      0,   1.2, '#DeltaR(#mu_{2}, #mu_{3})']                                     
#histos['dr_jpsi_mu'                ] = ['dr_jpsi_mu'                , '', 50,      0,   1.2, '#DeltaR(J/#Psi, #mu_{3})']                                      
#histos['maxdr'                     ] = ['maxdr'                     , '', 50,      0,   1.2, 'maximum #DeltaR(#mu_{i}, #mu_{j})']                             
#histos['mindr'                     ] = ['mindr'                     , '', 50,      0,   1.2, 'minimum #DeltaR(#mu_{i}, #mu_{j})']                             
# histos['bdt_mu'                    ] = ['bdt_mu'                    , '',100,      0,   1. , 'BDT score #mu'                                                 
# histos['bdt_tau'                   ] = ['bdt_tau'                   , '',100,      0,   1. , 'BDT score #tau'                                                
# histos['bdt_bkg'                   ] = ['bdt_bkg'                   , '',100,      0,   1. , 'BDT score bkg'                                                 
'''
histos['abs_mu1mu2_dz'             ] = ['abs_mu1mu2_dz'             , '',100,      0,   0.5, '|#mu_{1} d_{z} - #mu_{2} d_{z}| (cm)']                          
histos['abs_mu1k_dz'               ] = ['abs_mu1k_dz'               , '',100,      0,   0.5, '|#mu_{1} d_{z} - #mu_{3} d_{z}| (cm)']                          
histos['abs_mu2k_dz'               ] = ['abs_mu2k_dz'               , '',100,      0,   0.5, '|#mu_{2} d_{z} - #mu_{3} d_{z}| (cm)']                          
histos['jpsiK_pt'                  ] = ['jpsiK_pt'                  , '', 50,      0,    50, '(J/#Psi + K^{+}) p_{T} (GeV)']                                  
# histos['jpsiK_mass'                ] = ['jpsiK_mass'                , '', 80,      2,     7, '(J/#Psi + K^{+}) mass (GeV)']                                   
histos['jpsiK_mass'                ] = ['jpsiK_mass'                , '',100,      5,     6, '(J/#Psi + K^{+}) mass (GeV)']                                   
histos['jpsiK_eta'                 ] = ['jpsiK_eta'                 , '', 30,     -3,     3, '(J/#Psi + K^{+}) #eta'                                         ]
histos['jpsiK_phi'                 ] = ['jpsiK_phi'                 , '', 20, -np.pi, np.pi, '(J/#Psi + K^{+}) #phi'                                         ]
histos['jpsipi_pt'                 ] = ['jpsipi_pt'                 , '', 50,      0,    50, '(J/#Psi + #pi^{+}) p_{T} (GeV)']                                
histos['jpsipi_mass'               ] = ['jpsipi_mass'               , '', 80,      3,     8, '(J/#Psi + #pi^{+}) mass (GeV)']                                 
histos['jpsipi_eta'                ] = ['jpsipi_eta'                , '', 30,     -3,     3, '(J/#Psi + #pi^{+}) #eta'                                       ]
histos['jpsipi_phi'                ] = ['jpsipi_phi'                , '', 20, -np.pi, np.pi, '(J/#Psi + #pi^{+}) #phi'                                       ]
histos['bct'                       ] = ['bct'                       , '', 50,      0,  1e-1, 'ct (cm)']
'''
                                                       
# histos['npv_good'                  ] = ['npv_good'                  , '', 70,      0,    70, '# good PV'                                                     
histos['nPV'                       ] = ['nPV'                       , '', 70,      0,    70, '#PV'                                                          ]
'''
histos['mmm_p4_par'                ] = ['mmm_p4_par'                , '', 50,    -50,   100, '3-#mu p_{#parallel} (GeV)']                                     
histos['mmm_p4_perp'               ] = ['mmm_p4_perp'               , '', 50,      0,    15, '3-#mu p_{#perp}  (GeV)']                                        
histos['Bdir_eta'                  ] = ['Bdir_eta'                  , '', 30,     -3,     3, 'B #eta from PV-SV direction'                                   ]
histos['Bdir_phi'                  ] = ['Bdir_phi'                  , '', 20, -np.pi, np.pi, 'B #phi from PV-SV direction'                                   ]
histos['mcorr'                     ] = ['mcorr'                     , '', 50,      4,    15, 'm_{corr} (GeV)']                                                
'''
#histos['decay_time_ps'             ] = ['decay_time_ps'             , '', 50,      0,    10, 't (ps)']                                                        
histos['ip3d'                      ] = ['ip3d'                      , '', 50,  -0.05,  0.05, '#mu_{3} IP3D(vtx_{J/#Psi}) (cm)']                               
#histos['ip3d_e_corr'               ] = ['ip3d_e_corr'               , '', 50,      0,  0.01, 'corrected #mu_{3} IP3D(vtx_{J/#Psi}) unc. (cm)']                
#histos['ip3d_sig_corr'             ] = ['ip3d_sig_corr'             , '', 50,     -5,     5, 'corrected #mu_{3} IP3D(vtx_{J/#Psi}) significance'             ]
histos['ip3d_e'                    ] = ['ip3d_e'                    , '', 50,      0,  0.01, '#mu_{3} IP3D(vtx_{J/#Psi}) unc. (cm)']                          
histos['ip3d_sig'                  ] = ['ip3d_sig'                  , '', 50,     -5,     5, '#mu_{3} IP3D(vtx_{J/#Psi}) significance'                       ]
# histos['bdt_mu'                    ] = ['bdt_mu'                    , '', 50,      0,     1, 'BDT #mu score'                                                 
# histos['bdt_tau'                   ] = ['bdt_tau'                   , '', 50,      0,     1, 'BDT #tau score'                                                
# histos['bdt_bkg'                   ] = ['bdt_bkg'                   , '', 50,      0,     1, 'BDT bkg score'                                                 
#histos['decay_time'                ] = ['decay_time'                , '', 50,      0,  1e-9, 't (s)']                                                         
#histos['norm'                      ] = ['norm'                      , '',  1,      0,     1, 'normalisation'                                                 ]
