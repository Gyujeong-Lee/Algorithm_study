'''
구현문제
단순하게 접근했다가 수 많은 시행착오 끝에 해결함
시간이 너무 많이 소요됨
문제 풀기 전, 풀이 전체에 대해 생각한 후 시작할 것.
잔 실수도 너무 많음

'''


def solution(n, t, m, timetable):
    answer = ''
    '''
    버스가 오는 시각
    해당 시간 별로 남아있는 자리
    -> 없다면 사람들 중 가장 늦게온 사람보다 1분 빨리 오면 됨
    '''
    start = 9 * 60
    bus_timetable = [start]

    for i in range(n - 1):
        bus_timetable.append(start + (i + 1) * t)

    new_timetable = []
    # 숫자화시키기, 비교를 위해
    for t in timetable:
        tmp = t.split(':')
        new_timetable.append(int(tmp[0]) * 60 + int(tmp[1]))
    new_timetable.sort()
    print(bus_timetable)
    print(new_timetable)

    waiting = [[] for _ in range(len(bus_timetable))]

    j = 0
    for i in range(len(bus_timetable)):
        cur_bus = bus_timetable[i]
        if i == 0:
            for time in new_timetable:
                if time <= cur_bus:
                    waiting[i].append(time)
                    j += 1
        else:
            # 이전 대기열을 현재 대기열로
            tmp_wait = waiting[i - 1]
            if len(tmp_wait) > m:
                f = 0
                for idx, tmp in enumerate(tmp_wait):
                    if idx > m- 1:
                        if f == 0:
                            f = idx
                        waiting[i].append(tmp_wait[idx])
                waiting[i - 1] = tmp_wait[:f]

            for idx, time in enumerate(new_timetable):
                if j == idx and time <= cur_bus:
                    waiting[i].append(time)
                    j += 1
    print(waiting)
    for i in range(len(waiting) - 1, -1, -1):
        if len(waiting[i]) == m:
            first = waiting[i][0]
            last = waiting[i][-1]
            if first == last:
                cur = first - 1
            else:
                cur = last - 1
            h = str(cur // 60)
            mi = str(cur % 60)
            if len(h) == 1:
                h = '0' + h
            if len(mi) == 1:
                mi = '0' + mi
            answer = h + ':' + mi
            return answer

        elif len(waiting[i]) > m:
            cur = waiting[i][m - 1] - 1
            h = str(cur // 60)
            mi = str(cur % 60)
            if len(h) == 1:
                h = '0' + h
            if len(mi) == 1:
                mi = '0' + mi
            answer = h + ':' + mi
            return answer

        else:
            # 자리가 남아있을 때는 그냥 그 시간
            cur = bus_timetable[i]
            h = str(cur // 60)
            mi = str(cur % 60)
            if len(h) == 1:
                h = '0' + h
            if len(mi) == 1:
                mi = '0' + mi
            answer = h + ':' + mi
            return answer
