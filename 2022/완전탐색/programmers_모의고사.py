'''
1, 2, 3 사람
찍는 방식
1) '12345'*n        // 5
2) '21232425'*n       // 8
3) '33 11 22 44 55' (3 1 2 4 5) 두번씩  // 10
누가 가장 많이 맞췄냐

answers 길이 10,000
'''

input_answer = list(map(int, input().split(',')))


def solution(answers):
    answer = []

    n = len(answers)
    answer_a = '12345' * (n//5) + '12345'[:(n%5)]
    answer_b = '21232425' * (n//8) + '21232425'[:(n%8)]
    answer_c = '3311224455' * (n//10) + '3311224455'[:(n%10)]

    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    for i in range(n):
        correct = str(answers[i])
        if answer_a[i] == correct:
            cnt_a += 1

        if answer_b[i] == correct:
            cnt_b += 1

        if answer_c[i] == correct:
            cnt_c += 1

    tmp_answer = [cnt_a, cnt_b, cnt_c]
    max_cnt = -100000000
    # print(cnt_a, cnt_b, cnt_c)
    for i in range(3):
        if tmp_answer[i] > max_cnt:
            max_cnt = tmp_answer[i]
            answer = [i+1]

        elif tmp_answer[i] == max_cnt:
            max_cnt = tmp_answer[i]
            answer.append(i+1)

    return answer


print(solution(input_answer))