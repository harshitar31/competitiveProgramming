# https://codeforces.com/problemset/problem/1976/A

for testcase in range(int(input())):
    n=int(input())
    pwd=input()
    flag=True
    lastDig=-1
    lastletter=""
    ind=n
    for i in range(n):
        if pwd[i].isdigit():
            if int(pwd[i])<lastDig:
                flag=False
                break
            lastDig=int(pwd[i])
        if pwd[i].isalpha():
            if pwd[i]<lastletter:
                flag=False
                break
            lastletter=pwd[i]
            ind=i
        if pwd[i].isdigit() and i>ind:
            flag=False
            break

    if flag:
        print('YES')
    else:
        print('NO')

            
            
        
        
