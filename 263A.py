# https://codeforces.com/problemset/problem/263/A

l=[]
i=0
for k in range(5):
    li=list(map(int,input().split()))
    if 1 in li:
        j=li.index(1)+1
        i=k+1
    l.append(li)
print(abs(3-i) + abs(3-j))
