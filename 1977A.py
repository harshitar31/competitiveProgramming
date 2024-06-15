# https://codeforces.com/problemset/problem/1977/A

for testcase in range(int(input())):
    n,m=map(int,input().split())
    if n<m:
        print('No')
    elif n==m:
        print('Yes')
    else:
        if (n-m)%2==0:
            print('Yes')
        else:
            print('No')
