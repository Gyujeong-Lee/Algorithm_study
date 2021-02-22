n = int(input())
stack1 = []
stack2 = []
stack3 = []
for i in range(n, 0, -1):
    stack1.append(i)
#stack 3으로 다 옮겨야 함
#후입선출
#but 각 숫자는 너비를 의미하며
#작은 것은 무조건 큰 것 위에 있어야 함.

