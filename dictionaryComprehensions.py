x = {i: str(i) for i in range(5)}
print(x)

#When we want to swap keys and values
myDict = {1:"dog", 2:"cat", 3:"hamster"}
x = {value:key for key, value in myDict}
print(x)

