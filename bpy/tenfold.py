'''
Created on Jan 4, 2010

@author: brent
'''
import os, sys
from pprint import pprint
from optparse import *
         
def main(argv=sys.argv):
    parser = OptionParser()
    parser.add_option("-f", "--outputfile", dest="outputfilename", help="The file where data will be writen", metavar="FILE")
    parser.add_option("-h", "--outputfile", dest="outputfilename", help="The file where data will be writen", metavar="FILE")
    parser.add_option("-p", "--percent", dest="the percent of the file to select for heldout",help="The weight given to getting positive examples correct")
    parser.add_option("-c", "--reg", dest="c",help="The weight of reguralization")
    parser.add_option("-s", "--stub", dest="rootfilename",help="the head of tmp files")
    
    (options, args) = parser.parse_args()
    


if __name__ == '__main__':
    #directory = "../../DeltaMFCCFeatures/delta"
    main(sys.argv)
