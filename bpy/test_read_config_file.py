'''
Created on Jul 15, 2011

@author: brentpayne

unittest for the read_config_file module
'''
import unittest
import os.path
from datamining.config.read_config_file import read_config_file

                                     
class TestReadConfigFile(unittest.TestCase):
    
    def setUp(self):
        self.__SAMPLE_CONFIG_FILE = os.path.join( os.path.dirname(os.path.abspath( __file__ )),'sample.cfg')
        
    def _set_cp(self, config_parser):
        self.cp = config_parser

    def testReturnConfigParser(self):
        read_config_file( self.__SAMPLE_CONFIG_FILE, [self._set_cp] )
        cp = self.cp
        self.assertTrue(cp.has_section('mysqld'))
        self.assertTrue('old_passwords' in [i[0] for i in cp.items('mysqld')])
        self.assertEqual(cp.getint('mysqld','old_passwords'),1)
        self.assertTrue('pid-file' in [i[0] for i in cp.items('mysqld')])
        self.assertEqual(cp.get('mysqld','pid-file'),'/var/run/mysqld/mysqld.pid')
        self.assertEqual(len(cp.items('mysqld')),7)
        self.assertTrue(cp.has_section('My Section'))
        self.assertEqual(len(cp.items('My Section')),3)
        self.assertTrue('dir' in [i[0] for i in cp.items('My Section')])
        self.assertEquals(cp.get('My Section','dir'),'frob')
        

    def testReturnDictionary(self):
        d = read_config_file( self.__SAMPLE_CONFIG_FILE )
        self.assertTrue('old_passwords' in d)
        self.assertEqual(d['old_passwords'],'1')
        self.assertTrue('pid-file' in d)
        self.assertEqual(d['pid-file'],'/var/run/mysqld/mysqld.pid')
        self.assertTrue('dir' in d)
        self.assertEquals(d['foodir'],'frob/whatever')
        self.assertEqual(len(d),9)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()