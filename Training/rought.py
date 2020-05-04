'''
Created on Mar 27, 2017

@author: empqtut
'''
from timeit import Timer


popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()","from __main__ import x")


x = list(xrange(100000))
print popzero.timeit(1000)

x = list(xrange(100000000))
print popend.timeit(1000)
