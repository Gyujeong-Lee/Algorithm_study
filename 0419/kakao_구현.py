'''
요금정책 : 기본료, 추가요금
기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
180	5000	10	600
10분 이하 - 올림
'''
'''
주차시간 구하기
출차 - 입차
입차만 존재한다면
24 - 입차
(주차시간 - 기본시간) / 10
'''
fees = [180, 5000, 10, 600]
base_time = fees[0]
base_fee = fees[1]
extra_time = fees[2]
extra_fee = fees[3]

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#답 result = [14600, 34400, 5000]
answer = []
N = len(records)
#현재 주차 되어 있는지 확인
#OUT일 때
check = []
#차량별 주차시간
times = {}
#23:59
t = 1439

#차량 별 주차시간
for rec in records:
    tmp = rec.split(' ')
    time = tmp[0]
    car_num = tmp[1]
    if not times.get(car_num):
        times[car_num] = 0

    if tmp[2] == 'IN':
        check.append(car_num)
        #주차시간 기본값
        tmp_time = t - (int(time[0] + time[1]) * 60 + int(time[3] + time[4]))
        times[car_num] += tmp_time
    else:
        check.remove(car_num)
        #주차시간 업데이트
        tmp_time = t - (int(time[0] + time[1]) * 60 + int(time[3] + time[4]))
        times[car_num] -= tmp_time

#주차요금 계산
for key, value in times.items():
    if value > base_time:
        rest = value - base_time
        if rest % extra_time:
            #나머지 존재
            final_fee = base_fee + (extra_fee * ((rest // extra_time) + 1))
            times[key] = final_fee
        else:
            final_fee = base_fee + (extra_fee * (rest // extra_time))
            times[key] = final_fee
    else:
        times[key] = base_fee
for key, value in sorted(times.items()):
    answer.append(value)

