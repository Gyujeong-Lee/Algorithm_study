'''
출발지가 여러개인 BFS 문제
거리 구하기

모든 경로를 탐색하는 방법은 피하자
L -> W까지 모든 최단 거리의 합
반대로
물에서 출발하는 BFS
DFS 출발지 한개
BFS 출발지 여러개 가능 / 최단거리
가장 가까운 순으로 방문

인접의 정의 : 현재 칸의 상하좌우
인접 칸이 땅 (땅 -> 땅 / 물 -> 땅) and 방문 x

DFS와 BFS 차이를 인지하자
BFS - 시작정점부터 거쳐가는 간선의 수가 같은 순서로 탐색하는 방식
- 거리정보를 요구하는 문제
- visited에 거리정보를 넣어라


3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL

물에서 땅으로 역추적 ㄱ

'''
#
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def bfs(r, c, d):
#
#     Q = []
#     Q.append((r, c, d))
#     visited[r][c] = 1
#
#     while len(Q) != 0:
#         cur = Q.pop(0)
#         cur_idx = [cur[0], cur[1]]
#         cur_cnt = cur[2]
#
#         #4방향 탐색
#         for k in range(4):
#             nr = cur_idx[0] + dr[k]
#             nc = cur_idx[1] + dc[k]
#
#             if nr >= 0 and nr < n and nc >= 0 and nc < m:
#                 if node[nr][nc] == 'L' and visited[nr][nc] == 0:
#                     Q.append((nr, nc, cur_cnt+1))
#                     visited[nr][nc] = 1
#
#                 if node[nr][nc] == 'W':
#                     min_cnt.append(cur_cnt + 1)
#                     return
#
# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     node = [input() for _ in range(n)]
#     min_cnt = []
#     visited = [[0 for _ in range(m)] for _ in range(n)]
#
#
#     for i in range(n):
#         for j in range(m):
#             if node[i][j] == 'L':
#                 bfs(i, j, 0)
#
#     print('#{} {}'.format(tc, sum(min_cnt)))
#


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    node = [input() for _ in range(n)]
    min_cnt = 0
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    Q = []

    for i in range(n):
        for j in range(m):
            if node[i][j] == 'W':
                Q.append((i, j))
                visited[i][j] = 0

    while Q:
        cur = Q.pop(0)
        r = cur[0]
        c = cur[1]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                if node[nr][nc] == 'L' and visited[nr][nc] < 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1






    print('#{} {}'.format(tc, sum(min_cnt)))