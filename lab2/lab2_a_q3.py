marks = int(input("Enter marks [enter 999 to end]: "))
while marks != 999:
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 80:
        print("Your grade is A")
    elif marks >= 70:
        print("Your grade is B")
    elif marks >= 60:
        print("Your grade is C")
    elif marks >= 50:
        print("Your grade is D")
    else:
        print("Your grade is F")

    marks = int(input("Enter marks [enter 999 to end]: "))
