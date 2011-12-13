'''
.. container:: creation-info

Created on 12/9/11

@author: brent
'''
import cProfile
import threading

__author__ = 'brent'

class ProfiledThread(threading.Thread):
    # Overrides threading.Thread.run()
    def run(self):
        profiler = cProfile.Profile()
        try:
            return profiler.runcall(threading.Thread.run, self)
        finally:
            profiler.dump_stats('myprofile-%d.profile' % (self.ident,))