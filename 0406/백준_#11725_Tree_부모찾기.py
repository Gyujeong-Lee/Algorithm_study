'''
루트를 1로 변경하고 각 노드의 부모를 찾아라
7
1 6
6 3
3 5
4 1
2 4
4 7

12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

4 1
-> 1 4
'''
from collections import deque

N = int(input())
#그래프같은 트리
tree = [[] for _ in range(N+1)]

#트리 담기
#연결된 노드
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)


Q = [1]
ans = {}
#방문 검색처럼
check = [False for _ in range(N+1)]

while len(Q) > 0:
    parent = Q.pop(0)
    for i in tree[parent]:
        if not check[i]:
            ans[i] = parent
            Q.append(i)
            check[i] = True

for i in range(2, N+1):
    print(ans[i])





# for i in range(N+1):
#     if len(tree[i]) == 1:
#         parents[i] = tree[i][0]
#         Q.append(i)