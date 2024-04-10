# https://www.codechef.com/START129D/problems/BID

for testcase in range(int(input())):
    n=int(input())
    atA=sum(list(map(int,input().split())))
    defA=sum(list(map(int,input().split())))
    atP=sum(list(map(int,input().split())))
    defP=sum(list(map(int,input().split())))
    
    if atA>atP and defA>defP:
        print('A')
    elif atA<atP and defA<defP:
        print('P')
    else:
        print('DRAW')
