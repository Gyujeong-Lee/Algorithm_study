import copy
a = [1, 2, 3, 4]
b = a
c = copy.deepcopy(a)

a[1] = 7


print(a)
print(b)
print(c)