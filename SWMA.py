# https://www.codechef.com/START130D/problems/SWMA

for testcase in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print('YES')
    elif int(str(a)[::-1])>int(str(b)[::-1]):
        print('YES')
    elif a>int(str(b)[::-1]):
        print('YES')
    elif int(str(a)[::-1])>b:
        print('YES')
    else:
        print('NO')
