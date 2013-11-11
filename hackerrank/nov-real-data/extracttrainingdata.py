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

trainingfile = open("training.json", "r")
sampledtrainingfile = open("training_"+str(combno+1)+".json","w")

n = int(trainingfile.readline())

for i in range(n):
    notmyline = False
    line = trainingfile.readline()
    for sub in combinations[combno]:
        if sub not in line:
            notmyline = True
    if not notmyline:
        sampledtrainingfile.write(line)

trainingfile.close()
sampledtrainingfile.close()
