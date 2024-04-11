# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/VDATES

for testcase in range(int(input())):
    d,l,r=map(int,input().split())
    if (l<=d<=r):
        print('Take second dose now')
    elif (d>r):
        print('Too Late')
    else:
        print('Too Early')
