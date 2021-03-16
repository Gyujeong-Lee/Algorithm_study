'''
기본적인 dfs 탐색
N*N 배열
가장 높은 봉우리 시작 : 시작점 탐색 (맥스값)
높 -> 낮
가로 또는 세로 / 대각선 불가
한 곳을 정해 최대 K만큼 지형을 깎는다.

A형 문제는 완전 탐색을 하라! 하지만, 불필요한 중복은 삭제하라
A형은 백트래킹을 안해도 할 수 있다.


아이디어
가장 높은 봉우리의 높이 h를 찾는다.
h인 모든 칸에서 시작해본다
인접 칸 중 낮은 칸으로 이동한다(네 방향 탐색)
낮지 않은 칸은 높이차이가 K보다 작고 깎는 횟수가 남아있으면 이동한다.
 - 이미 등산로에 포함된 칸을 깍지 않도록 한다,(visited)
 - 깍은 칸 방향 탐색 후 다른 방향을 탐색할 때 원래 높이를 복원한다. -> 깍기 전 높이를 저장
각 칸에 들어갈 때 마다 가장 킨 등산로와 비교해 최대 길이를 갱신한다.

i,j c(1 or 0) s (이전까지 만든 등산로 길이)
최대 길이 maxV
최대 길이 maxV와 s+1 비교

방문 표시(중복 방문을 허용할 때) : 다른 점에서 온 경우를 위해
한 경로가 끝점을 만나 리턴을 한 뒤 초기화해줘야 한다.
for 문 밖에서 처리


입력
10
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2
1 2 1
2 1 2
1 2 1
'''

#4방향 탐색
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

#dfs 탐색 재귀로

def dfs(i, j, k, s):#행, 렬, 굴삭 여부, 등산로 길이
    global max_len

    # 등산로 길이 +1
    s += 1

    #현재 등산로 길이가 최장 길이보다 크다면 갱신
    if s > max_len:
        max_len = s

    #좌표
    r = i
    c = j

    #4방향 탐색
    for l in range(4):
        nr = r + dr[l]
        nc = c + dc[l]
    #벽에 부딪히지 않았을 때
        if nr >= 0 and nr < N and nc >= 0 and nc < N:
            if hiking[r][c] > hiking[nr][nc] and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr, nc, k, s)
                visited[nr][nc] = 0

            elif hiking[nr][nc] - K < hiking[r][c] and visited[nr][nc] == 0:
                if k == 0:
                    visited[nr][nc] = 1
                    tmp = hiking[nr][nc]
                    hiking[nr][nc] = hiking[r][c] - 1
                    k = 1
                    dfs(nr, nc, k, s)
                    #원상복구
                    visited[nr][nc] = 0
                    k = 0
                    hiking[nr][nc] = tmp




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hiking = [list(map(int, input().split())) for _ in range(N)]

    #시작점 배열
    heights = []
    #최장 등산로
    max_len = 0

    #시작점 찾기
    max_height = 0
    for i in range(N):
        for j in range(N):
            if hiking[i][j] >= max_height:
                max_height = hiking[i][j]

    for i in range(N):
        for j in range(N):
            if hiking[i][j] == max_height:
                heights.append([i, j])

    #dfs 탐색

    for i in range(len(heights)):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[heights[i][0]][heights[i][1]] = 1
        dfs(heights[i][0], heights[i][1], 0, 0)
        #시작점 좌표 + 깍음 여부 + 등산로 길이

    print('#{} {}'.format(tc, max_len))


