'''
완전 탐색?
각 2에서 모든 1까지 거리 측정
배열 담기
정렬(오름차순)
M개의 거리 총합

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''

#도시치킨거리 구하기 : 각 가정집에서 가까운 치킨집과의 거리
def find(arr):
    dist = 0
    #각 가정집에서 어느 치킨집이 가까운가?
    for i in range(len(house)):
        #최소 거리 비교를 위한 임시변수
        tmp_dist = 10000000
        for j in range(len(group)):
             tmp = abs(house[i][0]-group[j][0]) + abs(house[i][1]-group[j][1])
             if tmp_dist >= tmp:
                 tmp_dist = tmp

        dist += tmp_dist

    return dist

# 조합 알고리즘
def combination(idx):
    global group
    global distance
    result = 0
    #기저 케이스, 재귀 종료, 해당 조합으로 도시치킨거리 구하기
    if len(group) == M:
        # print('조합 : {}'.format(group))
        #도시치킨거리를 위한 함수 (실행 인자로 위치정보가 담긴 arr을 넘겨 받음)
        result = find(group)
        if result <= distance:
            distance = result
        return

    #재귀 호출을 위한 포문
    for i in range(idx, len(hope)):
        if visited[i] != 1:
            group.append(hope[i])
            visited[i] = 1
            combination(i+1)
            visited[i] = 0
            group.pop()


N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))


#1번 좌표 - 가정집
house = []
#2번 좌표 - 치킨집
hope = []

#각 경우의 수, 즉 조합의 도시 치킨 거리 넣기
distance = 1000000000

#1. 치킨집과 가정집 좌표로 배열 만들기.
for i in range(len(city)):
    for j in range(len(city)):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            hope.append([i, j])
            
#
# print('가정집 : {}'.format(house))
# print('치킨집 : {}'.format(hope))

#2. combination으로 M개 뽑아서 경우의 수에 대하여 도시치킨거리 구하기
visited = [0 for _ in range(len(hope))]
group = []
combination(0)
print(distance)






# dx = []
# dy = []

# start = ()
# Q = [start]
# while Q:
#     x, y = Q.pop(0)
#     for i in range(4):
#         now_x = x + d[i]
#         now_y = y + d[i]
#
#         #범위 검사 & visited ㅔㅊ크
#             #visited 처리
#             #q.append

