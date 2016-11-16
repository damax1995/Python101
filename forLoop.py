x = range(5)
print(x)
y = range(5,10)
print(y)
auxList = list(range(1, 10, 2))
print(auxList)

for number in range(5):
    print (number)

print()
for number in [0, 1, 2, 3, 4]:
    print (number)

print()
myDict = {"one":1, "two":2, "three":3}
for key in myDict:
    print(key)

print()
myDict = {1:"one", 2:"two", 3:"three"}
keys = myDict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

print()
for number in range(10):
    if number % 2 == 0:
        print(number)
