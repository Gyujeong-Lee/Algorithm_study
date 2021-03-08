'''
2
3 ABC
5 /HTP
'''
T = int(input())
for tc in range(1, T+1):
    r, s = input().split()
    r = int(r)
    new_s = ''
    for i in range(len(s)):
        new_s += s[i]*r

    print(new_s)