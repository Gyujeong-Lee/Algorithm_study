from collections import deque
# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# n = len(board)
# #이동 방향 상하좌우 네 방향
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# #목적지 도달 시 비교 후 최신화
# min_cost = 10000000000000000000000000
#
# #x축, y축, 비용, 방향
# def dfs(x, y, c, dr):
#     global min_cost
#     old_dr = dr
#     #첫 방문처리
#     if x == 0 and y == 0:
#         board[x][y] = 1
#
#     #기저조건
#     if x == n-1 and y == n-1:
#         if c < min_cost:
#             min_cost = c
#         return
#     #가지치기 이미 같거나 클 때 더 해볼 필요 x
#     if c >= min_cost:
#         return
#
#     #네 방향 재귀로 돌림
#     for i in range(4):
#         #다음 나아갈 방향
#         nx = x + dx[i]
#         ny = y + dy[i]
#         #보드 안에 존재
#         if 0 <= nx <= n-1 and 0 <= ny <= n-1:
#             #다음 갈 곳이 방문하지 않았고 막혀있지 않을 때
#             if board[nx][ny] != 1:
#                 #1) 비용계산, 2) 방문처리, 3) 재귀호출
#                 #코너, 직선 검사 0의 idx가 같은지 다른지
#                 now_dr = [dx[i], dy[i]]
#                 #출발지점 - 무조건 직선 비용
#                 if old_dr == [0, 0]:
#                     board[nx][ny] = 1
#                     dfs(nx, ny, c+100, now_dr)
#                     board[nx][ny] = 0
#                 #코너
#                 elif now_dr.index(0) != old_dr.index(0):
#                     board[nx][ny] = 1
#                     dfs(nx, ny, c+600, now_dr)
#                     board[nx][ny] = 0
#                 #직선
#                 else:
#                     board[nx][ny] = 1
#                     dfs(nx, ny, c+100, now_dr)
#                     board[nx][ny] = 0
#
# dfs(0, 0, 0, [0,0])
# print(min_cost)

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
n = len(board)
dp = [[10000000000000000 for _ in range(n)] for _ in range(n)]
#이동 방향 상하좌우 네 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#목적지 도달 시 비교 후 최신화
min_cost = 10000000000000000000000000

#시작점 삽입 -> 반복문 -> 삽입, 삭제 반복
#stack
#que

q = deque([(0, 0, 0, [0,0])])

while q:
    x, y, c, old_dir = q.popleft()

    if x == 0 and y == 0:
        board[x][y] = 1
    # 기저조건
    if x == n-1 and y == n-1:
        if c < min_cost:
            min_cost = c
        continue

    #굳이 더 돌 필요가 없음
    elif c >= min_cost:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        new_dir = [dx[i], dy[i]]
        add_c = 0
        if old_dir == [0, 0]:
            add_c = 100
        elif old_dir.index(0) != new_dir.index(0):
            add_c = 600
        else:
            add_c = 100

        if not (0 <= nx <= n-1 and 0 <= ny <= n-1) or board[nx][ny] == 1:
            continue
        if dp[nx][ny] < c + add_c:
            continue
        dp[nx][ny] = c + add_c
        q.append((nx, ny, c + add_c, new_dir))

print(min_cost)
