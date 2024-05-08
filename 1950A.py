# https://codeforces.com/contest/1950/problem/A

for testcase in range(int(input())):
    a,b,c=map(int,input().split())
    if a<b<c:
        print('STAIR')
    elif a<b>c:
        print('PEAK')
    else:
        print('NONE')
