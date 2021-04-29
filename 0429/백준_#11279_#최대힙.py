'''
x = 자연수 배열에 추가
x = 0 가장 큰 값 출력 후 삭제
'''
import heapq
from sys import stdin

N = int(input())
que = []

for i in range(N):
    x = int(stdin.readline())

    if x == 0:
        if len(que) > 0:
            print(-heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, -x)
