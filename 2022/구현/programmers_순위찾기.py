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

    # On = n * 4
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

        info_score = sorted(info_dict[query])  # 시간초과가 나는 이유
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

