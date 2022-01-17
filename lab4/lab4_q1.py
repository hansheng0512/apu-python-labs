def differenceOfTwoNumbers(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
tot = differenceOfTwoNumbers(number1, number2)

print("Difference of given two numbers is: ", tot)
