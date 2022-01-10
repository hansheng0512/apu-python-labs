# First Technique
total = 0
counter = 1

while counter <= 5:
    num = int(input("Enter a number: "))
    total += num
    counter += 1

average = total/5
print("The average of 5 numbers is %.2f" % average)


# Second Technique
total = 0

for i in range(1, 6):
    num = int(input("Enter a number: "))
    total += num

average = total/5
print("The average of 5 numbers is {0:.2f}".format(average))
