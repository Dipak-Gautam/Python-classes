num1 = int(input("Please enter a number"))

result = 1

for i in range(num1, 1, -1):
    result = result*i

print("factorial of number is", result)
