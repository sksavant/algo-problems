#!/usr/bin/python
'''

Problem Statement

Fox Ciel is now in high school. The seats in her classroom are arranged into an n by m matrix. The rows are numbered from 0 to n-1 (front to back) and the columns from 0 to m-1 (left to right).   At the beginning, Ciel can choose any of the seats. Then, at the end of each week Ciel will shift one row to the back and one column to the right, wrapping around whenever necessary. Formally, if her current seat is in row r and column c, then her seat next week will be the one in row ((r+1) modulo n) and column ((c+1) modulo m).   Fox Ciel now wonders whether she can sit in all the seats in the classroom if she follows the above procedure. As we already mentioned, she can start in any of the seats. Also, she can attend the school for as many weeks as she wants to. Return "Possible" if she can sit in all the seats and "Impossible" otherwise.
Definition

Class:
FoxAndClassroom
Method:
ableTo
Parameters:
integer, integer
Returns:
string
Method signature:
def ableTo(self, n, m):



Constraints
-
n will be between 2 and 10, inclusive.
-
m will be between 2 and 10, inclusive.
Examples
0)


2
3
Returns: "Possible"
We will use (r,c) to denote the chair at row r, column c. Suppose Ciel starts at (1,0). In the following weeks she will then sit at (0,1), (1,2), (0,0), (1,1), (0,2), (1,0) again, (0,1) again, and so on. We can see that already after 6 weeks Ciel sat in all the seats.
1)

2
2
Returns: "Impossible"
Suppose that she starts at (0,0). Then the next week she will sit at (1,1) and the week after that she will be back at (0,0). She would never sit at (0,1) and (1,0). Similarly we can show that none of the other starting positions work.
2)

4
6
Returns: "Impossible"

3)
3
6
Returns: "Impossible"

4)
5
7
Returns: "Possible"

5)

10
10
Returns: "Impossible"

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
'''

def nextseat(s,n,m):
    return ((s[0]+1)%n,(s[1]+1)%m)

class FoxAndClassroom:
    def ableTo(self, n, m):
        seats = []
        seat = (0,0)
        seats.append(seat)
        while True:
            ns = nextseat(seat,n,m)
            seat = ns
            #print ns
            if ns in seats:
                if len(seats) == n*m:
                    return "Possible"
                else:
                    return "Impossible"
            else:
                seats.append(ns)

if __name__=="__main__":
    print nextseat((1,1),2,3)
    s = FoxAndClassroom()
    for i in range(2,11):
        for j in range(2,11):
            print i,j,s.ableTo(i,j)
    '''
    print s.ableTo(2,2)
    print s.ableTo(4,6)
    print s.ableTo(3,6)
    print s.ableTo(5,7)
    print s.ableTo(10,10)
    '''
