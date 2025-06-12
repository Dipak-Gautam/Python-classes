# # 2, 4, 6, 8, 9, 10... upto 20th item

# number = 2
# for i in range(1, 21):
#     print(number)
#     number = number+2


# 2,6,18,54,...10th item
# number = 2
# for i in range(1, 10):
#     print(number)
#     number = number*3


# 1,1,2,3,5,8,13....20th item

num1 = 1
num2 = 1
print(num1)
for i in range(1, 20):
    print(num2)
    temp = num2
    num2 = num1+num2
    num1 = temp
