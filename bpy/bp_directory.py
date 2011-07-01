'''
Created on Jan 4, 2010

@author: brent
'''
import re
import os

#get files from a directory
def get_files_from_directory(directory):
    return [os.path.join(directory,f) for f in os.listdir(directory)]

#walk example
import os
mydir= '/Users/xah/web/SpecialPlaneCurves_dir'
def g(s): print "g touched:", s
def myfun(dummy, dirr, filess):
    for child in filess:
        if '.html' == os.path.splitext(child)[1] and os.path.isfile(dirr+'/'+child):
            g(dirr+'/'+child)
os.path.walk(mydir, myfun, 3)



def delete_walk(top):
    
    # Delete everything reachable from the directory named in "top",
    # assuming there are no symbolic links.
    # CAUTION:  This is dangerous!  For example, if top == '/', it
    # could delete all your disk files.
    
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
