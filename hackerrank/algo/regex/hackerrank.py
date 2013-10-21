#!/usr/bin/python
import re
hackerstartregex = re.compile('\Ahackerrank[\s\w\W\S]*')
hackerendregex = re.compile('[\s\w\S\W]*hackerrank\Z')
n = int(raw_input())
for i in range(n):
    s = raw_input()
    start = not hackerstartregex.match(s)==None
    end = not hackerendregex.match(s)==None
    if start and end:
        print "0"
    elif start:
        print "1"
    elif end:
        print "2"
    else:
        print "-1"

