# The part containing the exact set of instructions that are executed during the function call.

# There are two types of functions in Python:

#     Built-in functions #Already present in Python
#     User-defined functions #Defined by the user

# Examples of built-in function includes len(), print(), range(), etc.

def funct1():
    print("Hello World")

funct1()
    
# Q. Write a program to greet the user "Good Day" using functions
name = input("Enter name : ")
def greet():
    print("Good Day "+ name)

greet()


# A function can accept some values it can work with. We can put these values in the parenthesis. A function can also return values as shown below:

def greet(name):
	gr = "Hello" + name
	return gr

# Default Parameter Value
# We can have a value as the default argument in a function.