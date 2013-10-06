#!/usr/bin/python
'''

Problem Statement

The pony Applejack is going to raise a new barn. The barn will consist of N sections in a row. Some of the sections will be empty, others will contain a single cow each. You are given a string str with N characters. This string describes the desired layout of the barn: the character 'c' represents a section with a cow, and the character '.' represents an empty section.  After she raises the barn, Applejack will build a wall that will divide the barn into two separate parts: one containing the first k sections and the other containing the last N-k sections, for some integer k. Each part must contain at least one section. (I.e., k must be between 1 and N-1, inclusive.) Additionally, Applejack wants both parts to contain exactly the same number of cows.  Return the number of possible positions for the wall. In other words, return the number of choices for the integer k such that all the conditions above are satisfied.
Definition

Class:
RaiseThisBarn
Method:
calc
Parameters:
string
Returns:
integer
Method signature:
def calc(self, str):



Constraints
-
str will contain between 2 and 50 characters, inclusive.
-
Each character in str will be 'c' or '.'.
Examples
0)


"cc..c.c"
Returns: 3
Applejack can choose k=2, k=3, or k=4. The three corresponding solutions are shown below, with '|' representing the wall between the two parts.
cc|..c.c
cc.|.c.c
cc..|c.c
1)


"c....c....c"
Returns: 0
There is an odd number of cows. It is impossible to divide them into two equal halves.
2)


"............"
Returns: 11
This is a barn with 12 empty sections. It can be divided in 11 different ways: into 1+11 sections, 2+10 sections, ..., or 11+1 sections.
3)


".c.c...c..ccc.c..c.c.cc..ccc"
Returns: 3

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
'''

class RaiseThisBarn:
    def calc(self,s):
        n_cows = 0
        ls = len(s)
        for x in s:
            if x=='c':
                n_cows=n_cows+1
        if n_cows%2==1:
            return 0
        if n_cows==0:
            return len(s)-1
        n_left = 0
        for i_left in range(ls):
            if s[i_left]=='c':
                n_left = n_left +1
            if n_left == n_cows/2:
                break
        #print i_left
        n_right = 0
        for i_right in range(ls):
            if s[ls-1-i_right]=='c':
                n_right = n_right+1
            if n_right == n_cows/2:
                break
        #print ls-1-i_right
        return ls-1-i_right-i_left

x = RaiseThisBarn()
print x.calc("cc..c.c")
print x.calc("c....c....c")
print x.calc("............")
print x.calc(".c.c...c..ccc.c..c.c.cc..ccc")
