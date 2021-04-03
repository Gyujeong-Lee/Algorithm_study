import pandas as pd

#임희중이 DC 결정해야 할 품목들
arr_Lim = pd.read.excel('')

#선배들이 지금까지 DC한 품목
#중복 제거해야 함.

arr_senior = [1, 1, 2, 3, 4, 5, 6, 7, 10, 2, 2, 3, 4, 5, 6]

set_senior = set(arr_senior)

result = []

for product in arr_Lim:
    if product in set_senior:
        result.append(product)

print(result)