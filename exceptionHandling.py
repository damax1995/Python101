try:
    print(1/0)
except ZeroDivisionError:
        print("You can't divide by 0!")

print()
try:
    print(1/0)
except:
    print("You cannot divide by 0!")

print()
myDict = {"a":1, "b":2, "c":3}
try:
    value = myDict["d"]
except KeyError:
    print("That key doesn't exist!")

print()
myList = [1,2,3,4,5]
try:
    x = myList[6]
except IndexError:
    print("That index does not exist!")

print()
myDict = {"a":1, "b":2, "c":3}
try:
    value = myDict["d"]
except IndexError:
    print("This index does not exist.")
except KeyError:
    print("This key is not in the dictionary.")
except:
    print("Some other error ocurred!")

print()
try:
    value = myDict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError ocurred!.")
    
