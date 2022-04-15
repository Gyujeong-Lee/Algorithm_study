#재귀 - 팩토리얼
def factorial(n):
    
    if n == 1:
        return 1


    return n * factorial(n-1)

num = int(input())

if num > 0:
    ans = factorial(num)

elif num == 0:
    ans = 1

print(ans)