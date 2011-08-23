#!python
'''
This file shows an example of two decorators.

A normal decorator and a decorator that takes arguments
'''

def std_decorator(func):
    '''
    @param func   the dunction to decorate
    '''
    print 'decorating a function'
    
    def wrapping_code(*args):
        '''
        this is the code that wraps the decorated function
        '''
        print 'decorating code'
        func(*args)
        print 'done with decorating code'

    return wrapping_code #make sure to always return a function pointer


class argument_decorator(object):
   '''
   This decorator takes arguments
   '''

   def __init__(self, arg1 = 3, arg2 = 5):
      '''
      this is the initializer for the decorator which takes two optional arguments
      '''
      self.arg1 = arg1
      self.arg2 = arg2
      print 'init with ',arg1, arg2


   def __call__(self, func):
      '''
      this is called to wrap a function
      @param func   the function to be decorated
      '''
      print 'inside __call__'
      def wrapping_code(*args):
          '''
          The wrapping code
          '''
          try:
             print 'in wrapper with args:',self.arg1,self.arg2
             func(*args)
             print 'adding args',self.arg1+self.arg2
          except Exception as e:
             print "not going to handle this Exception",e
             raise e
      return wrapping_code #remember to return a function pointer


if __name__ == '__main__': 
   print 'decorating simple function with simple decorator'
   @std_decorator
   def simple_function():
       print 'this is a simple funciton'
   simple_function()
   print 'decorating with default arguments'
   @argument_decorator() #must have () else it doesn't work
   def f1(n):
       print '100 dived by %d'%n
       print 100/n
   f1(5)
   print 'decorating with arguments (7,5)'
   @argument_decorator(7,5)
   def f2(n):
       print '100 dived by %d'%n
       print 100/n
   f2(5)
   print 'decorating with named arguments arg2=7, arg1=9'
   @argument_decorator(arg2=7, arg1=9)
   def f3(n):
       print '100 dived by %d'%n
       print 100/n
   f3(5)
   f3(0)
