#!/usr/bin/python
import re
char = '[A-Z]'
num = '[0-9]'
panregex = re.compile('\A'+char*5+num*4+char+'\Z')

n = int(raw_input())
for i in range(n):
    s = raw_input()
    if panregex.match(s)==None:
        print "NO"
    else:
        print "YES"
