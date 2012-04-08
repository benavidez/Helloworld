'''
Created on Apr 8, 2012

@author: eduardob
'''
import unittest
import Foo

class FooTester(unittest.TestCase):


    def testFoo(self):
        res = Foo.foo(18)
        self.assertEqual(res, 'fizz', res)
        res = Foo.foo(10)
        self.assertEqual(res, 'buzz', res)
        res = Foo.foo(555)        
        self.assertEqual(res, 'fizzbuzz', res)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()