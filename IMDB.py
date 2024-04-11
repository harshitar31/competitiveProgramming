# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/IMDB

for testcase in range(int(input())):
    n,x=map(int,input().split())
    space=[]
    rating=[]
    high=0
    for mov in range(n):
        num,rat=map(int,input().split())
        space.append(num)
        rating.append(rat)
    for i in range(n):
        if rating[i]>high and space[i]<=x:
            high=rating[i]
    print(high)
