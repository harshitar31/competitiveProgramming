# https://www.codechef.com/START129D/problems/BLNDOR

for testcase in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(2)%8
    if a==0:
        print('YES')
    else:
        print('NO')
