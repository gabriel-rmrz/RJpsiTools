import ROOT
import os, sys


chunks_of = 50
inFilePath = sys.argv[1]
#outFileName = sys.argv[2]

list_of_files =[]
for inFile  in os.listdir(inFilePath):
    #if not os.isfile(inFile) :
    #    continue
    #print(inFile)
    list_of_files.append(inFilePath+"/"+inFile)

lenght=len(list_of_files) 
 
print("Number of files: ",lenght)
for i in range(0, (lenght//chunks_of +1)):
    input_files = "{}".format(list_of_files[i:i+chunks_of]).replace("[","").replace(",","").replace("]","").replace("'","")
    print ( input_files)
    os.system('hadd -k -j 10 {}/chunk_{}.root {}'.format(inFilePath,i,input_files))
    i = i+chunks_of

os.system('hadd -k -n 50 %s/file_total.root %s/chunk_*.root'.format(inFilePath,inFilePath))
