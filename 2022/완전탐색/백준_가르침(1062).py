'''
시간초과 해결 못함

K가 5 미만이면 무조건 0 출력
'''
base = set(['a', 'n', 't', 'i', 'c'])
max_cnt = 0
def comb(arr, idx, cnt, r):
    global max_cnt
    if cnt == r:
        cur_cnt = 0
        tmp_set = set(arr)
        for k in range(N):
            tmp_set1 = set(words[k])
            if tmp_set1 - tmp_set:
                pass
            else:
                cur_cnt += 1
        if max_cnt < cur_cnt:
            max_cnt = cur_cnt
        return

    for i in range(idx, len(letters)):
        if letters[i] not in arr:
            comb(arr + [letters[i]], i, cnt+1, r)

'''
이 글자들 이외에 글자를 선택 K-5 범위 내에서 - 조합
해당 조합들로 어떤 글자를 읽을 수 있는 지 파악 
'''

N, K = map(int, input().split())
words = []
letters = set()
for i in range(N):
    tmp = input()
    tmp_letter = []
    for l in tmp:
        if l not in base:
            tmp_letter.append(l)

    words.append(tmp_letter)
    letters.update(tmp_letter)
# print(words)
# print(letters)
n = K - 5

if n < 0:
    print(0)
else:
    '''
    1) letters에서 r개를 뽑는 조합 추출함
    2) for N 단어 확인하면서 그 조합으로 만들 수 있는가 검사 
    '''
    letters = list(letters)
    comb([], 0, 0, n)
    print(max_cnt)

