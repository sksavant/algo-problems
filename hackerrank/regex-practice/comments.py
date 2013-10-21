#!/usr/bin/python
import re
single = re.compile('\.*\/\/[\s\S\w\W]*')
multistart = re.compile('\.*\/\*[\s\S\w\W]*')
multistop = re.compile('[\s\S\w\W]*\*\/\.*')
multicomment = False
#print single.findall('// s')
while True:
    try:
        x = raw_input()
    except EOFError:
        break
    if multicomment:
        try:
            print multistop.findall(x)[0]
            multicomment = False
        except IndexError:
            print x
    else:
        try:
            print single.findall(x)[0]
        except IndexError:
            pass
        try:
            s= multistart.findall(x)[0]
            try:
                print multistop.findall(s)[0]
            except IndexError:
                print s
                multicomment = True
        except IndexError:
            pass
