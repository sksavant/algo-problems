#!/usr/bin/python
import re
n = int(raw_input())
latlongregex = re.compile('\([\-\+]*\d+[.\d]*, [+-]*\d+.*\d*\)')
lat1regex = re.compile('(?<=\()[\+\-]*[1-9]\d*.\d+(?=,)')
lat2regex = re.compile('(?<=\()[\+\-]*[1-9]\d*(?=,)')
lng1regex = re.compile('(?<=, )[\+\-]*[1-9]\d*.\d+(?=\))')
lng2regex = re.compile('(?<=, )[\+\-]*[1-9]\d*(?=\))')
for i in range(n):
    x = raw_input()
    if not latlongregex.match(x):
        print "Invalid"
        #print "latlong"
        continue
    if lng1regex.findall(x)==[] and lng2regex.findall(x)==[]:
        #print lng1regex.match(x), lng2regex.match(x)
        #print lng1regex.findall(x), lng2regex.findall(x)
        print "Invalid"
        #print "long"
        continue
    #print lat1regex.findall(x), lat2regex.findall(x)
    if lat1regex.findall(x)==[] and lat2regex.findall(x)==[]:
        print "Invalid"
        #print "lat"
        continue
    lat,lng = map(float, x.strip('() +').split(', '))
    try:
        assert lat <= 90 and lat>=-90
    except AssertionError:
        print "Invalid"
        continue
    try:
        assert lng <= 180 and lng>=-180
    except AssertionError:
        print "Invalid"
        continue
    #print lat,lng
    print "Valid"
