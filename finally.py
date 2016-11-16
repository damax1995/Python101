myDict = {"a":1, "b":2, "c":3}
try:
    value = myDict["d"]
except KeyError:
    print("A KeyError ocurred!")
finally:
    print("The finally statement was executed.")
