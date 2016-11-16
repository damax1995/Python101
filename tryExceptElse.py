myDict = {"a":1, "b":2, "c":3}
try:
    value = myDict["a"]
except KeyError:
    print("A KeyError ocurred!")
else:
    print("No error ocurred!")

print()
try:
    value = myDict["a"]
except KeyError:
    print("A keyError ocurred!")
else:
    print("No error ocurred")
finally:
    print("Finally statement ran!")
    
