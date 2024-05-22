# https://www.codechef.com/START135D/problems/FOOTBALLTIES

for testcase in range(int(input())):
    x,y=map(int,input().split())
    print(min(x,y)%3) #or max
