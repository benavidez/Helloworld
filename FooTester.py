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
        # test not divisible by 3 or 5
        res = Foo.foo(8)        
        self.assertEqual(res, '', res)
        res = Foo.foo(1)
        self.assertEqual(res, '', res)
        res = Foo.foo(0)        
        self.assertEqual(res, '', res)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()