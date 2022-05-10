import heapq
from copy import deepcopy

def heapSort(arr):
    n = len(arr)

    # heap 형태로 데이터를 정렬한다.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # root와 마지막값을 바꿔 정렬하고 바뀐값을 기준으로 다시 heapify
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 노드가 존재하고, 루트보다 더 큰 값일 때
    if left < n and arr[root] < arr[left]:
        root = left

    # 오른쪽 노드가 존재하고, 루트보다 더 큰 값일 때
    if right < n and arr[root] < arr[right]:
        root = right

    # 왼쪽, 오른쪽 자식 노드들과 바꿔줄 위치를 찾았을 때
    if root != i:
        # 찾아낸 값과 swap
        arr[i], arr[root] = arr[root], arr[i]
        # 계속 heap 형태를 갖출 때까지 실행
        heapify(arr, n, root)

a = [50, 80, 150, 260, 210, 150]
b = [50, 80, 150, 260, 210, 150]
c = deepcopy(a)
c.pop()
print(a, c)
heapq.heapify(a)
print(a)
print(type(a))
print(heapSort(b))