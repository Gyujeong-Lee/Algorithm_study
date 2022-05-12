'''
str1 = ' abc'
str2 = 'abbb'
인 경우 출력 값이 16384가 나와야 합니다.

만약 21845값이 나온다면 합집합 로직의 문제 입니다.
합집합 = ['ab', 'bc', 'bb', 'bb'] (o)
합집합 = ['ab', 'bc', 'bb'] (x)
'''

import math

st1 = ' abc'
st2 = 'abbb'

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str_list1 = []
    str_list2 = []
    for i in range(len(str1) - 1):
        tmp = str1[i:i + 2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            str_list1.append(tmp)

    for j in range(len(str2) - 1):
        tmp = str2[j:j + 2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            str_list2.append(tmp)

    print(str_list1, str_list2)

    # 일반 교집합
    tmp_set1 = set(str_list1) & set(str_list2)
    # 일반 합집합
    tmp_set2 = set(str_list1) | set(str_list2)
    set1 = []
    set2 = list(tmp_set2)

    # 다중 교집합 및 합집합 고려
    for s1 in tmp_set1:
        x = str_list1.count(s1)
        y = str_list2.count(s1)
        # 다중 교집합
        cnt1 = min(x, y)
        cnt2 = max(x, y)
        set2.remove(s1)
        for i in range(cnt1):
            set1.append(s1)
        for j in range(cnt2):
            set2.append(s1)

    for s2 in tmp_set2:
        if not s2 in tmp_set1:
            if s2 in str_list1:
                x = str_list1.count(s2)
                for i in range(x-1):
                    set2.append(s2)
            if s2 in str_list2:
                x = str_list2.count(s2)
                for i in range(x-1):
                    set2.append(s2)

    print(set1, set2)

    if len(set2) == 0:
        answer = 65536
    else:
        answer = math.floor((len(set1) / len(set2)) * 65536)
    return answer

print(solution(st1, st2))