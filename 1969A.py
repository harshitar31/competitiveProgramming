# https://codeforces.com/problemset/problem/1969/A

for testcase in range(int(input())):
    n=int(input())
    p=list(map(int, input().split()))
    inv=0
    for i in range(len(p)-1):
        x=p[i]
        if p[x-1]==i+1:
            print(2)
            break
    else:
        print(3)
