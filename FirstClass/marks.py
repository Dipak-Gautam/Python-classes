marks = input("enter a obtained marks :")

marks = int(marks)

if marks > 80:
    print("you have been passed in distension")
elif marks > 60:
    print("you have been passed in first division")
elif marks > 50:
    print("you have been passed in second division")
elif marks >= 40:
    print("you have been passed in third division")
else:
    print("you have been failed")
