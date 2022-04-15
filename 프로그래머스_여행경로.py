# 시작 12:00, 종료 14:10
# DFS를 살짝 응용해서 푸는 문제
# 풀이 순서
# ICN을 먼저 스택에 넣기
# 1. 스택 top을 보고 거기서부터 갈 수 있는 공항들을 tickets에서 검색.
# ** 스택에서 꺼내지 않음. 즉 pop이 아니고 top
# 2. 여러 개 있을 경우 알파벳 순서가 높은 것을 하나 넣기(ex: ATL, SOF 라면 ATL을 선택)
# 3. 스택에 넣은 경로(ex: ICN-ATL)는 tickets에서 제거
# 4. tickets의 경로가 모두 제거될 때까지 1 ~ 3번을 반복
# tickets에서 모든 경로가 다 제거된 후 스택을 출력하면 끝
def dfs(start, top):

    if len(tickets) == 0:
        return

    tmp = []
    for idx, ticket in enumerate(tickets):
        if ticket[0] == start:
            if len(tmp) == 0:
                tmp.append((ticket[1], idx))
            else:
                t1 = tmp[0][0]
                t2 = ticket[1]
                if t1 < t2:
                    tmp.pop()
                    tmp.append((ticket[1], idx))
    if len(tmp) > 0:
        top += 1
        tickets.pop(tmp[0][1])
        stack.append(tmp[0][0])
        dfs(stack[top], top)

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
n = len(tickets)
stack = ["ICN"]

dfs("ICN", 0)
print(stack)