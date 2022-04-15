'''
1) 음악시간과 재생시간을 고려하여 총 멜로디 산출
음악시간 > 재생시간
재생시간에서 짜른 멜로디[:]
음악시간 < 재생시간
남은 시간 만큼 문자열을 붙임
2) 나단이가 기억하는 멜로디 배열과 일치 여부 판별
3) 일치하는 경우 존재 시 조건에 맞춰 출력
- 제목 길이가 긴 순서
- 먼저 재생된 노래 순서
'''

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
answer = ''
trans = {
    'A#': 'H',
    'C#': 'I',
    'D#': 'J',
    'F#': 'K',
}
for key, value in trans.items():
    if key in m:
        m = m.replace(key, value)

for music in musicinfos:
    info = music.split(',')
    #멜로디 치환
    melody = info[3]
    for key, value in trans.items():
        if key in melody:
            melody = melody.replace(key, value)

    #재생시간, 음악시간 계산
    play_time = 0
    start_time = info[0]
    end_time = info[1]
    tmp1 = int(start_time[0] + start_time[1])*60 + int(start_time[3] + start_time[4])
    tmp2 = int(end_time[0] + end_time[1])*60 + int(end_time[3] + end_time[4])
    play_time = tmp2 - tmp1
    music_time = len(melody)

    #실제 멜로디 계산
    if play_time > music_time:
        n = play_time // music_time
        rest = play_time % music_time
        melody = melody*n + melody[:rest]

    else:
        melody = melody[:play_time]

    if m in melody and len(info[2]) > len(answer):
        answer = info[2]

if len(answer) == 0:
    answer = 'None'
