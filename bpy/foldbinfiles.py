'''
This takes a list of files then creates n-fold test/train files.
There where be n (test file, train file) pairs.  One for each file in the file
list. The test file will be the contents of one of the files.  Its paired train 
file will be the concatenation of the contents of all other files.

@author: brent payne
'''
import os, sys
from pprint import pprint
from optparse import *
from bp_file import open_file_proper
from random import *
         

def main(argv=sys.argv):
    parser = OptionParser()
    parser.add_option("-f", "--filelist", dest="filelist", help="A file containing a list of files to fold", metavar="FILE")
    parser.add_option("-o", "--output", dest="output", help="The text begins each output file's name", metavar="FILE")
    
    (options, args) = parser.parse_args()
    filenames = [filename for filename in open_file_proper(options.filelist)]
    for i in range(0,len(filenames)):
        files = [open_file_proper(filename[0:len(filename)-1]) for filename in filenames]
        train_set = files[:i]+files[i+1:]
        test_input_file = files[i]
        train_output_file = open_file_proper(options.output+'.train.'+str(i+1), 'w')
        test_output_file = open_file_proper(options.output+'.test.'+str(i+1), 'w')
        for tf in train_set:
            for line in tf:
                train_output_file.write(line)
        for line in test_input_file:
            test_output_file.write(line)
        test_output_file.close()
        train_output_file.close()
        for f in files:
            f.close()

if __name__ == '__main__':
    #directory = "../../DeltaMFCCFeatures/delta"
    main(sys.argv)
