'''
Created on Apr 8, 2012

@author: eduardob
'''

def foo(n):
    ret = ''
    if n != 0:
        if n % 3 == 0:
            ret += 'fizz'
        if n % 5 == 0:
            ret += 'buzz'
    return ret
            