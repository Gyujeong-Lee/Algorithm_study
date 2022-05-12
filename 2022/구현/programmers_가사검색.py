'''
해쉬맵
이진탐색
memoization
으로 효율성 극복
하지만 효율성 테케 2번 통과 못함

느낀점 : 어려운 알고리즘을 써야하는 경우도 있으나
생각만 잘하면 풀 수 있는 수준이다.
'''

def binary_search(arr, query, n):
    cnt = 0
    new_qeury = ''
    s, f = 0, n - 1

    # 접두사
    if query[0] == '?':
        while s <= f:
            mid = (s + f) // 2
            if query[mid] == '?' and query[mid + 1] != '?':
                mid += 1
                break
            elif query[mid] == '?':
                s = mid + 1
            else:
                f = mid - 1

        new_query = query[mid:]
        for word in arr:
            if new_query == word[mid:]:
                cnt += 1
    # 접미사
    else:
        while s <= f:
            mid = (s + f) // 2
            if query[mid] == '?':
                f = mid - 1
                if query[f] != '?':
                    break
            else:
                s = mid + 1

        new_query = query[:mid]
        for word in arr:
            if new_query == word[:mid]:
                cnt += 1
    return cnt


def solution(words, queries):
    '''
    효율성 때문에 어려울듯
    10만 * 10만
    = 100억 + a (문자열 검색한다면 시간복잡도 증가)
    해결책
    해쉬맵 - 길이 별 목록 정리
    이진탐색 - ? 끝 자리를 확인함으로써 검사 범위 확인
    result 배열에 query를 저장해 같은 쿼리를 재탐색하지 않게함 (효율성 테케 1 )
    '''
    answer = []
    result = []
    # Hash Map - word 길이 별로 담아둘 것
    word_dict = {}
    # 쿼리 돌면서 길이에 맞는 리스트만 이진탐색
    for word in words:
        l = len(word)
        if not word_dict.get(l):
            word_dict[l] = [word]
        else:
            word_dict[l].append(word)

    for query in queries:
        l = len(query)
        if query in result:
            idx = result.index(query)
            tmp = answer[idx]
            result.append(query)
            answer.append(tmp)
            continue
        if query.count('?') == l:
            if word_dict.get(l):
                answer.append(len(word_dict[l]))
            else:
                answer.append(0)
        elif word_dict.get(l):
            answer.append(binary_search(word_dict[l], query, l))
        else:
            answer.append(0)

        result.append(query)

    return answer