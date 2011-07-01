'''
Created on Jan 4, 2010

@author: brent
'''
import re
class Filter(object):
    """
    Filter is a functor object that returns true if the input exactly matches the filter regex
    """
    def __init__(self, filter):
        if(type(filter).__name__ == 'SRE_Pattern'):
            self.filter = filter
        else:
            self.filter = re.compile(filter)
        
        
    def __call__(self, argv):
        if(self.filter.match(argv)):
            return True
        return False
        

class ActionFiltered(object):
    """
    Preforms action on an argument if the argument passes a filter
    """
    def __init__(self, action, filter):
        self.filter = Filter(filter)
        self.action = action
    
    def __call__(self, argv):
        if(self.filter(argv)):
            return self.action(argv)