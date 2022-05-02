

scoville = [2, 1, 3, 9, 10, 12]
K = 7
answer = 0
#가장 작은 음식 두 개 섞어서 하나의 음식 만들기
'''
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
'''
import heapq

#heap으로 변환
heapq.heapify(scoville)
print(scoville)
while scoville[0] < K:
    if len(scoville) < 2:
        answer = -1
        break

    min_1 = heapq.heappop(scoville)
    min_2 = heapq.heappop(scoville)

    new = min_1 + min_2*2
    heapq.heappush(scoville, new)

    answer += 1

print(answer)


