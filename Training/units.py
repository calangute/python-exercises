'''
Created on Feb 1, 2017

@author: empqtut

dia.viji@gmail.com

09845432124
'''
import mymathlib
import unittest

class mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_add(self):
        self.assertEqual(mymathlib.add(10,20), 30)
    def test_minus(self):
        self.assertEqual(mymathlib.minus(20,5), 15)    
    

if __name__ == '__main__':
    unittest.main()