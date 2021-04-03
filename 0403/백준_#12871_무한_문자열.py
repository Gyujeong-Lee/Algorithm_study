'''
ab
abab

1 or 0
'''

s = input()
t = input()
length_s = len(s)
length_t = len(t)

for i in range(len(s) * len(t)):
    if s[i % len(s)] != t[i % len(t)]:
        print(0)
        break
else:
    print(1)




