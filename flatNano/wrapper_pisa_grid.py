import os
import itertools
import subprocess
import time

from multiprocessing import Process
from multiprocessing import Pool
from write_list_files import storage_list

class task_handler:
  def __init__(self, file_list=[]):
    self.file_list = file_list 
    #self.script_name = 'Resonant_dummy.py'
    self.script_name = 'Resonant_Rjpsi_v10_Pisa.py'
    self.sample_type = 'mc_mu'
  def add_file_name(self, file_name):
    self.file_list.append(file_name)

  def set_script_name(self, script_name):
    self.script_name = script_name

  def submit_task(self):
    '''
    if (self.input_file == ''):
      print('ERROR: The input file is missing')
      return 0
    elif (self.command == ''):
      print('ERROR: The command is missing')
      return 0
    else:
    '''
    for fn in self.file_list:
      command = 'python ' + self.script_name + ' --' + self.sample_type + '=' + fn
      #print(command)
    
      process = subprocess.Popen(command.split(),  stdout=subprocess.PIPE)
      output, error = process.communicate()
      print(output)

def pf(file_name):
  task = task_handler(file_name)
  task.submit_task()





def main():
  batch_size=10

  ''' MET Dataset
  sl1 = storage_list(request_name='data_Run2018A_UL', dataset_name='MET', is_mc = False, date='2022Aug17', job_id='220817_130825', njobs=2940, nfiles_per_job=10)
  sl2 = storage_list(request_name='data_Run2018B_UL', dataset_name='MET', is_mc = False, date='2022Aug17', job_id='220817_130809', njobs=1425, nfiles_per_job=10)
  sl3 = storage_list(request_name='data_Run2018C_UL', dataset_name='MET', is_mc = False, date='2022Aug17', job_id='220817_130834', njobs=1351, nfiles_per_job=10)
  sl4 = storage_list(request_name='data_Run2018D_UL', dataset_name='MET', is_mc = False, date='2022Aug17', job_id='220817_130817', njobs=6284, nfiles_per_job=10)
  sl1.save_to_files()
  sl2.save_to_files()
  sl3.save_to_files()
  sl4.save_to_files()
  '''


  ''' Charmonium 24Oct2022
  sl1 = storage_list(request_name='data_Run2018A_UL', dataset_name='Charmonium', is_mc = False, date='2022Oct24', job_id='221024_211510', njobs=2923, nfiles_per_job=10)
  sl2 = storage_list(request_name='data_Run2018B_UL', dataset_name='Charmonium', is_mc = False, date='2022Oct24', job_id='221024_211441', njobs=1414, nfiles_per_job=10)
  sl3 = storage_list(request_name='data_Run2018C_UL', dataset_name='Charmonium', is_mc = False, date='2022Oct24', job_id='221024_211526', njobs=1332, nfiles_per_job=10)
  sl4 = storage_list(request_name='data_Run2018D_UL', dataset_name='Charmonium', is_mc = False, date='2022Oct24', job_id='221024_211454', njobs=6570, nfiles_per_job=10)
  '''


  # Charmonium 7Nov2022
  sl1 = storage_list(request_name='data_Run2018A_UL', dataset_name='Charmonium', is_mc = False, date='2022Nov07', job_id='221107_134119', njobs=2923, nfiles_per_job=2923)
  sl2 = storage_list(request_name='data_Run2018B_UL', dataset_name='Charmonium', is_mc = False, date='2022Nov07', job_id='221107_134102', njobs=1414, nfiles_per_job=1414)
  sl3 = storage_list(request_name='data_Run2018C_UL', dataset_name='Charmonium', is_mc = False, date='2022Nov07', job_id='221107_134128', njobs=1332, nfiles_per_job=1332)
  sl4 = storage_list(request_name='data_Run2018D_UL', dataset_name='Charmonium', is_mc = False, date='2022Nov07', job_id='221107_134110', njobs=6570, nfiles_per_job=6570)
  sl1.save_to_files()
  sl2.save_to_files()
  sl3.save_to_files()
  sl4.save_to_files()
  
  sl_mc1 = storage_list(request_name='BcToJpsiMuNu', dataset_name='BcToJPsiMuNu_TuneCP5_13TeV-bcvegpy2-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143314', njobs=153, nfiles_per_job=153)
  sl_mc2 = storage_list(request_name='BcToJpsiTauNu', dataset_name='BcToJPsiTauNu_TuneCP5_13TeV-bcvegpy2-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143205', njobs=72, nfiles_per_job=72)
  sl_mc3 = storage_list(request_name='BcToJPsiMuMu_1', dataset_name='BcToJPsiMuMu_inclusive_TuneCP5_13TeV-bcvegpy2-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143719', njobs=299, nfiles_per_job=299)
  sl_mc4 = storage_list(request_name='BcToJPsiMuMu_2', dataset_name='BcToJPsiMuMu_inclusive_TuneCP5_13TeV-bcvegpy2-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143620', njobs=304, nfiles_per_job=304)
  sl_mc5 = storage_list(request_name='BcToJPsiMuMu_3', dataset_name='BcToJPsiMuMu_inclusive_TuneCP5_13TeV-bcvegpy2-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143516', njobs=303, nfiles_per_job=303)
  sl_mc6 = storage_list(request_name='BuToJpsiK', dataset_name='BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143816', njobs=437, nfiles_per_job=437)
  sl_mc7 = storage_list(request_name='HbToJPsiMuMu_3MuFilter', dataset_name='HbToJPsiMuMu_3MuFilter_TuneCP5_13TeV-pythia8-evtgen', is_mc = True, date='2022Nov07', job_id='221107_143416', njobs=4071, nfiles_per_job=4071)


  sl_mc1.save_to_files()
  sl_mc2.save_to_files()
  sl_mc3.save_to_files()
  sl_mc4.save_to_files()
  sl_mc5.save_to_files()
  sl_mc6.save_to_files()
  sl_mc7.save_to_files()

  #pool = Pool(batch_size)
  #pool.map(pf, sl_mc7.get_file_names())




if __name__ == '__main__':
  main()
