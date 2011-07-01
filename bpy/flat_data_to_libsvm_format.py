'''
Created on Jun 23, 2010

@author: brent
'''

import sys

from open_file_proper import open_file_proper
from str_to_float import strs_to_float


def featurefile_to_libsvmfeaturefile(input_features_filename, libsvm_output_filename):

    
    #open input file
    input_file = open_file_proper(input_features_filename)
    
    #open output file
    libsvm_file = open_file_proper(libsvm_output_filename,'w')
    
    #read in observations
    for line in input_file:
        cols = strs_to_float(line.split(), 0.0)
        value = " ".join(map( lambda x: "%d:%d"%x, enumerate(cols) ))
        libsvm_file.write(value+"\n")
    
    input_file.close()
    libsvm_file.close()

def featurefile_labelfile_to_libsvmfeaturefile(input_features_filename, input_label_filename, labelnum, libsvm_output_filename):
    
    #open input files
    input_features_file = open_file_proper(input_features_filename)
    input_labels_file = open_file_proper(input_features_filename)
    
    #open output file
    libsvm_file = open_file_proper(libsvm_output_filename,'w')
    
    #read in observations
    for line in input_features_file:
        labels = strs_to_float(input_labels_file.readline().split(),0)
        cols = strs_to_float(line.split(), 0.0)
        value = labels[labelnum]+' '+" ".join(map( lambda x: "%d:%d"%x, enumerate(cols) ))
        libsvm_file.write(value+"\n")
    
    input_features_file.close()
    input_labels_file.close()
    libsvm_file.close()
    

def csv_to_libsvmfeaturefile(input_filename, output_filename):
        
    #open input file
    input_file = open_file_proper(input_filename)
    
    #open output file
    libsvm_file = open_file_proper(output_filename,'w')
    
    #read in observations
    for line in input_file:
        cols = strs_to_float(line.split(","), 0.0)
        value = "%d"%cols[0]+" "+" ".join(map( lambda x: "%d:%d"%x, enumerate(cols[1:]) ))
        libsvm_file.write(value+"\n")
    
    input_file.close()
    libsvm_file.close()
    

def convert_all_cvs_in_folder(foldername, regmatch):
    from glob import *
    import re
    
    globstr = foldername+"/"+ regmatch
    it = glob(globstr)
    for f in it:
        m = re.search("(.*\.).*?$",f)
        fout = m.group(1) + "libsvm"
        print f, fout
        csv_to_libsvmfeaturefile(f,fout)
        
    
    
      

if __name__ == '__main__':
    print("NOT A MAIN FILE")
    convert_all_cvs_in_folder("/home/brent/Coding/multilabel","cal500*txt")
