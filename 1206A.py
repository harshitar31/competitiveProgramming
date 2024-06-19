# https://codeforces.com/contest/1206/problem/A

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
flag=False
for i in a:
    for j in b:
        if i+j not in a and i+j not in b:
            print(i,j)
            flag=True
            break
    if flag:
        break
