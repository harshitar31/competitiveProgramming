# https://www.codechef.com/START133D/problems/MXALT?tab=ide

for testcase in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    total=0
    l.sort(reverse=True)
    if n%2==0:
        total=sum(l[:(n//2)])-sum(l[(n//2):])
    else:
        total=sum(l[:(n//2)+1])-sum(l[(n//2)+1:])
    print(total)
            
