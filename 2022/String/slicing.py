s = 'abcdefghijklmnop'
l = len(s)
print(l)
n = 3
result = s[0:l:n]
print(result)

for i in range(0, l, n):
    print(s[i:i+n])

a = '213'

print('4' + a)
