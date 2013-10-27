#!/usr/bin/python

memo = {}

def composedof(s, subs):
    if s=="":
        return True
    try:
        if memo[s]:
            return memo[s]
        else:
            return memo[s]
    except KeyError:
        memo[s] = False
    for w in subs:
        length = len(w)
        start = s[0:length]
        rest = s[length:]
        if start==w and composedof(rest,subs):
            memo[s] = True
    return memo[s]

subs = ['R','RY','RYY']
n =int(raw_input())
for i in range(n):
    s = raw_input()
    x = composedof(s,subs)
    if x:
        print "YES"
    else:
        print "NO"
