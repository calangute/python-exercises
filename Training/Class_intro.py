'''
Created on Feb 1, 2017
demonstrating classes and functions
@author: empqtut
'''

class VenA(object):
    def __init__(self):
        pass
    def fun1(self):
        print "Ven A --->Func1"
    def fun2(self):
        print "Ven A --->Func2"    
class VenB(object):
    def __init__(self):
        pass
    def fun2(self):
        print "Ven B --->Func2"

class Alpha(VenA,VenB):
    def __init__(self):
        VenA.__init__(self)
        VenB.__init__(self)
    def fun3(self):
        print "Alpha ---> Fun3"
    def fun2(self):
        super(Alpha,self).fun2()
        VenB.fun2(self)
        print "Alpha ---> Func2"

class Beta(Alpha):
    def __init__(self):
        Alpha.__init__(self)
    def fun4(self):
        print "Beta --> func4" 


b = Beta()

print b.fun4()
  
        
        