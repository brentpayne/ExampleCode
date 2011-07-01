'''
Created on Jan 4, 2010

@author: brent
'''
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
