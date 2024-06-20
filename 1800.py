# https://codeforces.com/contest/1800/problem/A

for testcase in range(int(input())):
    n=int(input())
    s=input()
    a='meowMEOW'
    if ('m' not in s and 'M' not in s) or ('e' not in s and 'E' not in s) or ('o' not in s and 'O' not in s) or ('w' not in s and 'W' not in s):
        print('NO')
    else:
        for i in range(n):
            if s[i] not in a:
                print('NO')
                break
            else:
                if s[i] in 'mM' and ('o' in s[:i] or 'O' in s[:i] or 'e' in s[:i] or 'E' in s[:i] or 'w' in s[:i] or 'W' in s[:i] ):
                    print('NO')
                    break
                elif s[i] in 'eE' and ('o' in s[:i] or 'O' in s[:i] or 'w' in s[:i] or 'W' in s[:i] ):
                    print('NO')
                    break
                elif s[i] in 'oO' and ('w' in s[:i] or 'W' in s[:i] ):
                    print('NO')
                    break
        else:
            print('YES')
