'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
def pre_order(idx): #0부터 N까지만 들어올거임
    global ans_pre
    if tree[idx][1]:
        ans_pre += tree[idx][1]
        pre_order(tree[idx][0])
        pre_order(tree[idx][2])

def in_order(idx): #0부터 N까지만 들어올거임
    global ans_in
    if tree[idx][1]:
        in_order(tree[idx][0])
        ans_in += tree[idx][1]
        in_order(tree[idx][2])

def post_order(idx): #0부터 N까지만 들어올거임
    global ans_post
    if tree[idx][1]:
        post_order(tree[idx][0])
        post_order(tree[idx][2])
        ans_post += tree[idx][1]

#노드의 개수
N = int(input())
data = []
for _ in range(N):
    data.append(input().split())

tree = [[0] * 3 for _ in range(N+1)]

for arr in data:
    tree[ord(arr[0])-64][1] = arr[0]
    if arr[1] != '.':
        tree[ord(arr[0])-64][0] = ord(arr[1])-64
    if arr[2] != '.':
        tree[ord(arr[0])-64][2] = ord(arr[2])-64

# A : 65 Z : 90
# if 65 <= ord(data[x]) <= 90

ans_pre = ''
ans_in = ''
ans_post = ''

pre_order(1)
in_order(1)
post_order(1)

print(ans_pre)
print(ans_in)
print(ans_post)
