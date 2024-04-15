# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/NFS?tab=statement

for testcase in range(int(input())):
    u,v,a,s=map(int,input().split())
    if u==v:
        print('YES')
    elif (u**2 - 2*a*s) > v**2:
        print('NO')
    else:
        print('YES')
