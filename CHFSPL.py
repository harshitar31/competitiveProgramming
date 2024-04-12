# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFSPL

for testcase in range(int(input())):
    l=list(map(int,input().split()))
    maxi=l.pop(l.index(max(l)))
    maxi2=l.pop(l.index(max(l)))
    print(maxi+maxi2)
