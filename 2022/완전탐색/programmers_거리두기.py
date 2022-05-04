'''
BFS로 푸는 완전 탐색
사실 쌩 구현으로 품
'''

input_places = [["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]
#5칸
#0,0에서 시작하므로 오른쪽, 아래만 검사
dr = [0, 1, 1, 0, 2, -1]
dc = [1, 0, 1, 2, 0, 1]

def bfs(arr):
    flag = True

    for i in range(5):
        for j in range(5):
            #그 외는 검사할 필요 없음
            if arr[i][j] == 'P':
                #이때 주변 5칸 검사
                cur_r = i
                cur_c = j
                for k in range(6):
                    nr = cur_r + dr[k]
                    nc = cur_c + dc[k]

                    if 0 <= nr <= 4 and 0 <= nc <= 4:
                        if arr[nr][nc] == 'P':
                            #이때 파티션 여부에 따라 달라짐
                            if k <= 1:
                                flag = False
                                return flag
                            elif k == 2:
                                if arr[cur_r+1][cur_c] == 'X' and arr[cur_r][cur_c+1] == 'X':
                                    continue
                                else:
                                    flag = False
                                    return flag
                            elif k == 3:
                                if arr[nr][cur_c+1] == 'X':
                                    continue
                                else:
                                    flag = False
                                    return flag
                            elif k == 4:
                                if arr[cur_r+1][nc] == 'X':
                                    continue
                                else:
                                    flag = False
                                    return flag

                            elif k == 5:
                                if arr[cur_r-1][cur_c] == 'X' and arr[cur_r][cur_c+1] == 'X':
                                    continue
                                else:
                                    flag = False
                                    return flag
    return flag


def solution(places):
    '''
    완전탐색
    조건 - 맨하튼 거리 2 이하
    |r1 - r2| + |c1 - c2|
    하지만 파티션 섞인 경우 ㄱㅊ

    1) P1 8방향 M 2이하인 P2
    2) X가 있는 경우, cnt -1
    '''

    n = len(places)
    answer = [0 for _ in range(n)]

    for i in range(n):
        if bfs(places[i]):
            answer[i] = 1
    return answer

print(solution(input_places))

