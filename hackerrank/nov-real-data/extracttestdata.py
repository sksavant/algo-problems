#!/usr/bin/python

import sys

combinations = [
    ["English", "Physics", "Chemistry", "Mathematics", "ComputerScience"],
    ["English", "Physics", "Chemistry", "Mathematics", "PhysicalEducation"],
    ["English", "Physics", "Chemistry", "Mathematics", "Economics"],
    ["English", "Physics", "Chemistry", "Mathematics", "Biology"],
    ["English", "Economics", "Accountancy", "Mathematics", "BusinessStudies"]
    ]

combno = int(sys.argv[1])-1

testfile = open("sample-test.in.json", "r")
ansfile = open("sample-test.out.json", "r")
sampledtestfile = open("sample-test_"+str(combno+1)+".in.json","w")
sampledansfile = open("sample-test_"+str(combno+1)+".out.json","w")

n = int(testfile.readline())

for i in range(n):
    notmyline = False
    line = testfile.readline()
    ansline = ansfile.readline()
    for sub in combinations[combno]:
        if sub not in line and sub!="Mathematics":
            notmyline = True
    if not notmyline:
        sampledtestfile.write(line)
        sampledansfile.write(ansline)

testfile.close()
sampledtestfile.close()
