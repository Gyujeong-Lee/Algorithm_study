'''
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	14332	5067	3711	37.809%
문제
세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1 ~ N 시작한다.
1 * 1 = 1  1
1 * 2 = 2  2
1 * 3 = 3  3
1 * N
idx = N
...
2 * 1 = 2  4
2 * 2 = 4  5
2 * 3 = 6  6
2 * N
idx = 2N

3 * 1 = 3
3 * 2 = 6
3N
4N
5N
...
N * N
B = [1 2 2 3 3 4 4 5 5 6 6 7 7 .. N*N]
'''
def binary_search(s, f):
    m = (s+f) // 2
    pass

N = int(input())
k = int(input())
B = []
for i in range(1, N+1):
    for j in range(1, N+1):
        B.append(i*j)

binary_search(0, N*N-1)


