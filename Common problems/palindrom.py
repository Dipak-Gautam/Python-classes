number = input("enter a number")

reversed_num = str(number)[::-1]

if (number == reversed_num):
    print("entered number is palindrome")
else:
    print("entered number is not palindrome")
