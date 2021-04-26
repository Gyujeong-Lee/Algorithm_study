'''
3 3
1 2 1
2 3 -1
1 3 -1
'''
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union_set(x, y):
    p[find_set(y)] = find_set(x)
    return

def Kruskal():
    total = 0
    for e in edge:
        if find_set(e[0]) != find_set(e[1]):
            Union_set(e[0], e[1])
            total += e[2]
    return total

V, E = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(E)]
edge = sorted(edge, key=lambda x:x[2], reverse=False)
p = [i for i in range(V+1)]
ans = Kruskal()
print(ans)