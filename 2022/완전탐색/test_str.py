
a = '12345'
b = [1, 2, 3, 4, 5]

print(a*2)
print(b*2)
n = 12
print('12345' * (n//5) + '12345'[:(n%5)])

a = [1, 2]
b = [2, 1]

if a == b:
    print('t')
else:
    print('f')

base = set([1, 2, 3])
base2 = set([1, 2, 3, 4])
result = base - base2
print(base2 - base)
print(base - base2)
if result:
    print('True')
else:
    print('False')