'''
입력 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
Mississipi
출력 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
?
'''

word = input().upper()
spells = set(word)
count_dict = {}

for spell in spells:
    count_dict[spell] = word.count(spell)
# print(count_dict)
ans = ''
max_cnt = 0
for key,value in count_dict.items():
    if value > max_cnt:
        ans = key
        max_cnt = value
    elif value == max_cnt:
        ans = '?'

print(ans)