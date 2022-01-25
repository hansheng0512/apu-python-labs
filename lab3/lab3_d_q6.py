values = []

name = input("Enter name: ")
tpNumber = input("Enter TP number: ")
values = [name, tpNumber]

subMarks = []
while True:
    mark = int(input("Enter Marks: "))
    subMarks.append(mark)
    cont = input("Press <enter> to continue or 'x' to exit: ")
    if cont == 'x' or cont == 'X':
        break

total = 0
for mark in subMarks:
    total += mark
values.append(total)

avgMarks = total/len(subMarks)
values.append(avgMarks)

print(values)

if avgMarks >= 80:
    grade = "A+"
elif avgMarks >= 75:
    grade = "A"
elif avgMarks >= 70:
    grade = "B+"
elif avgMarks >= 65:
    grade = "B"
elif avgMarks >= 60:
    grade = "C+"
elif avgMarks >= 55:
    grade = "C"
elif avgMarks >= 50:
    grade = "C-"
else:
    grade = "D"

values.append(grade)

print("Name:", values[0])
print("TP Number:", values[1])
print("Total Marks:", values[2])
print("Average Marks: %.2f" % values[3])
print("Grade:", values[4])