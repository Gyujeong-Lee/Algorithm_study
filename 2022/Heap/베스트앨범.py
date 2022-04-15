
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

'''
i는 고유 번호임
많이 재생된 장르
많이 재생된 곡
재생횟수가 같다면 고유번호가 작은 순
'''

#장르별 분류
# ex) classic : [(i, cnt), (), ...]
genre_dict = {}

for i in range(len(genres)):
    genre = genres[i]
    cnt = plays[i]
    if not genre_dict.get(genre):
        genre_dict[genre] = 0

    genre_dict[genre] += cnt

print(genre_dict)

