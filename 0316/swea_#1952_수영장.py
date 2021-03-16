'''
가장 적은 비용으로 수영장을 이용할 수 있는 방법과 그 비용을 구하라
최소비용 찾기

상태 트리 - 재귀 - dfs
아이디어 : 각 달에 모든 방법으로 지불해보고 1년치 최소 비용을 1년권과 비교해본다.
완전 탐색 : 순열
n월에 1달 비용만 내고 n+1월을 고려한다.
n월까지 비용 : s
n-1월까지의 비용 : s
1일 비용 : d
3개월권 비용 : m3
n==12
1년권과 총 비용 비교



1)i-1월의 최소비용 + min(1일권 * 이용일, 1개월 권), i>=1
2) i-3월의 최소비용 + 3개월권, i>= 3
1, 2 중 작은 값
12월까지 비용을 정한 후 1년권과 비교

입력
10
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
'''

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    #1 ~ 12월 이용횟수
    month = list(map(int, input().split()))
    n = len(month)
    #누적 비용
    total = [0] * n
    total_quarter = 0
    min_total = prices[3]

    #이전 달에 추가하는 방식
    for i in range(n):
        if i == 0:
            if month[i] * prices[0] > prices[1]:
                total[i] = prices[1]
            else:
                total[i] = month[i] * prices[0]

        elif month[i] * prices[0] > prices[1]:
            total[i] = total[i-1] + prices[1]

        elif month[i] * prices[0] <= prices[1]:
            total[i] = total[i - 1] + month[i] * prices[0]

        if i >= 2:
            if i == 2:
                if prices[2] < total[i]:
                    total[i] = prices[2]
            else:
                total_quarter = total[i-3] + prices[2]
                if total_quarter < total[i]:
                    total[i] = total_quarter
        
    
    if min_total > total[11]:
        min_total = total[11]

    print('#{} {}'.format(tc, min_total))





