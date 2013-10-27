#!/usr/bin/python

# If k < n, then what?
# Then each k can be 'j' with 1/n prob
# Probability of any 2 being equal is the same as 1-prob(no equal pairs)

probdict = {}

def probunique(k,n):
    try:
        return probdict[(k,n)]
    except KeyError:
        pass
    if k>n:
        return 0.0
    if k==0:
        return 1.0
    pne = 1.0 - (1.0/n)*probunique(k-1,n-1)
    probdict[(k,n)]=pne
    return pne

t = int(raw_input())
for i in range(t):
    k,n = map(int,raw_input().split())
    print probunique(k,n)
