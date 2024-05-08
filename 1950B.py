# https://codeforces.com/contest/1950/problem/B

for testcase in range(int(input())):
    n=int(input())
    l=[]
    c=0
    for i in range(n):
        l.append([""])
        if c%2==0:
            for j in range(n):
                if j%2==0:
                    l[-1][-1]+="##"
                else:
                    l[-1][-1]+=".."
        else:
            for j in range(n):
                if j%2==0:
                    l[-1][-1]+=".."
                else:
                    l[-1][-1]+="##"
        c+=1

    for k in range(len(l)):
        print(l[k][-1])
        print(l[k][-1])
