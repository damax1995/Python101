#In this part we are going to catch File errors with 'with' operator

#This one will be with try/catch
try:
    fileHandler = open("test.txt")
    for line in fileHandler:
        print(line)
except IOError:
    print("An IOError has ocurred.")
finally:
    fileHandler.close()

#And this other one will be with 'with' operator
print("------")
try:
    with open("test.txt") as fileHandler:
        for line in fileHandler:
            print(line)
except IOError:
    print("An IOError has ocurred.")
