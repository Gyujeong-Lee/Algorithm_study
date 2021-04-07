'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
def dfs(idx):
    print(idx, end=' ')
    visited_dfs[idx] = 1
    for i in range(N+1):
        if adj[idx][i] == 1 and visited_dfs[i] == 0:
            dfs(i)

#bfs 그래프 탐색
def bfs(idx):
    Q = []
    Q.append(idx)
    visited_bfs[idx] = 1

    while Q:
        cur_idx = Q.pop(0)
        print(cur_idx, end=' ')
        for i in range(N+1):
            if adj[cur_idx][i] == 1 and visited_bfs[i] == 0:
                visited_bfs[i] = 1
                Q.append(i)


#정점, 간선 개수, 탐색 시작 정점
N, M, V = map(int, input().split())
edge = []
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]

#양방향 그래프 표시
for i in range(M):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1

#방문 배열
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)


dfs(V)
print()
bfs(V)

