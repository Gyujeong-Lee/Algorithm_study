'''
몇개의 바람개비를 돌릴 수 있나

2차원 배열
벽 6
선풍기 5
빈칸 0
바람개비 그 외 정수(임계치)

완전탐색
'''
from itertools import combinations
from copy import deepcopy
#Sample
grid1 = [[0, 0, 5, 0, 1], [0, 0, 0, 0, 1], [1, 2, 3, 5, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
to_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check(arr, dr, s):
    new_grid = deepcopy(arr)
    l = len(new_grid)
    n = len(dr)
    result = [[False for _ in range(l)] for _ in range(l)]

    for i in range(n):
        #방향 바꿀 fan의 좌표
        fan_r, fan_c = s[i][0], s[i][1]
        idx = dr[i]
        nr, nc = to_dir[idx][0], to_dir[idx][1]
        # print(fan_r, nr, fan_c, nc)
        while 0 <= fan_r + nr < l and 0 <= fan_c + nc < l:
            next_r, next_c = fan_r+nr, fan_c+nc
            if 0 < new_grid[next_r][next_c] and new_grid[next_r][next_c] != 5 and new_grid[next_r][next_c] != 6:
                new_grid[next_r][next_c] -= 1

                if new_grid[next_r][next_c] == 0:
                    result[next_r][next_c] = True
            if new_grid[next_r][next_c] == 6:
                break

            fan_r = next_r
            fan_c = next_c
    cnt = 0
    for i in range(l):
        for j in range(l):
            if result[i][j]:
                cnt += 1

    return cnt

def solution(grid):
    answer = 0
    n = 0
    start = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 5:
                n += 1
                start.append((i, j))

    # 0: 동, 1: 서, 2: 남, 3: 북
    direction = [i for i in range(4)] * n
    dir_comb = list(combinations(direction, n))

    for idx_comb in dir_comb:
        cnt = check(grid, idx_comb, start)
        if cnt > answer:
            answer = cnt

    return answer



print(solution(grid1))