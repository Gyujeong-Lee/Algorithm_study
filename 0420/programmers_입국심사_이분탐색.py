'''
https://programmers.co.kr/learn/courses/30/lessons/43238
6	[7, 10]	28
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
가장 적은 시간이 걸리는 심사대에서 몇명이 할 지 정한다.
i j k ...
if time[0]*i > time[1] * j
하나씩 줄여감
'''
#입국자
n = int(input())
#입국 심사에 걸리는 시간 (심사관 별)
times = list(map(int, input().split()))

'''
6 0 0 = 42
5 1 0 = 35
4 1 1 = 33
3 2 1 = 21
'''
def solution(n, times):
    answer = 0
    #최솟값이 나올 수 안될만큼 큰 수를 범위로 지정, 하지만 가능한 작게
    #최소 시간을 탐색하기 위한 범위 지정이라고 생각하면 됨
    start, end = 0, max(times) * (n+1)

    while start < end:
        # 중간
        mid = (start + end) // 2
        people_num = 0
        #각 심사관이 몇명을 맞을건지 총 인원수를 구함
        for time in times:
            people_num += mid // time

        #구해진 인원수가 입력 인원보다 크다 => 총 소요 시간은 더욱 적은 시간이어야 함
        if people_num >= n:
            end = mid

        elif people_num < n:
            start = mid + 1

    answer = start
    return answer
