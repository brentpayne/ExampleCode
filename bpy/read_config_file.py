'''
Created on Jul 14, 2011

@author: brentpayne

function used to read in an auditreport package style configuration file 
and return the configuration object. If this module is called as
a script, it will output the values specified in that files.
'''

from ConfigParser import SafeConfigParser, Error as ConfigParserError

def read_config_file(config_file, call_backs=[]):
    '''
    Reads a config file into a ConfigParser then passes that ConfigParser to all call_back routines.
    The call_back routine use the ConfigParser to set necessary variables
    additionally returns a dictionary of key value pairs from all sections
    this list is flattened so a key's value will be overwritten if it is 
    duplicated in another section.  This functionality is a convenience for 
    simple config files, but call_backs are recommended
    '''
    config_reader = SafeConfigParser()
    dict={}
    try:
        config_reader.read(config_file)
        for _call_back in call_backs:
            _call_back(config_reader)
        for s in config_reader.sections():
            for (k,v) in config_reader.items(s):
                dict[k]=v
    except ConfigParserError as (errno, errstr):
        print "CONFIG PARSER ERROR: #",errno, ", ",errstr
    return dict


def _print_config_file(config_parser):
    '''
    prints sections in ConfigParser to stdout
    '''
    #import block for modules only used in this function
    from pprint import pprint

    for section in config_parser.sections():
        print "\nSECTION '"+section+"'"
        pprint(config_parser.items(section))
    

def main(argv):
    '''
    The main function called when the module is used as a commnadline script.
    '''
    
    #import block for modules only used in this function
    from optparse import OptionParser
    import os
    from sys import exit
    
    #parse options
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config", help="the configuration file")
    (options, args) = parser.parse_args()
    #pprint(options)    
    if(options.config is not None):
        #run read and print specified config file
        config_file = options.config
        if( os.path.isfile(config_file)):
            read_config_file(config_file,[print_config_file])
        else:
            sys.exit(config_file+' could not be found or is not a file')
    else:
        #run and print arguments as if they are config files
        [read_config_file(arg) for arg in args if os.path.isfile(arg)]
        
    
    

if __name__ == '__main__':
    #import block for modules only used in this function
    import sys
    
    #just call main function
    main(sys.argv)