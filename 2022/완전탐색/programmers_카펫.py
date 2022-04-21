'''
카펫 세로, 가로 구하기
1) 테두리는 브라운 ( 8 ~ 5000 )
2) 그 외 옐로우 ( 1 ~ 2000000 )
-> 브라운과 옐로우 개수가 주어질 때 전체 길이를 구하라
항상 가로가 세로보다 길거나 같다.
'''

input_brown = int(input())
input_yellow = int(input())

def divide(x):
    arr = []
    for i in range(1, x):
        if x % i == 0:
            tmp = x // i
            if (i, tmp) not in arr and (tmp, i) not in arr:
                arr.append((i, tmp))
    return arr

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    #토탈의 약수 중 3 이상으로 이루어진 것 중 하나
    #1) x, y 쌍 추출
    tup = divide(total)
    # 2) 그 중 아래 식을 성립하는 약수 쌍 찾기
    #(x-2)*(y-2) = yellow
    for i in range(len(tup)):
        tmp = tup[i]
        #가로가 항상 더 큼
        tmp_x = tmp[1]
        tmp_y = tmp[0]
        if (tmp_x - 2) * (tmp_y - 2) == yellow:
            answer.append(tmp_x)
            answer.append(tmp_y)

    return answer

print(solution(input_brown, input_yellow))