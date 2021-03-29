'''
동물원
5
0 1 2 3 4


2
5 8

6
0 0 0 0 0 0

5
1 0 2 0 1

0 0 1 1 2



3
1 0 1
'''
def find():
    global ans
    #정렬
    for i in range(n - 1):
        min_idx = i
        for j in range(i, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    #최댓값이랑
    max_num = arr[n-1]
    #중복된 숫자 중 최댓값
    sub_num = -1

    for num in arr:
        if arr.count(num) == 2:
            sub_num = num

        if arr.count(num) > 2:
            return


    #분기 처리 하면서 경우의 수를 구하기
    if max_num >= N or sub_num >= N:
        return

    #중복된 숫자가 없을 때
    if sub_num == -1:
        #중복된 숫자가 없지만, 경우의 수가 존재할 때
        if arr == list(range(max_num+1)):
            #0 1 2 max_num = 2 -> list = [0, 1, 2]
            ans = 2
            return
        else:
            return
    #1 1 2 3 / n = 7 max_num = 5+1 sub_num = 0+1 // 7
    elif max_num+1 + sub_num+1 == N:

        if max_num == sub_num:
            ans = 2 ** (sub_num + 1)
            return
        else:
            ans = (2 ** (sub_num + 1)) * 2
            return



N = int(input())
arr = list(map(int, input().split()))
n = len(arr)
ans = 0
find()
print(ans)