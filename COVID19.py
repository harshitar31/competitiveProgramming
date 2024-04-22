# https://www.codechef.com/problems/COVID19

for testcase in range(int(input())):
    n=int(input())
    x=list(map(int, input().split()))
    l=[];c=1
    for i in range(1,n):
        if x[i]-x[i-1]<=2:
            c+=1 
        else:
            l.append(c)
            c=1
    else:
        l.append(c)
    print(min(l),max(l),sep=" ")
