'''
This takes a list and partitions it into n-bins of equal size. 
If used as a main, the lines of the input file we be the list. 
The output will be n new files in the current directory.

@author: brent payne
'''
import os, sys
from pprint import pprint
from optparse import *
from bp_file import open_file_proper
from random import *
         

def main(argv=sys.argv):
    parser = OptionParser()
    #TODO: default to 10
    parser.add_option("-n", "--number_of_bins", dest="number", help="The number of bins to create")
    parser.add_option("-o", "--output", dest="output", help="The text begins each output file's name", metavar="FILE")
    parser.add_option("-r", "--random", dest="random", help="Use if you would like that lines to be randomly selected, bins will still be equal size")
    #TODO add additional params
    #parser.add_option("-l", "--filelist", dest="filelist", help="The file contains a list of files.  The lines of each file will be binned", metavar="FILE")
    #parser.add_option("-f", "--filelist", dest="filelist", help="The file contains a file whose lines will be binned", metavar="FILE")
    #parser.add_option("-f", "--filelist", dest="filelist", help="The file contains a file whose lines will be binned", metavar="FILE")
    #TODO: add param to specify selection style (random with known total size, random unknown total sizes, fixed size chunks, etc)
    #TODO: add ability to set output file name
    
    (options, args) = parser.parse_args()
    #TODO process input stream
    n = int(options.number)
    output_filename = options.output

    bin_files = []
    for i in range(0,n):
        bin_files.append(open_file_proper(output_filename+'.'+str(i+1),'w'))
    if(options.random):
        process_randomly(args, bin_files, n)
    else:
        process_normally(args, bin_files, n)
    for f in bin_files:
        f.close()
        
def process_randomly(args, bin_files, n):
    '''
    This function takes a list of input files and a list of output files and the number of output files.
    It distributes the lines from the input files into the output files so that each output file has
    roughly the same number of lines. Lines are randomly selected for placement into each output file.
    The random funciton is seeded by system time.
    
    args : list of input filenames
    bin_files : list of output file handles
    n : number of output file handles
    '''
    map_to_lines = {}
    keys = []
    seed()
    file_handles =  [open_file_proper(arg) for arg in args];
    keyed_lines = []
    for f in file_handles:
        for line in f:
            keyed_lines.append((random(),line))
    #keyed_lines = [(random(),line) for line in [f.readlines for f in file_handles])]
    keyed_lines.sort()
    current_output_file_index = 0
    for t in keyed_lines:
        line = t[1]
        bin_files[current_output_file_index].write(line)
        current_output_file_index = (current_output_file_index + 1) % n
        
def process_normally(args, bin_files, n):
    '''
    This function takes a list of input files and a list of output files and the number of output files.
    It distributes the lines from the input files into the output files so that each output file has
    roughly the same number of lines.
    
    args : list of input filenames
    bin_files : list of output file handles
    n : number of output file handles
    '''
    current_output_file_index = 0
    for a in args:
        f = open_file_proper(a,'r')
        for line in f:
            bin_files[current_output_file_index].write(line)
            current_output_file_index = (current_output_file_index + 1) % n

if __name__ == '__main__':
    #directory = "../../DeltaMFCCFeatures/delta"
    main(sys.argv)
