'''
다익스트라 N번?
D1 : 1번에서 나가는 정점들의 비용
D2 : 1번에 도착하는 정점의 비용
인접행렬의 행 : 출발
인접행렬의 열 : 도착 -> 행으로 변환 시켜서 D2로 사용
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''
import heapq
def dijkstra(node, graph, dist):
    global inf

    #거리
    D = [inf for _ in range(V + 1)]
    #시작점 본인
    D[node] = 0

    #방문 체크
    U = [0 for _ in range(V+1)]
    U[node] = 1

    que = []
    #우선순위 큐, 힙큐 사용
    heapq.heappush(que, (node, dist))

    while len(que) > 0:
        #자동 정렬 후 가장 작은 것을 끄냄
        cur = heapq.heappop(que)
        cur_node = cur[0]
        cur_dist = cur[1]

        #인접한 노드 거리 계산 후 작으면 삽입
        for i in range(1, V+1):
            if graph[cur_node][i] < inf and U[i] == 0:
                new_node = i
                new_dist = cur_dist + graph[cur_node][new_node]
                if D[new_node] > new_dist:
                    D[new_node] = new_dist
                    # U[cur_node] = 1
                    heapq.heappush(que, (new_node, new_dist))

    return D

T = int(input())
for tc in range(1, T+1):
    V, E, X = map(int, input().split())
    inf = 10000000000000000000000000
    #출발지를 행으로 갖는 인접행렬
    adj_list = [[inf for _ in range(V+1)] for _ in range(V+1)]
    #도착지를 행으로 갖는 인접행렬 X번만 쓸거임
    adj_list2 = [[inf for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        s, f, w = map(int, input().split())
        adj_list[s][f] = w
        adj_list2[f][s] = w

    #x출발
    from_X = dijkstra(X, adj_list, 0)
    #X도착
    to_X = dijkstra(X, adj_list2, 0)
    max_dist = 0

    #왕복 거리 중 가장 큰 값
    for i in range(1, V+1):
        tmp = from_X[i] + to_X[i]
        if max_dist < tmp:
            max_dist = tmp

    print('#{} {}'.format(tc, max_dist))

