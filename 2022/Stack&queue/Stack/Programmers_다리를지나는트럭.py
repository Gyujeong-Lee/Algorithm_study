'''
stack에
하나씩 삽입, 삭제를 진행하며
시간 카운트
하지만 길이, 중량을 통해 stack에 넣을 수 있는 지 확인해야 함
'''

tmp1 = 100
tmp2 = 100
tmp3 = [10,10,10,10,10,10,10,10,10,10]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = []
    time = 1
    first_truck = truck_weights.pop(0)
    stack.append([first_truck, 1])

    while stack:
        # print(time, stack)
        time += 1
        total = 0

        if stack[0][1] == bridge_length:
            stack.pop(0)

        for truck in stack:
            total += truck[0]
            truck[1] += 1

        if truck_weights:
            if total + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                stack.append([new_truck, 1])

    return time



print(solution(tmp1, tmp2, tmp3))