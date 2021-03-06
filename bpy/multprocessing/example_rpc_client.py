#!python

####
# a client program that utilizes our example rpc server
####

from multiprocessing.managers import BaseManager

def main():
    BaseManager.register('run_rpc_function')
    manager = BaseManager(address=('127.0.0.1',51999), authkey='my_authkey')
    manager.connect()
    returned_proxy_object = manager.run_rpc_function('SOME LOUD TEXT')
    print returned_proxy_object
    print returned_proxy_object._getvalue() #might be a better way to get the value, probably need to specify my own proxy object, see BaseProxy

if __name__ == '__main__':
    main()
