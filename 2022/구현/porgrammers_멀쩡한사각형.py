'''
카카오 섬머/윈터 코딩
결론 : 틀렸다 하지만 이해가 되지 않는다. 그러므로 패스한다. 더러운 문제

내 풀이 : 기울기
다른 풀이 : 최대 공약수 (시간 복잡도 고려해야함)

기울기로 풀었을 때 틀리나 반례와 원인을 찾을 수 없음

'''


def solution(w, h):
    total = w * h
    '''
    1) 정사각형인 경우 (기울기 = 1)
    -> 1 row당 1개씩만 못씀 why? 사각형을 관통하도록 절취선이 생기기 때문에
    2) 직사각형인 경우
    -> 기울기 범위 별로 못쓰는 정사각형 개수가 달라짐
    ex) 1 ~ 2 사이 2개 
        2 ~ 3 사이 3개 ...
    '''
    impossible = 0
    if w == h:
        impossible = w
    elif w > h:
        if w % h == 0:
            # 기울기
            tmp = w // h
        else:
            tmp = (w // h) + 1

        impossible = tmp * h

    elif h > w:
        if h % w == 0:
            tmp = h // w
        else:
            tmp = (h // w) + 1

        impossible = tmp * w

    answer = total - impossible

    return answer