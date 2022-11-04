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
    self.sample_type = 'data'
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
  '''
  handler = task_handler()
  #handler.set_script_name('Resonant_dummy.py')
  #handler.set_sample_type('data')
  handler.add_file_name('test1.txt')
  handler.add_file_name('test2.txt')
  handler.add_file_name('test3.txt')
  #handler.submit_task()

  file_name_prefix = 'test'
  n_files = 100 
  file_names = []
  
  for n in range(1,n_files+1):
    file_names.append([file_name_prefix + str(n)+'.txt'])
  print(file_names)
    '''
  batch_size=10

  ''' MET Dataset
  sl1 = storage_list(request_name='data_Run2018A_UL', dataset_name='MET', date='2022Aug17', job_id='220817_130825', njobs=2940)
  sl2 = storage_list(request_name='data_Run2018B_UL', dataset_name='MET', date='2022Aug17', job_id='220817_130809', njobs=1425)
  sl3 = storage_list(request_name='data_Run2018C_UL', dataset_name='MET', date='2022Aug17', job_id='220817_130834', njobs=1351)
  sl4 = storage_list(request_name='data_Run2018D_UL', dataset_name='MET', date='2022Aug17', job_id='220817_130817', njobs=6284)
  sl1.save_to_files()
  sl2.save_to_files()
  sl3.save_to_files()
  sl4.save_to_files()
  '''

  # Charmonium 24Oct2022
  sl1 = storage_list(request_name='data_Run2018A_UL', dataset_name='Charmonium', date='2022Oct24', job_id='221024_211510', njobs=2923)
  sl2 = storage_list(request_name='data_Run2018B_UL', dataset_name='Charmonium', date='2022Oct24', job_id='221024_211441', njobs=1414)
  sl3 = storage_list(request_name='data_Run2018C_UL', dataset_name='Charmonium', date='2022Oct24', job_id='221024_211526', njobs=1332)
  sl4 = storage_list(request_name='data_Run2018D_UL', dataset_name='Charmonium', date='2022Oct24', job_id='221024_211454', njobs=6570)

  sl1.save_to_files()
  sl2.save_to_files()
  sl3.save_to_files()
  sl4.save_to_files()

  pool = Pool(batch_size)
  pool.map(pf, sl4.get_file_names())




if __name__ == '__main__':
  main()
