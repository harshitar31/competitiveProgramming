# https://codeforces.com/contest/405/problem/A

n=int(input())
l=list(map(int,input().split()))
ans=sorted(l)
for i in ans:
    print(i,end=" ")
