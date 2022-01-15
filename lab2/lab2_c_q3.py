while True:
    assign = int(input("Enter your assignment mark: "))
    if assign < 25:
        print("Redo assignment and get 25 marks")
        continue

    test = int(input("Enter your test mark: "))
    if test < 25:
        print("Redo test and get 25 marks")
        continue

    exam = int(input("Enter your exam mark: "))
    if test < 25:
        print("Redo exam and get 50 marks")
        continue

    print("You have passed the module")
    break