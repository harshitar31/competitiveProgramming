# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MXEVNSUB

for testcase in range(int(input())):
    n=int(input())
    if (n + n**2) % 4 == 0:
        print(n)
    else:
        print(n-1)
