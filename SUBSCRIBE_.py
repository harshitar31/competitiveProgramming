# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUBSCRIBE_

from math import ceil
for testcase in range(int(input())):
    n,x=map(int,input().split())
    print(ceil(n/6)*x)
