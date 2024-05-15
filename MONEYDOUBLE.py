# https://www.codechef.com/START134D/problems/MONEYDOUBLE

for testcase in range(int(input())):
    x,y=map(int,input().split())
    money=x
    for year in range(y):
        if money*2>money+1000:
            money*=2
        else:
            money+=1000
    print(money)
