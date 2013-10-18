#!/usr/bin/python
'''

Problem Statement

Wolf Sothe is playing the game Delaymaster. In this game, he can create new words according to the following rules:
For each positive integer n, the string which consists of n copies of 'w', then n copies of 'o', then n copies of 'l', and finally n copies of 'f' is a valid word.
The concatenation of two valid words is a valid word.
Only the words that can be obtained by rules 1 and 2 are valid. There are no other valid words.
Thus, for example:
By rule 1, "wolf", "wwoollff", and "wwwooolllfff" are valid words.
Then, by rule 2, "wolfwwoollff" is a valid word.
By applying rule 2 twice, "wolfwwoollffwolf" is a valid word.
The string "wfol" is not a valid word (order matters).
The string "wwolfolf" is not a valid word (we can only concatenate, not insert one word into another).
The string "wwwoolllfff" is not a valid word (only two 'o's instead of three).
You are given a string str. Return "VALID" if str is a valid word and "INVALID" otherwise. Note that the return value is case-sensitive: you must return the strings "VALID" and "INVALID" in all-uppercase.
Definition

Class:
WolfDelaymaster
Method:
check
Parameters:
string
Returns:
string
Method signature:
def check(self, str):



Constraints
-
str will contain between 1 and 50 characters, inclusive.
-
Each character in str will be 'w', 'o', 'l' or 'f'.
Examples
0)


"wolf"
Returns: "VALID"
The first valid word from the examples in the problem statement.
1)


"wwolfolf"
Returns: "INVALID"
The second invalid word from the examples in the problem statement.
2)


"wolfwwoollffwwwooolllfffwwwwoooollllffff"
Returns: "VALID"

3)


"flowolf"
Returns: "INVALID"

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
'''

class WolfDelaymaster:
    def check(self, s):
        red_count = [0,0,0,0]
        i = 0
        while True:
            if i>=len(s):
                break
            c = s[i]
            if c=='w':
                #print red_count
                if red_count!=[red_count[0]]*4:
                    return "INVALID"
                red_count = [0,0,0,0]
                i = i+1
                red_count[0]=red_count[0]+1
                while True:
                    if s[i]=='w':
                        red_count[0]=red_count[0]+1
                        i = i+1
                    else:
                        break
            elif c=='o':
                red_count[1]=red_count[1]+1
                i = i+1
            elif c=='l':
                red_count[2]=red_count[2]+1
                i = i+1
            elif c=='f':
                red_count[3]=red_count[3]+1
                i = i+1
            else:
                return "INVALID"
        if red_count!=[red_count[0]]*4:
            return "INVALID"
        return "VALID"

x= WolfDelaymaster()
print x.check("wolfwwoollffwwwooolllfffwwwwoooollllffff")
