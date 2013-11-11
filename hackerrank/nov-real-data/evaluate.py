#!/usr/bin/python

import sys

combno = int(sys.argv[1])-1


testfile = open("sample-test_"+str(combno+1)+".out.json","r")
anstestfile = open("computed-test_"+str(combno+1)+".json","r")

no_of_good_predictions = 0
no_of_correct_predictions = 0
total_no_of_cases = 0

for line in testfile.readlines():
    ans=int(line)
    computedans = int(anstestfile.readline())
    if abs(ans-computedans)<=1:
        no_of_good_predictions=no_of_good_predictions+1
    if ans==computedans:
        no_of_correct_predictions = no_of_correct_predictions+1
    total_no_of_cases=total_no_of_cases+1

print "Out of a total of",total_no_of_cases,"cases,"
print "Predicted",no_of_good_predictions,"cases within tolerable error"
print "Predicted",no_of_correct_predictions,"cases exactly!"
