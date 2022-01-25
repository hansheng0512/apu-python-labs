subMarks = []

while True:
    mark = int(input("Enter Marks: "))
    subMarks.append(mark)
    cont = input("Press <enter> to continue or 'x' to exit: ")
    if cont == 'x' or cont == 'X':
        break

total = 0
for mark in subMarks:
    total = total + mark

avgMarks = total/len(subMarks)

print("Average Marks: %.2f" % avgMarks)