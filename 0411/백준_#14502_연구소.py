'''
idea
모든 0에 벽을 세워보자
세개씩

BFS or DFS로 바이러스 확인 후 개수 세기

리스트에 담고 최저값 구하기
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
'''

#조합 알고리즘은 치킨집 참고(0410)
from itertools import combinations

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    global result
    global copy_lab

    #안전구역 세기
    cnt = 0

    # bfs 구현을 위한 Q
    Q = []
    for i in range(len(virus)):
        Q.append(virus[i])

    while Q:
        cur = Q.pop(0)
        r = cur[0]
        c = cur[1]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < N and nr >= 0 and nc < M and nc >= 0:
                if copy_lab[nr][nc] == 0:
                    Q.append([nr, nc])
                    copy_lab[nr][nc] = 2

    for row in copy_lab:
        cnt += row.count(0)

    result.append(cnt)

#세로, 가로
N, M = map(int, input().split())
#연구실
lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))

#빈 공간
empty = []
#바이러스 진원지
virus = []

#바이러스와 벽이 들어갈 수 있는 빈 공간 좌표 확인
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append([i, j])
        elif lab[i][j] == 2:
            virus.append([i, j])

#조합 내장메서드 사용 시 주소 반환됨
locations = list(combinations(empty, 3))

#순회 결과 담기
result = []

#리스트 안에 튜플 안에 좌표 저장되어있음
for tup in locations:
    # 원본 리스트를 보존하고 다른 경우의 수를 탐색하기 위해
    copy_lab = lab
    for i in range(len(tup)):
        copy_lab[tup[i][0]][tup[i][1]] = 1
    bfs()
    #다음 검사를 위한 초기화
    for j in range(len(tup)):
        copy_lab[tup[j][0]][tup[j][1]] = 0

print(max(result))