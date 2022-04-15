arr = [1, 2, 3]

N = 3#len arr

#사용한 결과물을 담는 데이터
sel = [0] * N#결과들이 저장될 리스트
check = [0] * N#해당 원소를 이미 사용했는지 안 했는지에 대한 체크

def comb(idx):
    if idx == N:
        print(sel)
        return
    for i in range(idx, N):
        if not check[i]:
            check[i] = True
            sel[i] = arr[i]
            comb(i+1)
comb(0)
