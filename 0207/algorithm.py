#array

# N = int(input())
# score_li = list(map(int, input().split()))
# max_num = max(score_li)
# new_num = 0
# new_nums = []

# # sum( i/max_num * 100 ) 

# for num in score_li:
#     new_num = (num / max_num) * 100
#     new_nums.append(new_num)

# print(sum(new_nums)/len(new_nums))

# n = int(input())


# for i in range(n):
#     score = 0
#     total = 0
#     test_case = input()
#     for j in test_case:
#         if j == 'O':
#             score += 1
#             total += score   
#         else:
#             score = 0
#     print(total)

C = int(input())
ratio = 0
for i in range(C):
    N_scores = list(map(int, input().split()))
    N = N_scores.pop(0)
    avg_scores = sum(N_scores) / len(N_scores)
    num_students = 0

    for score in N_scores:
        if score > avg_scores:
            num_students += 1
    ratio = (num_students / N) * 100
    print('%.3f%%' % ratio)    