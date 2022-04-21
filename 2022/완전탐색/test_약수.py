


def divide(x):
    arr = []

    for i in range(1, x):
        if x % i == 0:
            tmp = x // i
            if (i, tmp) not in arr and (tmp, i) not in arr:
                arr.append((i, tmp))
    return arr


print(divide(10))