# https://codeforces.com/contest/540/problem/A

n=int(input())
og=input()
sc=input()
num='0123456789'
c=0
for i in range(n):
    diff=abs(num.index(og[i])-num.index(sc[i]))
    if diff>5:
        diff=10-diff
    c+=diff
print(c)
