import heapq

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


def solution(infos, queries):
    # 이중 반복 x
    # hash 및 이진탐색
    answer = []

    info_dict = {}
    # 경우의 수 정리
    language = ['cpp', 'java', 'python', '-']
    position = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']

    # 최대 4 * 3 * 3 * 3 = 108
    for l in language:
        for p in position:
            for c in career:
                for f in food:
                    info_dict[l + p + c + f] = []

    # On = n * 4 = c최대 20만
    for info in infos:
        info = info.split(' ')
        for l in (info[0], '-'):
            for p in (info[1], '-'):
                for c in (info[2], '-'):
                    for f in (info[3], '-'):
                        info_dict[l + p + c + f].append(int(info[4]))

    # On 최대 108 * 100,000 = 천만 이하인데..
    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()

        query_score = int(query[1])
        query = query[0]

        info_score = heapSort(info_dict[query])  # 시간초과가 나는 이유
        # print(info_score)
        l = len(info_score)
        tmp = l

        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if query_score <= info_score[mid]:
                tmp = mid
                high = mid - 1

            else:
                low = mid + 1

        answer.append(l - tmp)

    return answer