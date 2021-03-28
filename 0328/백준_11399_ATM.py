'''
N명의 사람들이 각각 인출할 때 소요되는 시간이 리스트로 주어짐
누적 합을 시켰을 때 최솟값을 구하라
오름차순 정렬시키면 됨
입력
5
3 1 4 3 2
'''

N = int(input())
arr = list(map(int, input().split()))

#1오름차순 정렬
#선택정렬
for i in range(len(arr)-1):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]

# print(arr)

#2누적합 N이 1000까지 가므로 재귀로 못품
ans = 0

for i in range(len(arr)):
    for j in range(i+1):
        ans += arr[j]
print(ans)




















#재귀
# ans = 0
# def recursion(idx, total):
#     global ans
#     if idx == len(arr):
#         ans = total
#         return
#
#     for k in range(idx+1):
#         total += arr[k]
#
#
#     idx += 1
#     recursion(idx, total)
#
# recursion(0, 0)
# print(ans)


