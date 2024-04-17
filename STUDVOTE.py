# https://www.codechef.com/problems/STUDVOTE

for testcase in range(int(input())):
    n,k=map(int, input().split())
    l=list(map(int,input().split()))
    d=dict()
    for i in range(1,n+1):
        d[i]=l.count(i)
    count=0
    for i in d:
        if l[i-1]!=i and d[i]>=k:
            count+=1 
    print(count)
    
