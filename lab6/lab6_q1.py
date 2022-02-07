def flight_schedule():
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
    return schedules

fileHandler  = open("flight_schedule.txt", "w")
schedules = flight_schedule()

for sch in schedules:
    for fs in sch:
        fileHandler.write(fs)
        fileHandler.write("\t")
    fileHandler.write("\n")
fileHandler.close()