# https://codeforces.com/problemset/problem/1829/A

string="codeforces"
for testcase in range(int(input())):
    count=0
    s=input()
    for i in range(len(string)):
        if string[i]!=s[i]:
            count+=1
    print(count)

