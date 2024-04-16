# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/TANDJ1?tab=statement

for testcase in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    dist=0
    if a!=c:
        dist+=abs(a-c)
    if b!=d:
        dist+=abs(b-d)
    if k<dist:
        print("NO")
    elif k==dist:
        print("YES")
    else:
        if (k-dist)%2==0:
            print("YES")
        else:
            print("NO")
