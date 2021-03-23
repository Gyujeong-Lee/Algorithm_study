n, m = map(int, input().split())
nums = list(map(int, input().split()))
black_jack = []

for num in nums:
    for num2 in nums:
        if num != num2:
            for num3 in nums:
                if num != num3 and num2 != num3:
                    black_jack.append([num, num2, num3])
max_num = 0
for i in range(len(black_jack)):
    if max_num < sum(black_jack[i]) <= m:
        max_num = sum(black_jack[i])

print(max_num)