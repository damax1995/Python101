myString = "abc"
print(id(myString))
print(myString)
myString = "def"
print(id(myString))
print(myString)
myString = myString + "ghi"
print(id(myString))
print(myString)

myString = "This is a string!"
print(myString)

myString = myString.upper()
print(myString)

myString = myString.lower()
print(myString)

print(dir(myString))

myString = "I like python!"
print(myString)
print(myString[:1])
print(myString[0:12])
print(myString[0:13])
print(myString[0:14])
print(myString[0:-5])
print(myString[:])
print(myString[2:])

print(myString[0])

print("Hola xdd "+myString)
