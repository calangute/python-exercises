'''
Created on Aug 2, 2017

@author: empqtut
'''


def GetPrimes(n):
    '''print all the prime number from 0 to N
       there are multiple algorithms to deal with this problem.
       SieveOfEratosthenes algorithm marks false in an array of numbers
       from o to n for places that are multiples of prime factor
       This was one of the interview questions in viasat vp round'''
    prime = [True for i in range(n+1)]
    p=2
    while p*p <n:
        if prime[p]:
            for i in range(p+2,n+1,p):
                prime[i]=False
        p+=1
    print [i for i in range(2,n+1) if prime[i]]


if __name__=="__main__":
    print "lets run it yaar"
    GetPrimes(500)
