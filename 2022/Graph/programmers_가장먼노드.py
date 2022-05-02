from collections import deque
input_n = int(input())
input_edge = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]

def bfs(dict, s, k):
    dist_list = [0 for _ in range(k+1)]
    dist_list[s] = 1
    dist = 0
    q = deque([])
    q.append([s, dist])

    while q:
        tmp = q.popleft()
        cur_node, cur_dist = tmp[0], tmp[1]
        adj_nodes = dict[cur_node]

        for i in range(len(adj_nodes)):
            new_node = adj_nodes[i]
            if dist_list[new_node] == 0:
                # print(cur_node, new_node)
                dist_list[new_node] = cur_dist + 1
                q.append([new_node, cur_dist+1])
                # print(dist_list)

    return dist_list


def solution(n, edge):
    adj_list = {}

    for i in range(len(edge)):
        n1 = edge[i][0]
        n2 = edge[i][1]
        if not adj_list.get(n1):
            adj_list[n1] = [n2]
        else:
            adj_list[n1].append(n2)

        if not adj_list.get(n2):
            adj_list[n2] = [n1]
        else:
            adj_list[n2].append(n1)
    # print(adj_list)
    result = bfs(adj_list, 1, n)
    print(result)
    max_dist = max(result)

    answer = result.count(max_dist)
    if max_dist == 1:
        answer -= 1
    return answer

print(solution(input_n, input_edge))
