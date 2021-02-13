def self_number(i):
    num = i
    total = i

    while num != 0:
        total += num % 10
        num = num // 10

    return total

num_list = list(range(1, 10001))
unself_nums = []
for num in num_list:
    unself = self_number(num)
    if not unself in unself_nums:
        unself_nums.append(unself)

for num in unself_nums:
    if num in num_list:
        num_list.remove(num)

for num in num_list:
    print(num)


# for number in num_list:
#     for n in num_list:
#         if number == self_number(n):
#             break
#     else:
#         print(number)