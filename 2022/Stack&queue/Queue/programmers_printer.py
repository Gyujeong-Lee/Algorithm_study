'''
문제설명
자료구조 Queue 문제
우선순위 큐 (Heapq) 문제인듯,
queue를 통해 푼 이후 heapq로 다시 풀기

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
'''

input_priorities = list(map(int, input().split(',')))
input_location = int(input())



def solution(priorities, location):

    answer = 0
    front = 0
    rear = len(priorities) - 1

    while True:
        if priorities[front] >= max(priorities):
            answer += 1
            #이미 뽑힌 것은 최하위로
            priorities[front] = 0
            if front == location:
                break
        front += 1
        if front > rear:
            front = abs(front-len(priorities))

    return answer


print(solution(input_priorities, input_location))
