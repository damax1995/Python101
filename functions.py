def aFunction():
    print("You just created a function!")

def emptyFunction():
    pass

#Passing arguments to a function
def add(a,b):
    return a+b

#*args and **kwargs for infinite arguments and keyword arguments
def many(*args, **kwargs):
    print(args)
    print(kwargs)

def functionA():
    a = 1
    b = 2
    return a+b

def functionB():
    c = 3
    return a+c

print(functionA())
print(functionB())
#to make this code work, we have to make 'a' global in functionA()
