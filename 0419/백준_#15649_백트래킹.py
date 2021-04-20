'''
1 ~ N에서
M개를 뽑아 순열
'''
def dfs():
    if len(result) == M:
        for i in range(M):
            print(result[i], end=' ')
        print()
        return

    for i in range(N):
        if not data[i] in result:
            result.append(data[i])
            dfs()
            result.pop()

N, M = map(int, input().split())
data = list(range(1, N+1))
result = []
dfs()