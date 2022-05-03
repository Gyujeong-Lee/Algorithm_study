a = 'adceb'

x = sorted(a)
print(x)

a_dict = {
    'a': 1,
    'b': 3,
    'c': 2,
    'd': 3
}

print(sorted(a_dict.items(), key=lambda x:x[1]))

tmp = max(a_dict.items(), key= lambda x:x[1])
print(tmp)
print(list(a_dict.items()).count(tmp))

li = list(filter(lambda x: x[1] >= 2, a_dict.items()))
print(li)