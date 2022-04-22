'''
정점 한 개 이상 연결이 되어 있는 그룹
5
1, 1, 0, 0, 0
1, 1, 0, 0, 0
0, 0, 1, 1, 0
0, 0, 1, 1, 0
0, 0, 0, 0, 1
'''

input_n = int(input())
input_computers = []
for _ in range(input_n):
    input_computers.append(list(map(int, input().split(','))))


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    result = []
    queue = []
    for i in range(n):
        tmp = []
        queue.append(i)
        visited[i] = 1
        while queue:
            s = queue.pop(0)
            tmp.append(s)
            for j in range(n):
                if computers[s][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    queue.append(j)
        flag = False
        if len(tmp) == 1:
            for k in range(len(result)):
                if tmp[0] in result[k]:
                    flag = True
            if not flag:
                result.append(tmp)
        else:
            result.append(tmp)
    answer = len(result)
    return answer

print(solution(input_n, input_computers))