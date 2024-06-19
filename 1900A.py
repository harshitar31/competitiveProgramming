# https://codeforces.com/contest/1900/problem/A

for testcase in range(int(input())):
    n=int(input())
    row=input()
    count=0
    if row.count('#')==n:
        count=0
    else:
        while True:
            # print(row,count)
            if row.count('.')==0:
                break
            elif 'bbb' in row:
                row=row.replace('.','b')
            elif '...' in row:
                count+=2
                row=row.replace('...','bbb',1)
            else:
                count+=row.count('.')
                break
    print(count)
