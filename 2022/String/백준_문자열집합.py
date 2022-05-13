N, M = map(int, input().split())
s = []
c = []
cnt = 0
for i in range(N + M):
    if i <= N-1:
        s.append(input())
    else:
        x = input()
        if x in s:
            cnt += 1
print(cnt)
