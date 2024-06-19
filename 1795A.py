# https://codeforces.com/contest/1795/problem/A

def check(s):
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            return False
    return True
c=0
for testcase in range(int(input())):
    n,m=map(int,input().split())
    t1=input()
    t2=input()

    while True:
        if check(t1) and check(t2):
            print('YES')
            break
        elif check(t1) and t2[-1]!=t1[-1]:
            t1=t1+t2[-1]
            t2=t2[:-1]            
        elif check(t2) and t2[-1]!=t1[-1]:
            t2=t2+t1[-1]
            t1=t1[:-1]

        else:
            print('NO')
            break
    
