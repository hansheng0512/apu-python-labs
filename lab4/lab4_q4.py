import math


def diameter(radius):
    return 2 * radius


def circumference(radius):
    return 2 * math.pi * radius


def area(radius):
    return math.pi * radius ** 2


def menu():
    print("Circle- Diameter, Circumference and Area calculator Program")
    print("\t1. Diameter")
    print("\t2. Circumference")
    print("\t3. Area")

    option = int(input("Choose the operation from the given options: "))
    radius = float(input("Enter radius: "))

    if (option == 1):
        print("Diameter : %.3f" % diameter(radius))
    elif (option == 2):
        print("Circumference : %.3f" % circumference(radius))
    elif (option == 3):
        print("Area : %.3f" % area(radius))
    else:
        print("Invalid input!")


menu()
