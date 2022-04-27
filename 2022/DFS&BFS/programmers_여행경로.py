import copy
input_ticket = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
result = []

def dfs(dict, s, arr, use, ticket_list):
    global result
    cur_country = s
    if dict.get(s):
        adj_country = dict[cur_country]
    else:
        adj_country = []

    if not 0 in use:
        result.append(copy.deepcopy(arr))
        # print(result)
        return

    for i in range(len(adj_country)):
        next_country = adj_country[i]
        ticket = [cur_country, next_country]
        try:
            idx = ticket_list.index(ticket)
        except:
            continue
        if ticket in ticket_list and use[idx] == 0:
            use[idx] = 1
            arr.append(next_country)
            dfs(dict, next_country, arr, use, ticket_list)
            arr.pop()
            use[idx] = 0
        else:
            continue

def solution(tickets):
    global result

    num_tickets = len(tickets)
    used = [0 for _ in range(num_tickets)]
    #hash table
    route_dict = {}
    for i in range(len(tickets)):
        depart, arrive = tickets[i][0], tickets[i][1]
        if not route_dict.get(depart):
            route_dict[depart] = [arrive]
        else:
            route_dict[depart].append(arrive)

    #DFS 탐색
    dfs(route_dict, 'ICN', ['ICN',], used, tickets)
    result.sort()
    answer = result[0]
    return answer

print(solution(input_ticket))
