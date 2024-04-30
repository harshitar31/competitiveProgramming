# https://codeforces.com/problemset/problem/231/A

count=0
for problem in range(int(input())):
    l=input().split()
    if l.count('1')>=2:
        count+=1
print(count)
