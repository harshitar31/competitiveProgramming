# https://codeforces.com/contest/1846/problem/B

for testcase in range(int(input())):
    l=[]
    for i in range(3):
        l.append(list(input()))
    winner='DRAW'
    if l[0][0] == l[1][1] == l[2][2]:
        if l[0][0]!='.':
            winner=l[0][0]
    else:
        for i in l:
            if i.count(i[0])==3 and i[0]!='.':
                winner=i[0]
        for i in range(3):
            if l[0][i]==l[1][i]==l[2][i] and l[0][i]!='.':
                winner=l[0][i]
        if l[0][2]==l[1][1]==l[2][0] and l[0][2]!='.':
            winner=l[0][2]
    print(winner)
