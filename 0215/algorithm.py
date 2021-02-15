N = int(input())
num_li = [0] * 3
if N < 100:
    print(N)

else:
    cnt = 99

    for num in range(100, N+1):
        if num == 1000:
            pass
        else:
            for i in range(3):
                num_li[i] = num % 10
                num = num // 10

            if (num_li[0] + num_li[2]) / 2 == num_li[1]:
                cnt += 1
    print(cnt)