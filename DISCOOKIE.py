# https://www.codechef.com/problems/DISCOOKIE

for testcase in range(int(input())):
    n,m=map(int,input().split())
    if (m%n==0):
        print(0)
    elif (m/n>=1):
        cookies=m-(m//n)*n 
        if n-cookies>cookies:
            print(cookies)
        else:
            print(n-cookies)
    else:
        print(n-m)
