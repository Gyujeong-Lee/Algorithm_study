nums = input().split()
num1 = ''
num2 = ''
for i in range(len(nums[0])-1, -1, -1):
    num1 += nums[0][i]
    num2 += nums[1][i]
if int(num1) > int(num2):
    print(int(num1))
else:
    print(int(num2))