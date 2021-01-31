day6

a, b = map(int, input().split())

if a + b != 0:
    print(a + b)
while a + b != 0:
    a, b = map(int, input().split())
    if a + b == 0:
        break
    print(a+b)

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break



