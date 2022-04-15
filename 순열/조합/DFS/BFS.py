numbers = [1, 1, 1, 1, 1]
target = 3
l = len(numbers)
cnt = 0
def dfs(num, idx, n):
    global cnt
    if idx == n:
        if num == target:
            cnt += 1
        return
    dfs(num+numbers[idx], idx+1, n)
    dfs(num-numbers[idx], idx+1, n)

dfs(0, 0, l)
print(cnt)

