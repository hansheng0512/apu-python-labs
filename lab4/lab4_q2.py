def totalOf3Numbers(n1, n2, n3):
    return n1 + n2 + n3


def average(n1, n2, n3):
    return totalOf3Numbers(n1 , n2, n3) / 3


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

avg = average(number1, number2, number3)

print("The average of the three numbers is: ", avg)
