# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRANSFORM

for testcase in range(int(input())):
    size=['NORMAL','HUGE','SMALL']
    x=int(input())
    print(size[x%3])
