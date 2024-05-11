# https://codeforces.com/problemset/problem/617/A

x=int(input())
steps=0
for i in range(5,0,-1):
    steps+=x//i
    if (x//i)>0:
        x=x-(x//i)*i
print(steps)
    
