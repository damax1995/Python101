myList = [1, 2, 3, 4, 5]

for i in myList:
    if i == 3:
        print("Item found!!")
        break
    print(i)
else:
    print("Item not found!")

print()
myList2 = [1, 2, 3, 4, 5]

for k in myList2:
    if k == 9:
        print("Item found!!")
        break
    print(k)
else:
    print("Item not found!")
