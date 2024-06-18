# https://codeforces.com/contest/1619/problem/A

for testcase in range(int(input())):
    s=input()
    flag=False
    for i in range(len(s)):
        n=len(s)//2
        if s[:n]==s[n:]:
            flag=True
            break
    if flag:
        print('YES')
    else:
        print('NO')
