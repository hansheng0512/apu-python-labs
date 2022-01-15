total = 0
numOfStudents = 0

name = input("Enter name: ")
score = int(input("Enter score [999 to end]: "))
while score != 999 and name != "":
    if score > 0 and score <= 100:
        total += score
        numOfStudents += 1
    else:
        print("Invalid score")
    name = input("Enter name: ")
    score = int(input("Enter score [999 to end]: "))

if(numOfStudents > 0):
    print("Average score:", total / numOfStudents)
else:
    print("No students")
