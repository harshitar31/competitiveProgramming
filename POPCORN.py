# https://www.codechef.com/problems/POPCORN

for testcase in range(int(input())):
    combo=[]
    for i in range(3):
        po,pe=map(int,input().split())
        combo.append([po,pe])
    maxi=0
    for i in combo:
        if sum(i)>maxi:
            maxi=sum(i)
    print(maxi)
