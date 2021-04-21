'''
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
5
2 1 2 6 2 4 3 3

3,4,2,1,5
'''
n = int(input())
arr = list(map(int, input().split()))
num_game = [0 for _ in range(n+1)]
num = [0 for _ in range(n+1)]
ratio = {}

N = len(arr)
for i in range(N):
    if arr[i] > n:
        for j in range(1, n+1):
            num_game[j] += 1
    else:
        num[arr[i]] += 1
        for j in range(1, arr[i]+1):
            num_game[j] += 1

for i in range(n+1):
    if i >= 1:
        if num_game[i]:
            ratio[i] = num[i] / num_game[i]
        else:
            ratio[i] = 0
ans = sorted(ratio.items(), key=lambda x: x[1], reverse=True)
answer = []
for i in range(len(ans)):
    answer.append(ans[i][0])

print(ratio)
print(answer)

