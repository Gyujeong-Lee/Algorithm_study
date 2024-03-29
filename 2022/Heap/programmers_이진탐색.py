def solution(distance, rocks, n):
    answer = 0
    '''
    1) 기본 아이디어 : 최솟값 중 최댓값을 추출하기 위해 작은 값들을 지워나가야함
    2) 구현 로직 : 이분 탐색 
    상세)
    0 ~ distance 범위 내에서
    범위의 중간값(m)을 기준으로 (임의)
    이분 탐색 진행
    -> 중간값보다 작은 바위 지운다.

    3) m 검증 
     - 마지막 바위와 종점 거리
     - 파괴한 바위 개수
    '''
    rocks.sort()
    s, e, m = 0, distance, 0
    while s <= e:  # n 이 깨진 바위의 개수, 이분탐색은 거리로 한다.
        m = (s + e) // 2
        # print(m)
        rock_cnt, start, flag, backup = 0, 0, True, 0
        for rock in rocks:  ## 마지막 도착점과의 거리를 생각하지 않았다
            d = rock - start
            if d < m:  # 바위 파괴
                rock_cnt += 1
            else:
                # backup 에 그 전 start 위치 저장해놓기
                start, backup = rock, start
                # 마지막 돌이 파괴 안되고, 목 적지와의 거리가 m 보다 작을 때 -> 마지막돌 파괴해야함
        if rocks[-1] == start:
            if distance - start < m:
                rock_cnt += 1
                start = backup  # 스타트의 위치를 백업한 스타트의위치로 갱신해놓기

        # 종점과의 거리가 기준치 m 보다 작을때 --> m 이 더 작아도 똑같이 파괴할수 있다는 뜻
        if distance - start < m:
            flag = False  # 이 m은 올바른 답이 아니라는 것을 표시

        # rock_cnt : 거리의 최솟값의 최댓값이 m 이기 위해서 파괴되어야 하는 바위의 개수
        ## 거리의 최솟값의 최댓값이 유효하려면 바위 사이의 거리들중 일치하는 거리가 있어야 한다. --> 처리 안함

        if n < rock_cnt:  # 파괴한 바위가 많으면  -> m 줄어야
            e = m - 1
        else:  # 파괴한 바위가 적거나 같을 때
            if flag == False:
                e = m - 1
            else:
                s = m + 1
                answer = m

    return answer