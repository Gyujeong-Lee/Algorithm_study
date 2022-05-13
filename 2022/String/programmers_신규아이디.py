special = ['-', '_', '.']


def solution(new_id):
    answer = ''
    # 1, 2, 3단계 : 문자열 길이 상관없이 진행 가능
    new_id = new_id.lower()
    for s in new_id:
        if not s.isalpha() and not s.isdigit():
            if s not in special:
                new_id = new_id.replace(s, "")

    n = len(new_id)
    while n > 1:
        tmp = "." * n
        new_id = new_id.replace(tmp, '.')
        n -= 1

    # 4, 5, 6, 7
    if new_id:
        # 4 - 5 - 6 -7
        tmp = ''
        for i in range(len(new_id)):
            if i == 0 or i == len(new_id) - 1:
                if new_id[i] == '.':
                    continue
            tmp += new_id[i]
        new_id = tmp
        # 이때 빈 문자열 일 수 있음
        if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id[0] == '.':
                new_id = new_id[1:]
            if new_id[-1] == '.':
                new_id = new_id[:14]
        elif len(new_id) == 0:
            new_id = "a" * 3
        elif len(new_id) <= 2:
            tmp = new_id[-1]
            while len(new_id) < 3:
                new_id += tmp

    else:
        # 5단계 - 7단계
        new_id = "a" * 3

    answer = new_id
    return answer