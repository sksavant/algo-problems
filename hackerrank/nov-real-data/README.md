# November Real Data Contest

## Predict the missing Grade

training.json contains training data with grades of all 5 subjects for 79465 students

sample-test.in.json contains input data as specified for 69530 students

## The Data

The most dominant combinations are 
English, Physics, Chemistry, Mathematics, Computer Science
English, Physics, Chemistry, Mathematics, Physical Education
English, Physics, Chemistry, Mathematics, Economics
English, Physics, Chemistry, Mathematics, Biology
English, Economics, Accountancy, Mathematics, Business Studies


## Approach

### Decision tree classification

Features are the scores in other subjects
Just choose only those that are needed i.e, Check only for the given five
combinations

- Data seperation
-- First try to get training data containing combination 1
-- Get sample input and output for testing the combination 1


