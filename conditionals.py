if 2 > 1:
    print("This is a True statement\n")

var1 = 1
var2 = 3

if var1 > var2:
    print("That is also True\n");
else:
    print("That was False!\n")
    
value = input("How old are you?: ")
value = int(value)
if value < 10:
    print("You are under 10\n")
elif 10 <= value <= 30:
    print("You are between 10 and 30\n")
else:
    print("Damn, over 30\n")

x = 10
y = 20
if x < 10 or y > 15:
    print("This statement was True!\n")


x = 10
y = 10
if x == 10 and y==15:
    print("The statement was True!\n")
else:
    print("The statement was False!\n")

x = 10
if x != 11:
    print("'x' is not equals to 11!\n")

myList = [1, 2, 3, 4]
x = 10
if x not in myList:
    print("'x' is not in myList\n")
