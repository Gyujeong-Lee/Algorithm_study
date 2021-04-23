'''
그룹 나누기와 유사한 문제
idea : 서로소집합 or 트리의 깊이 or 랭크

2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edge = []
    p = [i for i in range(N + 1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        #n2의 대표원소를 n1으로 결정
        p[find_set(n2)] = find_set(n1)

    cnt = 0
    for i in range(1, N+1):
        if p[i] == i:
            cnt += 1

    print('#{} {}'.format(tc, cnt))




