# https://codeforces.com/problemset/problem/1971/A

for testcase in range(int(input())):
    x,y=map(int,input().split())
    print(min(x,y),max(x,y))
