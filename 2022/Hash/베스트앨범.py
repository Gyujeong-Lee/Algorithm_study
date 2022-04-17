
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = []
'''
i는 고유 번호임
많이 재생된 장르
많이 재생된 곡
재생횟수가 같다면 고유번호가 작은 순
'''

#장르별 분류
# ex) classic : [(i, cnt), (), ...]
genre_total_dict = {}
genre_dict = {}

for i in range(len(genres)):
    genre = genres[i]
    cnt = plays[i]
    if not genre_total_dict.get(genre):
        genre_total_dict[genre] = 0

    if not genre_dict.get(genre):
        genre_dict[genre] = []

    genre_total_dict[genre] += cnt
    genre_dict[genre].append((i, cnt))

print(genre_dict)
print(genre_total_dict)
sorted_total = sorted(genre_total_dict.items(), key=lambda x: x[1], reverse=True)

for tmp in sorted_total:
    tmp_genre = tmp[0]
    tmp_list = genre_dict[tmp_genre]

    if len(tmp_list) > 1:
        sorted_genre = sorted(tmp_list, key=lambda x: x[1], reverse=True)
        answer.append(sorted_genre[0][0])
        answer.append(sorted_genre[1][0])
    else:
        answer.append(tmp_list[0][0])
print(answer)