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

#How to read Files piece by piece
print()
handle = open("test.txt", "r")
for line in handle:
    print(line)
handle.close()

#handle a file with chunks
print()
handle = open("test.txt", "r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break

#Read a Binary File (i.e. PDF)
print()
try:
    handle = open("test.pdf", "rb") #rb means ReadBinary
except IOError:
    print("The PDF doesn't exist!")

#Now lets write on the File
print("\nWe are going to write in output.txt file.")
handle = open("output.txt", "w")
handle.write("This is a test!\n")
handle.write("Second line")
handle.close()

#Lets use 'With' operator to read a File, it will automatically close the file for us.
print()
with open("test.txt") as fileHandler:
    for line in fileHandler:
        print(line)
        





    
