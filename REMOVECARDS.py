# https://www.codechef.com/problems/REMOVECARDS

for testcase in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=set(a)
    maxi=0
    for i in s:
        if a.count(i)>maxi:
            maxi=a.count(i)
    print(n-maxi)
