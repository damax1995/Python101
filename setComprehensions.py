#Set is like a dictionary, but in a mathematical way.
#There can not be any repeated elements.
myList = [1,2,2,3,4,4,5,6,7,7,8]
print(myList)
mySet = set(myList)
print(mySet)

#Using set comprehensions:
print()
myList = [1,2,2,3,4,4,5,6,7,7,8]
print(myList)
mySet = {x for x in myList}
print(mySet)
