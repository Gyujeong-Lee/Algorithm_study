orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] #10, #20
course = [2,3,4] #10개
comb_dict = {}
combi = []

#가장 큰 경우의 수를 갖고 조합을 짬
#딕셔너리를 통해 조합 카운트
#카운트 2이상
def comb(s, cnt, r, l):
    #저장
    if cnt in course:
        str_combi = ''.join(combi[:cnt])
        # print(str_combi)
        if comb_dict.get(str_combi):
            comb_dict[str_combi] += 1
        else:
            comb_dict[str_combi] = 1
    #종료
    if cnt == r:
        return
    #조합로직
    for i in range(s, l):
        combi[cnt] = order[i]
        comb(i+1, cnt+1, r, l)

for order in orders:
    n = len(order)
    if n >= course[-1]:
        combi = ['' for _ in range(course[-1])]
        #course의 최댓값을 r로 조합 돌리기
        comb(0, 0, course[-1], len(order))
    elif n >= course[0]:
        combi = ['' for _ in range(len(order))]
        #n을 r로 조합을 돌리기
        comb(0, 0, n, len(order))
    else:
        continue
#
print(comb_dict)
for key, value in comb_dict.items():
    if value >= 2:
        print(key)