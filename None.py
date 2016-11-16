emptyList = []
emptyTuple = ()
emptyString = ""
nothing = None

if emptyList == []:
    print("It's an empty list!\n")

if emptyTuple:
    print("It's not an empty tuple!\n")

if not emptyString:
    print("This is an empty string!\n")

if not nothing:
    print("Then it's nothing!\n")

emptyString = "something"
if emptyString == "":
    print("This is an empty string!\n")
else:
    print("This string contains something\n")
    
print(emptyList == emptyList)
