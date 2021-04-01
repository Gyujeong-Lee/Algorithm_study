'''
첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.

이분탐색
start finish
반을 나눠서 크면
0부터 36
18 제곱
0부터 18
9의 제곱
0부터 9
4의 제곱
4부터 9
6의 제곱

'''

N = int(input())
start = 0
finish = N
while True:
    mid = (finish + start) // 2
    if mid**2 > N:
        finish = mid
    elif mid**2 < N:
        start = mid
    else:
        print(mid)
        break

