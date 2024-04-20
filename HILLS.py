# https://www.codechef.com/problems/HILLS

for testcase in range(int(input())):
    n,u,d=map(int,input().split())
    h=list(map(int,input().split()))
    c=1
    parachute=True
    for i in range(1,n):
        if (h[i]-h[i-1]<=u and h[i]>h[i-1]) or (h[i-1]-h[i]<=d and h[i]<h[i-1]) or h[i-1]==h[i]:
            c+=1
        elif h[i-1]-h[i]>d and h[i]<h[i-1] and parachute:
            c+=1 
            parachute=False
        else:
            break
    print(c)
        
