#Two ways to open the file.
handle = open("test.txt")
print(handle)

handle = open(r"D:/ProjectosPython/pyhton101/test.txt")
print(handle)

#Difference between raw type and "not raw" type.
print()
print("D:\ProjectosPython\pyhton101\test.txt")
print(r"D:\ProjectosPython\pyhton101\test.txt")

print()
handle = open("test.txt", "r")
data = handle.read()
print(data)
handle.close()

print()
handle = open("test.txt", "r")
data = handle.readline() #read just one line
print(data)
handle.close()

print()
handle = open("test.txt", "r")
data = handle.readlines() #read all the lines
print(data)
handle.close()
