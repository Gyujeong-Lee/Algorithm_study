'''
price	money	count	result
3	20	4	10
'''


def solution(price, money, count):
    answer = -1
    total_cost = 0
    for i in range(1, c+1):
        total_cost += (p * i)
    answer = total_cost - money

    if answer <= 0:
        answer = 0


    return answer


p, m, c = map(int, input().split())
ans = solution(p, m, c)

print(ans)