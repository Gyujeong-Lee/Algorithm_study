'''
다익스트라 알고리즘
'''

import heapq


# 다익스트라
# 그래프(인접리스트), 거리, 큐
def dijkstra(graph, start, v):
    INF = int(1e9)
    costs = [INF for _ in range(v + 1)]  # 정점 별 거리
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0

    while q:
        cur_cost, cur_node = heapq.heappop(q)
        adj_nodes = graph[cur_node]

        # 진행할 필요가 없음, 이전 방문했을 때가 보다 경제적임
        if costs[cur_node] < cur_cost:
            continue

        for new in adj_nodes:
            new_node, new_cost = new[0], new[1]
            # 인접 노드 이동 시 비용
            transfer_cost = costs[cur_node] + new_cost
            # 새로운 방법이 기존 방법보다 작을 때
            if transfer_cost < costs[new_node]:
                costs[new_node] = transfer_cost
                heapq.heappush(q, (transfer_cost, new_node))
    # print(costs)
    return costs


# 정점개수, 출발지점, A도착, B도착, 금액(v1, v2, cost)
def solution(n, s, a, b, fares):
    # 1. S 시작 A, B, M(최소 정점)
    # 2. M 시작 A, B
    # S->M->(A+B) vs S->A + S->B

    adj_list = {key: [] for key in range(1, n + 1)}
    for edge in fares:
        n1, n2, cost = edge[0], edge[1], edge[2]
        adj_list[n1].append((n2, cost))
        adj_list[n2].append((n1, cost))

    # print(adj_list)
    # step1
    result1 = dijkstra(adj_list, s, n)
    print(result1)
    answer = result1[a] + result1[b]
    total_cost = int(1e9)
    # step2
    for i in range(1, n + 1):
        if i != 0 and i != s:
            mid_cost = result1[i]
            result2 = dijkstra(adj_list, i, n)
            mid_to_a = result2[a]
            mid_to_b = result2[b]
            if total_cost > mid_cost + mid_to_a + mid_to_b:
                total_cost = mid_cost + mid_to_a + mid_to_b

    if answer > total_cost:
        answer = total_cost

    return answer