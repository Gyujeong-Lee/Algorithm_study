'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
#노드 개수
N = int(input())
edge = []
for _ in range(N-1):
    edge.append(list(map(int, input().split())))

tree = [0] * (N+1)
sub_root = 0

for i in range(N-1):
    if edge[i][1] == 1:
        edge[i][0], edge[i][1] = edge[i][1], edge[i][0]
        sub_root = edge[i][1]

for j in range(N-1):
    if edge[j][0] != 1 and edge[j][1] == sub_root:
        edge[j][0], edge[j][1] = edge[j][1], edge[j][0]

    tree[edge[j][1]] = edge[j][0]

for node in tree:
    if node:
        print(node)
