# https://codeforces.com/contest/1950/problem/C

for testcase in range(int(input())):
    time=""
    h,m=map(str,input().split(':'))
    if h=='12':
        time+=h+':'+m+" PM"
    elif h=='00':
        time+='12'+':'+m+" AM"
    elif int(h)<12:
        time+=h+':'+m+" AM"
    else:
        if len(str(int(h)-12))==1:
            time+='0'+str(int(h)-12)+':'+m+" PM"
        else:
            time+=str((int(h)-12))+':'+m+" PM"
    print(time)
