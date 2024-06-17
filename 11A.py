# https://codeforces.com/problemset/problem/11/A

import math
n,d=map(int,input().split())
arr=list(map(int,input().split()))
c=0
i=1
while True:
    if i==n:
        break
    if arr[i-1]<arr[i]:
        i+=1
        continue
    else:
        if (arr[i-1]==arr[i]):
            c+=1
            arr[i]+=d
        else:
            c+=math.ceil((arr[i-1]-arr[i])/d)
            arr[i]+=math.ceil((arr[i-1]-arr[i])/d)*d
    if arr[i-1]==arr[i]:
        i-=1
    i+=1
        
print(c)
         
