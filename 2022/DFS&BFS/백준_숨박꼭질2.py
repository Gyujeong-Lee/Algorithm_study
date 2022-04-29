'''
Runtime Error 나옴
수빈이 위치 N / 동생 위치 K
찾는 방법
+1 / -1 / * 2
BFS로 다시 풀 것

'''
from collections import deque

N, K = map(int, input().split())
# [0] = 방문거리 / [1] = 방문횟수
visited = [[-1, 0] for _ in range(100001)]
visited[N][0] = 0
visited[N][1] = 1
q = deque([N])

while q:
    cur = q.popleft()

    if cur == K:
        break

    for nx in (cur-1, cur+1, cur*2):
        if 0 <= nx <= 100000:
            #첫방문
            if visited[nx][0] == -1:
                visited[nx][0] = visited[cur][0] + 1
                visited[nx][1] = visited[cur][1]
                q.append(nx)
            elif visited[nx][0] >= visited[cur][0] + 1:
                visited[nx][1] += visited[cur][1]

print(visited[K][0])
print(visited[K][1])