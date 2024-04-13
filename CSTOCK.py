# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CSTOCK

for testcase in range(int(input())):
    s,a,b,c=map(int,input().split())
    s=s+(c*0.01*s)
    if a<=s<=b:
        print('Yes')
    else:
        print('No')
