# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/PROBCAT?tab=statement

for testcase in range(int(input())):
    x=int(input())
    if x<100:
        print("Easy")
    elif x<200:
        print('Medium')
    else:
        print('Hard')
    
