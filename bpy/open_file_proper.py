'''
Created on Jul 7, 2010

@author: brent
'''

import sys

def open_file_proper(filename, options="r"):
    '''
    opens file with proper error checking
    '''

    try:
        fptr = open(filename, options)
    except IOError, e:
        sys.exit('file %s could not be opened: %s'%(filename, e))
    return fptr
    