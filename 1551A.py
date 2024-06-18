# https://codeforces.com/contest/1551/problem/A

import math
for testcase in range(int(input())):
    n=int(input())
    n1=n/3
    if n1==int(n1):
        n1=int(n1)
        print(n1,n1)
    else:
        if math.ceil(n1)+ 2*int(n1) ==n:
            print(math.ceil(n1),int(n1))
        else:
            print(int(n1),math.ceil(n1))
