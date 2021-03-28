'''
2 162
5
4 42
-1
100 40021
5
2를 곱하거나 수 마지막에 1을 더하거나

마지막 자리가 짝수라면 2로 나누고 홀수라면 1을 제외한 나머지 수를 출력
40021
4002
2001
200
100
'''

A, B = input().split()
cnt = 0

while True:
    n = len(B)

    if n > 1 and B[-1] == '1':
        B = B[:n-1]

    elif int(B) % 2 == 0:
        B = str(int(B) // 2)

    else:
        cnt = -1
        break
    cnt += 1

    if A == B:
        cnt += 1
        break

print(cnt)