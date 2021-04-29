'''
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
나갔다 들어오면 다 바뀜
Ry
'''
#세 가지 키워드만 가능
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
record_dict = {}

#최종 이름만 담김
for r in record:
    tmp = r.split()
    if len(tmp) == 3:
        record_dict[tmp[1]] = tmp[2]

result = []
for r in record:
    tmp = r.split()
    if tmp[0] == 'Enter':
        result.append('{}님이 들어왔습니다.'.format(record_dict[tmp[1]]))
    elif tmp[0] == 'Leave':
        result.append('{}님이 나갔습니다.'.format(record_dict[tmp[1]]))
    else:
        pass
print(result)
'''
programmers 제출
def solution(record):
    record_dict = {}
    #최종 이름만 담김
    for r in record:
        tmp = r.split()
        if len(tmp) == 3:
            record_dict[tmp[1]] = tmp[2]

    answer = []
    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(record_dict[tmp[1]]))
        elif tmp[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(record_dict[tmp[1]]))
        else:
            pass
    
    return answer
'''