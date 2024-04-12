# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/SMOL

from math import floor
for testcase in range(int(input())):
    n,k=map(int,input().split())
    if k==0:
        print(n)
    else:
     print(n-(floor(n/k))*k)
