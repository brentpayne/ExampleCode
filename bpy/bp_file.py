'''
Created on Jan 4, 2010

@author: brent
'''

def check_if_exists(filename):
    import os
    bexists = os.path.isfile(filename)
    
    #handle error opening
    try:
       fsock = open(filename)       
    except IOError:                     
        print "The file does not exist, exiting gracefully"
    print "This line will always print" 

    
def count_file_lines(filename):
    f = open(filename,'r')
    i=0
    while(f.readline()):
        i+=1   
    f.close()
    return i

def read_file_into_tuples(filename):
    f = open(filename,'r')
    list_of_tuples = []
    for line in f.readlines():
        list_of_tuples.append( 
                              tuple( 
                                    [float(t) for t in line.split()] 
                                     ) 
                              )
    f.close()
    return list_of_tuples
    

def open_file_proper(filename, options="r"):
    import sys
    '''
    opens file with proper error checking
    '''

    try:
        fptr = open(filename, options)
    except IOError, e:
        sys.exit('file %s could not be opened: %s'%(filename, e))
    return fptr

