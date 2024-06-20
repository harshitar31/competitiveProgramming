# https://codeforces.com/contest/71/problem/A

for testcase in range(int(input())):
    s=input()
    if len(s)>10:
        print(f'{s[0]}{len(s[1:-1])}{s[-1]}')
    else:
        print(s)
