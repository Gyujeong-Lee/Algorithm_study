# n-2번째 배차시간 ~ n-1번째 배차시간 사이의 timetable 값의 개수
# m과 비교
# m 이상
# 그 중 몇 명이 못타는지 분류
# min값보다 -1
# m 이하
# 마지막 배차 (n-1)
n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
answer = ""
#9시
s = 540
last = s + (n-1)*t
sub_last = s + (n-2)*t
new_timetable = []
for tm in timetable:
    new_tm = int(tm[0]+tm[1])*60 + int(tm[3]+tm[4])
    new_timetable.append(new_tm)

if n*m > len(timetable):
    cnt = 0
    for ntm in new_timetable:
        if sub_last < ntm <= last:
            cnt += 1
        else:
            new_timetable.remove(ntm)
    print(new_timetable)
    print(cnt)
    if cnt >= m:
        new_timetable.sort()
        int_answer = new_timetable[m-1] - 1
    else:
        int_answer = last

    hour = str(int_answer // 60)
    if len(hour) == 1:
        hour = "0" + hour
    minute = str(int_answer % 60)
    if len(minute) == 1:
        minute = "0" + minute
    answer = hour + ":" + minute
else:
    seat = [m for _ in range(n)]
    new_timetable.sort()

print(answer)