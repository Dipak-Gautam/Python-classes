num1 = int(input("enter a number: "))
operator = input("enter a operator : ")
num2 = int(input("enter a second number: "))
result = 0

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1/num2
else:
    print("invalid operator")

print("result", result)
