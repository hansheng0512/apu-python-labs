fileHandler = open('first.txt', 'r')

content = fileHandler.read()

for char in content:
    print(char, end='')

fileHandler.close()