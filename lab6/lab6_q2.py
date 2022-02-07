fileHandler = open("flight_schedule.txt", "r")

for line in fileHandler:
    line = line.rstrip()
    print(line)

fileHandler.close()