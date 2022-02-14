def save_flight_schedule():
    schedules = []
    for i in range(5):
        sch = []
        flightNumber = input("Enter flight number: ")
        sch.append(flightNumber)
        depTime = input("Enter departure time: ")
        sch.append(depTime)
        arrTime = input("Enter arrival time: ")
        sch.append(arrTime)
        dest = input("Enter destination: ")
        sch.append(dest)
        depForm = input("Enter departure airport: ")
        sch.append(depForm)
        schedules.append(sch)

    fileHandler  = open("flight_schedule.txt", "w")

    for sch in schedules:
        for fs in sch:
            fileHandler.write(fs)
            fileHandler.write("\t")
        fileHandler.write("\n")
    fileHandler.close()


def sprint_flight_schedule():
    fileHandler = open("flight_schedule.txt", "r")
    for line in fileHandler:
        print(line)
    fileHandler.close()


def searchFlightSchedule():
    fhand = open("flight_schedule.txt", "r")
    searchInput = input("Type what you watn to search: ")

    for line in fhand:
        line = line.rstrip()
        if not searchInput.lower() in line.lower():
            continue
        print(line)
    fhand.close()


def menu():
    print("Select the operation that you want to perform: ")
    print("1. Save Flight Schedules")
    print("2. Print Flight Schedules")
    print("3. Search Flight Schedules")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if (choice == 1):
        save_flight_schedule()
    elif (choice == 2):
        sprint_flight_schedule()
    elif (choice == 3):
        searchFlightSchedule()
    elif (choice == 4):
        print("Have a nice day!")
    else:
        print("Invalid choice!")


menu()