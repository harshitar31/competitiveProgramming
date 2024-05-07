# https://codeforces.com/problemset/problem/490/A

n=int(input())
l=list(map(int, input().split()))
pr=l.count(1)
ma=l.count(2)
pe=l.count(3)
arr=[]
a=[];b=[];c=[]
w=0
while pr>0 and ma>0 and pe>0:
    w+=1
    pr-=1;ma-=1;pe-=1
 
for i in range(w):
    a=l.index(1)
    b=l.index(2)
    c=l.index(3)
    l[a]=0
    l[b]=0
    l[c]=0
    arr.append([a+1,b+1,c+1])

print(w)
for i in arr:
    print(i[0],i[1],i[2])
