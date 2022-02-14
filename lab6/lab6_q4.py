def searchFlightSchedule():
    fhand = open("flight_schedule.txt", "r")
    searchInput = input("Type what you watn to search: ")

    for line in fhand:
        line = line.rstrip()
        if not searchInput.lower() in line.lower():
            continue
        print(line)
    fhand.close()

searchFlightSchedule()