id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
N = len(id_list)

report_list = [set() for _ in range(N)]
report_cnt = {}
block_user = []
answer = [0 for _ in range(N)]
for i in range(len(report)):
    reporter = report[i].split(' ')[0]
    reported = report[i].split(' ')[1]
    tmp_idx = id_list.index(reporter)
    report_list[tmp_idx].add(reported)

for i in range(N):
    report_cnt[id_list[i]] = 0

for key in report_cnt.keys():
    for i in range(N):
        if key in report_list[i]:
            report_cnt[key] += 1
    if report_cnt[key] >= k:
        block_user.append(key)

for i in range(N):
    cnt = 0
    for j in range(len(block_user)):
        if block_user[j] in report_list[i]:
            cnt += 1
    answer[i] = cnt
print(answer)
#신고자가 몇 번의 정지 결과 이메일을 받는가
#1) 신고자 : [피신고자] (중복 제거)
#2) 그 다음 카운트
#3) 정지된 인원 목록 추출
#4) 신고자 : [피신고자] 목록 중 몇명이나 정지된 인원인지 확인


