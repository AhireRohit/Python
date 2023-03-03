# Variable – Container to store a value

# Keywords – Reserved words in Python

# Identifiers – class/function/variable name

# Data Types:

# Primarily there are the following data types in Python:
#     Integers
#     Floating point numbers
#     Strings
#     Booleans
#     None

# Python is a fantastic language that automatically identifies the type of data for us.

# Rules for defining a variable name: (Also applicable to other identifiers)
#     A variable name can contain alphabets, digits, and underscore.
#     A variable name can only start with an alphabet and underscore.
#     A variable can’t start with a digit.
#     No white space is allowed to be used inside a variable name.

# Examples of few valid variable names,
# Harry, harry, one8, _akki, aakash, harry_bro, etc.

# Operators in Python

# The following are some common operators in Python:

#     Arithmetic Operators (+, -, *, /, etc.)
#     Assignment Operators (=, +=, -=, etc.)
#     Comparison Operators (==, >=, <=, >, <, !=, etc.)
#     Logical Operators (and, or, not)

a = 23;
b = "Rohit"
print(type(a))              # type() -- it is used to find the data type of variable
print(type(b)) 


# Below steps are used to convert a variable from one data type to another

c = int("21")
print(type(c))

d = str(32)
print(type(d))

# input() function
# This function allows the user to take input from the keyboard as a string.

a = input("Enter name: ") 

# When we take input from user the output is always in string format. So use below steps to conert to integer

z = input("Enter value: ")
z = int(z)
print(type(z))
