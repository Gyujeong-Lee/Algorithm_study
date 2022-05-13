#1차 코드 시간 초과
# from collections import deque
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# #n이 행, m이 열
# m, n = map(int, input().split())
# arr = []
# #전체 토마토 개수
# total = 0
# #익은 토마토가 있는 곳
# rc_list = []
# not_yet = []
#
# q = deque([])
# visited = [[1e9 for _ in range(m)] for _ in range(n)]
# #1: 익은 토마토 / 0 : 안익은 토마토 / -1 비어있음
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#     for j in range(m):
#         if arr[i][j] == 1 or arr[i][j] == 0:
#             total += 1
#             if arr[i][j] == 1:
#                 rc_list.append((i, j))
#                 q.append((i, j, 0))
#             else:
#                 not_yet.append((i, j))
# #원래 모든 토마토가 익은 경우
# if total == len(rc_list):
#     print(0)
# else:
#     flag = True
#     min_date = -1
#     while q:
#         cur_r, cur_c, cur_day = q.popleft()
#         for k in range(4):
#             nr = cur_r + dr[k]
#             nc = cur_c + dc[k]
#             if 0 <= nr < n and 0 <= nc < m:
#                 if visited[nr][nc] > cur_day + 1:
#                     visited[nr][nc] = cur_day + 1
#                     q.append((nr, nc, cur_day+1))
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j] == 1e9:
#                 if (i, j) in not_yet:
#                     flag = False
#             else:
#                 if visited[i][j] > min_date:
#                     min_date = visited[i][j]
#     if flag:
#         print(min_date)
#     else:
#         print(-1)

# 2차코드
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for row in matrix:
    for j in row:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(row))
print(res - 1)