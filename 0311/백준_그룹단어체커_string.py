'''
3
happy
new
year
'''
#단어의 개수
n = int(input())
words = []
for i in range(n):
    words.append(input())

cnt = 0
for i in range(n):
    s = []
    tmp = True
    for j in range(len(words[i])):
        if words[i][j] not in s:
            s.append(words[i][j])
        else:
            if s.pop() != words[i][j]:
                tmp = False
                break
            else:
                s.append(words[i][j])

    if tmp == True:
        cnt += 1
print(cnt)
