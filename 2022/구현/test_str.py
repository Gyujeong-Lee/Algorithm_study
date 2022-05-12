from copy import deepcopy
# a = 'A3*abb'
# b = '*'
# print(a.strip(b))
# print(a)
# c = [1, 2, 3, 4]
# c.copy()
#
str_list1 = [1, 1, 2, 2, 3]
str_list2 = [1, 2, 2, 4, 5]

temp = deepcopy(str_list1)

result = []
result2 = []
for n in str_list2:
    if n in temp:
        result.append(n)
        temp.remove(n)
result3 = set(str_list1) - set(str_list2)
result4 = set(str_list2) - set(str_list1)
for n in set(result):
    x = str_list1.count(n)
    y = str_list2.count(n)
    for i in range(max(x, y)):
        result2.append(n)


print(result)
print(result2)
print(result3)
print(result4)
# 결과

