# a-z 0~25 txt
# str1 pattern
#처음 등장 위치 없으면 -1

word = input()
arr = [-1] * 26

for i in range(len(word)):
    if arr[ord(word[i]) - ord('a')] != -1:
        pass
    else:
        arr[ord(word[i]) - ord('a')] = i

for i in range(len(arr)):
    print(arr[i], end=' ')
