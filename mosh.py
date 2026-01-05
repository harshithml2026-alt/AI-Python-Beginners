import math

# Boolean variables
is_published = True  # True or False are case sensitive in python
print(is_published)

####################################################################################

# String operations and indexing
course = "Python Programming"

print(len(course))  # 18
print(course[0])  # P
print(course[-1])  # g
print(course[0:3])  # Pyt
print(course[0:])  # Python Programming
print(course[:3])  # Pyt

####################################################################################

# Escape sequences and string formatting
string_test = "Python \" Programming"  # Escape sequence is backslash \"\"

print(string_test)

first = "Harshith"
last = "Govind"

print(first + " " + last)  # Harshith Govind
print(f"{first} {last}")  # Harshith Govind
print(f"{len(first)} last")  # 8 last

####################################################################################

# String methods
source = "Youtube learning"

print(source.upper())  # YOUTUBE LEARNING
print(source.title())  # Youtube Learning
print(source.find("tube"))  # 3
print(source.find("XXX"))  # -1
print(source.replace("Y", "N"))  # Noutube learning
print("tube " in source)  # True

####################################################################################

# Numbers and arithmetic operations
x = 1
y = 1.1
z = 1 + 2j  # complex numbers

print(10 / 3)  # 3.3333333333335
print(10 // 3)  # 3
print(10 % 3)  # 1
print(10 ** 3)  # 1000

print(round(2.9))  # 3
print(abs(-2.9))  # 2.9
print(math.ceil(2.2))  # 3  # Google math module of python3 for more functions

####################################################################################

# Type conversion
x = 1.1
print(int(x))  # 1  # Converts to integer

y = 1
print(float(y))  # 1.0  # Converts to float

# Falsy values => "", 0, NaN
print(bool(0))  # False
print(bool("False"))  # True (any non-empty string is truthy)
print(bool(""))  # False (empty string is falsy)
####################################################################################
# Conditionals - strings, numbers and booleans are primitives in python
temperature = 30

if temperature >= 25:
    print("Cold")
elif temperature > 1000:
    print("YOLO")
else:
    print("hot")

####################################################################################

# Loops
for i in range(3):
    print("Hi")

# Output:
# Hi
# Hi
# Hi

####################################################################################


def greet():
    print("Hello World")
    print("This is a function")

greet()

####################################################################################

def greet_with_input(name):
    print(f"Hello {name}")
    print("This is a function with a parameter")

greet_with_input("Harshith")

####################################################################################


def greet_with_default(name="Guest"):
    print(f"Hello {name}")
    print("This is a function with a default parameter")    

greet_with_default()  # Uses default parameter
greet_with_default("Harshith")  # Overrides default parameter

####################################################################################

