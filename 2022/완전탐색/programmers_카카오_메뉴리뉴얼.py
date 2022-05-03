'''
조합 문제이나
한 시간이 소요된듯..
Lambda 식을 공부할 필요성을 많이 느낌
'''

result = {}


def comb(order, idx, r, cnt, ch):
    global result
    l = len(order)

    if r == cnt:
        # print(ch)
        tmp_li = sorted(ch)
        tmp = ''.join(tmp_li)
        if not result.get(tmp):
            result[tmp] = 1
        else:
            result[tmp] += 1

        return
    for i in range(idx, l):
        comb(order, i + 1, r, cnt + 1, ch + order[i])


def solution(orders, course):
    '''
    2가지 이상 단품
    각 단품은 최소 2명 이상 주문
    '''

    for n in course:
        for i in range(len(orders)):
            comb(orders[i], 0, n, 0, '')

    answer = []

    for n in course:
        tmp = list(filter(lambda x: x[1] > 1 and len(x[0]) == n, result.items()))
        if tmp:
            tmp_max = max(tmp, key=lambda x: x[1])

        for x in tmp:
            if x[1] == tmp_max[1]:
                answer.append(x[0])
    answer.sort()

    return answer