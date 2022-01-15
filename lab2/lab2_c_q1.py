for i in range(1, 16):
    fahrenheit = float(input("Enter the temperature {} in Fahrenheit: ".format(i)))
    celcius = (fahrenheit - 32) * 5 / 9
    print("%.2f" % fahrenheit, "Fahrenheit is", "%.2f" % celcius, "Celcius")
    print()

print("All temperatures have been processed")