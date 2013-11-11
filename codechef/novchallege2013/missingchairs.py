#!/usr/bin/python
#from operator import mul    # or mul=lambda x,y:x*y
#from fractions import Fraction

#def nCk(n,k):
      #return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    ans = 2**n-1
    #for k in range(1,n+1):
    #    ans = ans + nCk(n,k)
    print ans%1000000007
