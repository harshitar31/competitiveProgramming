# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/WEIGHTBL

for testcase in range(int(input())):
    w1,w2,x1,x2,m=map(int,input().split())
    inc=w2-w1
    if x1*m<=inc<=x2*m:
        print(1)
    else:
        print(0)
