'''
그리디
N <= 10
완탐 가능
동전은 오름차순으로

동전의 최소 사용 개수
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
N, changes = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

#나눠 떨어지는 것을 디폴트 값으로 잡아 놓자.
#이후 두번째 탐색에는 뒤에서부터 큰걸로

cnt_default = 100000000000000
for i in range(N-1, -1, -1):
    if changes % coins[i] == 0:
        cnt_default = changes // coins[i]
cnt = 0
for j in range(N-1, -1, -1):
    if changes >= coins[j]:
        cnt += changes // coins[j]
        changes = changes % coins[j]

ans = 0

if cnt_default > cnt:
    ans = cnt
else:
    ans = cnt_default

print(ans)