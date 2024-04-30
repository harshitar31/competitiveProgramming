# https://codeforces.com/problemset/problem/1928/A

for testcase in range(int(input())):
    a,b=map(int,input().split())
    flag=False
    if a%2==0 or b%2==0:
        if a%2==0:
            x,y=a//2,b
            if {a,b}!={x,2*y}:
                flag=True
        if b%2==0:
            x,y=a,b//2
            if {a,b}!={2*x,y}:
                flag=True
    if flag:
        print('Yes')
    else:
        print('No')
