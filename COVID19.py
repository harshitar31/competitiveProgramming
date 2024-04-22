# https://www.codechef.com/problems/COVID19

for testcase in range(int(input())):
    n=int(input())
    x=list(map(int, input().split()))
    l=[];c=1
    for i in range(1,n):
        if x[i]-x[i-1]<=2:
            c+=1 
        else:
            if c>0:
                l.append(c)
            c=1
    else:
        if c>0:
            l.append(c)
        if l==[]:
            l.append(1)
    print(min(l),max(l),sep=" ")
            
    
