# https://www.codechef.com/problems/MISSP?tab=statement

for testcase in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))
    for i in l:
        if l.count(i)%2!=0:
            print(i)
            break
        
