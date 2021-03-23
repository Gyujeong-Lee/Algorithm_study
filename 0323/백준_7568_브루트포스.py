'''
N명의 사람을 순서대로 덩치 순위 출력하기
5
55 185
58 183
88 186
60 175
46 155

한 사람씩 다른 사람과 덩치를 비교하며 그 사람보다 큰 사람이 몇명인지 계산한다.
'''
N = int(input())
spec = [list(map(int, input().split())) for _ in range(N)]
ranks = []

for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j:
            if spec[i][0] < spec[j][0] and spec[i][1] < spec[j][1]:
                cnt += 1
    ranks.append(cnt+1)

for rank in ranks:
    print(rank, end=' ')
print()
