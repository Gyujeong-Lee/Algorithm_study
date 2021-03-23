'''
245 -> 245 + 2 + 4 + 5 = 256
=> 245는 256의 생성자

1 ~ N 까지 모든 수를 생성자로 하는 숫자 만들기?
if 만든 수 == N:
list에 넣고
그 중 가장 큰 값을 뽑자


N이 주어졌을 때 가장 작은 생성자를 구하라

가장 작은 생성자 ->

'''

N = int(input())
made_from = list(range(N+1))
create = []

for num in made_from:
    tmp = num
    create.append(num)
    if num < 10:
        tmp += (num % 10)
        if tmp != N:
            create.pop()
    else:
        while num >= 10:
            tmp += (num % 10)
            num = num // 10
            if num < 10:
                tmp += num
                break
        if tmp != N:
            create.pop()
if create:
    print(min(create))
else:
    print(0)


