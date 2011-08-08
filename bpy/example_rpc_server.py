#!python

####
# An example RPC Server built using python's multiprocessing library
#  (new in python 2.6)
# This example serves a function that recieves a string and returns the 
#  lowercase version of the string
# went ahead a daemoned it with pyton_daemon
####

from multiprocessing.managers import BaseManager
import daemon

def some_function(text):
    print text
    return text.lower()

def main():
    BaseManager.register('run_rpc_function', some_function)
    manager = BaseManager(address=('127.0.0.1',51999),authkey='my_authkey')
    service = manager.get_server()
    service.serve_forever()

if __name__ == '__main__':
    print 'here'
    with daemon.DaemonContext():
        print "in daemon context"
        main()
