# https://codeforces.com/contest/707/problem/A

n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input().split())
for i in l:
    if i.count('B')+i.count('G')+i.count('W')!=len(i):
        print('#Color')
        break
else:
    print('#Black&White')
