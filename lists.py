myList = [1, 2, 3]
myList2 = ["a", "b", "c"]
myList3 = ["a", 1, "Python", 5]

nestedtList = [myList, myList2]
print(nestedtList)

comboList = []
myList4 = [4, 5]
comboList.extend(myList4)
print(comboList)

comboList = myList + myList2
print(comboList)

numberList = [34, 65, 12, 25, 81, 93, 55, 43, 23]
print(numberList)
numberList.sort()
print(numberList)

print(numberList[0:5])
