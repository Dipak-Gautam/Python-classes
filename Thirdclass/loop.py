# write a program to print number from 50 to 100


# for i in range(50, 100):
#     print(i,)


# write a program to enter a marks in 3 subject and find pass or fail

english = int(input("Enter a marks in english: "))
maths = int(input("Enter a marks in maths : "))
nepali = int(input("Enter a marks in Nepali : "))

if (english >= 40 and maths >= 40 and nepali >= 40):
    print("you have been passed")
else:
    print("you have been failed")
