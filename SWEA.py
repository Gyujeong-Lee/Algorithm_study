'''

Sample Input
5
6 4 5
0 1 2 3 4 7
1 2 3 4
5
3 1 4
1 6 5
1
0
7 3 6
1 8 0 2 6 7 9
2 1 4
91
5 2 10
4 0 5 3 9
3 4
28
5 3 1O
8 7 1 2 6
2 4 3
981	// 테스트 케이스 수는 5개
// 테스트 케이스 1 시작, N=6, O=4, M=5
// ‘0’, ‘1’, ‘2’, ‘3’, ‘4’, ‘7’ 입력 가능
 // ‘+’, ‘-‘, ‘*’, ‘/’ 입력 가능
// 원하는 숫자 5s
// 테스트 케이스 2 시작
// ‘+’ 입력 가능

// 테스트 케이스 3 시작

// ‘-‘, ‘+’, ‘/’ 입력 가능

// 테스트 케이스 4 시작

// ‘*‘, ‘/’ 입력 가능

// 테스트 케이스 5 시작

// ‘-’, ‘/’, ‘*’ 입력 가능
'''

T = int(input())

for tc in range(1, T+1):
    #터치 가능한 숫자 수 / 가능 연산자 수 / 터치 가능 횟수
    N, O, M = list(map(int, input().split()))
    #N
    enable_num = list(map(int, input().split()))
    #O
    #1 : + / 2: - / 3: * /4: // /
    enable_operator = list(map(int, input().split()))
    #원하는 숫자
    need_num = int(input())

    answer = -1
    print(enable_operator)
