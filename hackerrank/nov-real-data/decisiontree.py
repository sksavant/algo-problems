#!/usr/bin/python
import sys
import json
from sklearn import tree
from sklearn.externals.six import StringIO
#import pydot

combinations = [
    ["English", "Physics", "Chemistry", "Mathematics", "ComputerScience"],
    ["English", "Physics", "Chemistry", "Mathematics", "PhysicalEducation"],
    ["English", "Physics", "Chemistry", "Mathematics", "Economics"],
    ["English", "Physics", "Chemistry", "Mathematics", "Biology"],
    ["English", "Economics", "Accountancy", "Mathematics", "BusinessStudies"]
    ]

combno = int(sys.argv[1])-1

trainingfile = open("training_"+str(combno+1)+".json","r")

featuresamples = []
answersamples = [] #no. of samples

for line in trainingfile.readlines():
    grades = json.loads(line)
    features = []
    for sub in combinations[combno]:
        if sub is not "Mathematics":
            features.append(grades[sub])
            #print grades[sub]
    featuresamples.append(features)
    answersamples.append(grades["Mathematics"])
    #print temp.keys()
    #print type(temp.keys()[0])

assert len(featuresamples)==len(answersamples)
print len(featuresamples),"samples to train with",len(featuresamples[0]),"features" #18327

clf = tree.DecisionTreeClassifier()
clf = clf.fit(featuresamples, answersamples)

#print clf.predict([[4,3,3,4]])

testfile = open("sample-test_"+str(combno+1)+".in.json","r")
anstestfile = open("computed-test_"+str(combno+1)+".json","w")

testsamples = []

for line in testfile.readlines():
    grades = json.loads(line)
    testfeatures = []
    for sub in combinations[combno]:
        if sub is not "Mathematics":
            testfeatures.append(grades[sub])
    testsamples.append(testfeatures)

print "Computing expected grades for",len(testsamples),"test samples"

predictedans = clf.predict(testsamples)

for ans in predictedans:
    anstestfile.write(str(ans)+"\n")

anstestfile.close()
testfile.close()
trainingfile.close()

'''
with open("DTree_1.dot",'w') as dot_data: # = StringIO.StringIO()
    tree.export_graphviz(clf, out_file=dot_data)
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph.write_pdf("DTree_1.pdf")
'''
