# https://codeforces.com/contest/580/problem/A

n=int(input())
l=list(map(int,input().split()))
maxi=0
c=1
for i in range(1,n):
    if l[i-1]<=l[i]:
        c+=1
    else:
        if c>maxi:
            maxi=c
        c=1
if c>maxi:
    maxi=c
print(maxi)
