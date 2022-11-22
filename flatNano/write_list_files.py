import os
'''
/gpfs/ddn/srm/cms/store/user/garamire/crab_job_2022Jul06/EGamma/crab_data_Run2018A_UL/220706_123528/0000/RJPsi_data_2022Jul06_14

A -> 2923 -> 220706_123528
B -> 1409 -> 220706_123519
C -> 1332 -> 220706_123535
D -> 6508 -> 220707_140602

'''
class storage_list:
  def __init__(self, request_name='data_Run2018A_UL', dataset_name='EGamma', is_mc = True, date='2022Jul06', job_id='220706_123528', njobs=2923, nfiles_per_job=1):
    self.server_dir = '/gpfs/ddn/srm/cms'
    self.lfn_dir_base = '/store/user/garamire/crab_job_' + date
    self.date = date 
    self.is_mc = is_mc
    self.dataset_name=dataset_name
    self.request_name= request_name
    self.job_id = job_id
    self.nfiles_per_job = nfiles_per_job 
    self.njobs = njobs
    self.full_dir = self.server_dir + self.lfn_dir_base + '/' +self.dataset_name + '/crab_' + self.request_name + '/' + self.job_id
    self.dir_list = 'list'
    self.d_paths = {}
    self.define_names()

  def set_nfiles(self, nfiles_per_job):
    self.nfiles_per_job = nfiles_per_job
    self.define_names()

  def define_names(self):
    #self.file_full_names.clear()
    file_name = 'list_'+self.dataset_name+'_'+self.request_name
    a_paths = []
    for i in range(1, self.njobs+1):
      file_name_prefix = 'RJPsi_data'
      if(self.is_mc):
        file_name_prefix = 'RJPsi_mc'
      a_paths.append("%s/%s/%s_%s_%d.root" % (self.full_dir , (str(i//1000)).zfill(4), file_name_prefix, self.date, i))
      if (not (i % self.nfiles_per_job) ):
        path = file_name+'_'+str(i//self.nfiles_per_job )
        self.d_paths[path] = a_paths.copy()
        a_paths.clear()

      if (i == self.njobs ):
        self.d_paths[file_name+'_'+str(1 + i//self.nfiles_per_job)] = a_paths.copy()
        a_paths.clear()
  def get_file_names(self):
    a_dirs = []
    for key, value in self.d_paths.items():
      a_dirs.append([self.dir_list+'/'+ key + '.txt'])
    return a_dirs
    

  def get_paths(self):
    return self.d_paths

  def save_to_files(self):
    try:
      os.mkdir(self.dir_list)
    except OSError as error:
      print(error)

    for key, value in self.d_paths.items():
      with open(self.dir_list+'/'+ key + '.txt', 'w') as f:
        for v in value:
          f.write(v)
          f.write('\n')

