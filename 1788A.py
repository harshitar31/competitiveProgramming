# https://codeforces.com/contest/1788/problem/A

for testcase in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if arr.count(2)%2!=0:
        print(-1)
    elif 2 not in arr:
        print(1)
    else:
        c=0
        num=arr.count(2)//2
        for i in range(n):
            if arr[i]==2:
                c+=1
                if c==num:
                    print(i+1)
                    break
