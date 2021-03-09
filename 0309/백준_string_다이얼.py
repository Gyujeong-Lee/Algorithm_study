'''
UNUCIC
36
'''

dial = input()

ans = 2 * len(dial)

for sp in dial:
    if sp == '1':
        pass
    elif 65 <= ord(sp) <= 67:
        ans += 1
    elif 68 <= ord(sp) <= 70:
        ans += 2
    elif 71 <= ord(sp) <= 73:
        ans += 3
    elif 74 <= ord(sp) <= 76:
        ans += 4
    elif 77 <= ord(sp) <= 79:
        ans += 5
    elif 80 <= ord(sp) <= 83:
        ans += 6
    elif 84 <= ord(sp) <= 86:
        ans += 7
    elif 87 <= ord(sp) <= 90:
        ans += 8
    else:
        ans += 9
print(ans)
