'''
Created on Jul 18, 2010

@author: brent
'''
def request_string_from_user():
    '''
    Requests input from user
    Handles bad input by issuing warning and re-prompting for input
    returns user input
    '''
    value = ''
    
    while(len(value)==0):
        value = raw_input('Enter something')
        value = value.strip( )
        if(len(value)==0):
            print( 'not good enough' )
    
    return value  
