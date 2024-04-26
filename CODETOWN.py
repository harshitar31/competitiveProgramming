# https://www.codechef.com/problems/CODETOWN?

vowels="AEIOU"
for testcase in range(int(input())):
    town=input()
    v=True
    c=True
    ctown=[town[0],town[2],town[4],town[6],town[7]]
    vtown=[town[1],town[3],town[5]]
    for i in ctown:
        if i in vowels:
            v=False
    for i in vtown:
        if i not in vowels:
            c=False
    if v and c:
        print('YES')
    else:
        print('NO')
        
