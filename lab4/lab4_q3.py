def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    print("Calculator Program")
    print("\t1. Add")
    print("\t2. Subtract")
    print("\t3. Multiply")
    print("\t4. Divide")
    option = int(input("Choose an option: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if option == 1:
        print("Total of {} and {} is {}".format(num1, num2, add(num1, num2)))
    elif option == 2:
        print("Subtraction of {} and {} is {}".format(num1, num2, subtract(num1, num2)))
    elif option == 3:
        print("Multiplication of {} and {} is {}".format(num1, num2, multiply(num1, num2)))
    elif option == 4:
        print("Division of {} and {} is {}".format(num1, num2, divide(num1, num2)))
    else:
        print("Invalid option")


calculator()