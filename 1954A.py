# https://codeforces.com/contest/1954/problem/A

from math import ceil
for testcase in range(int(input())):
    n,m,k=map(int, input().split())
    # if n==1 or m==1:
    #     print('NO')
    # elif n==m==k:
    #     print('NO')
    # elif n-ceil(n/m)<=k:
    #     print('NO')
    # else:
    #     print('YES')
    if n-ceil(n/m)<=k:
         print('NO')
    else:
        print('YES')
