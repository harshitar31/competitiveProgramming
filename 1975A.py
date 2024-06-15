# https://codeforces.com/problemset/problem/1975/A

for testcase in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=sorted(l)
    x=l[:]
    y=[]
    for i in range(n-1):
        if l[i+1]<l[i]:
            x=l[:i+1]
            y=l[i+1:]
            break
    if y+x == ans:
        print('Yes')
    else:
        print('No')
 
