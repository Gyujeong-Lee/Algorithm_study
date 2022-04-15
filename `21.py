order = "ABCD"
n = 4
result = ['' for _ in range(n)]

def comb(s, cnt, r):
    if cnt == r:
        print(result)
        return

    for i in range(s, n):
        result[cnt] = order[i]
        comb(i+1, cnt+1, r)

comb(0, 0, 2)