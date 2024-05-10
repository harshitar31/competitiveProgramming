# https://www.codechef.com/problems/LONGSEQ

for testcase in range(int(input())):
    d=input()
    z=d.count('0')
    o=d.count('1')
    if z==1 and o==len(d)-1:
        print('Yes')
    elif o==1 and z==len(d)-1:
        print('Yes')
    else:
        print('No')
