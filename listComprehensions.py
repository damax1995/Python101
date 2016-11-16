x = [i for i in range(5)]
print(x)

#When we are reading some file, we can use some filter.
#if[i for i in line if "SOME TERM" in i]:
    #do something

#We want to cast a couple of strings to integer
print()
x = ['1', '2', '3', '4', '5']
print(x)
print(type(x[0]))
y = [int(i) for i in x]
print (y)
print(type(y[0]))

#If we want to create a nested list comprehension. For example to mix lists into one
print()
vec = [[1,2,3], [4,5,6], [7,8,9]]
x = [num for elem in vec for num in elem]
print(x)
