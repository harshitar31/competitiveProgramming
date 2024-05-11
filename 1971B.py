# https://codeforces.com/problemset/problem/1971/B

for testcase in range(int(input())):
    s=input()
    ssort=''
    for i in sorted(s):
        ssort+=i
    if s!=ssort:
        print('YES')
        print(ssort)
    elif s!=s[-1]+s[:-1]:
        print('YES')
        print(s[-1]+s[:-1])
    else:
        print('NO')
