from collections import deque
T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = list(map(int, input().split()))
    q = deque(arr)
    flag = True
    for s in p:
        if s == 'R':
            q.reverse()
        else:
            if len(q) >= 1:
                q.popleft()
            else:
                print('error')
                flag = False
                break
    if not flag:
        break
    print(list(q))

