'''
Created on Feb 28, 2017

@author: empqtut
'''
def gcd(m,n):
    while (m%n)!=0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
        

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        
    def simplify(self,n1,n2):
        common = gcd(n1,n2)
        return Fraction(n1//common,n2//common)
    
    def __str__(self):
        return "{0}/{1}".format(self.num,self.den)
    
    def __add__(self,fraction2):    
        newnum = ((self.num*fraction2.den)+(fraction2.num*self.den))
        newden = self.den * fraction2.den
        return self.simplify(newnum,newden)
    
    def __eq__(self,fraction3):
        firstnum = self.num*fraction3.den
        secondnum = self.den*fraction3.num
        return firstnum==secondnum   
    
    def __mul__(self,fract_m):
        mnum = self.num*fract_m.num
        mden = self.den*fract_m.den
        return self.simplify(mnum,mden)
    
    def __div__(self,fract_d):
        inv_frac = Fraction(fract_d.den,fract_d.num)
        return self.__mul__(inv_frac)  
    
    def __sub__(self,fract_s):
        snum = ((self.num*fract_s.den)-(fract_s.num*self.den))
        sden = self.den * fract_s.den
        return self.simplify(snum,sden)   
    
    def __gt__(self,fract_g):
        cden = gcd(self.den,fract_g.den)
        num1 = (cden/self.den)*self.num
        num2 = (cden/fract_g.den)*fract_g.num
        return True if num1 > num2 else False
    
    def __lt__(self,fract_l):
        cden = gcd(self.den,fract_l.den)
        num1 = (cden/self.den)*self.num
        num2 = (cden/fract_l.den)*fract_l.num
        return True if num1 < num2 else False
