# String is a data type in python
# string is sequence of characters enclosed in quotes

# We can primarily write a string in three ways:

    # Single quoted strings : 
a = 'harry'
    # Double quoted strings : 
b = "harry's"
    # Triple quoted strings : 
c = '''harry"s  and harry"s '''


# concatenation

greet = "Good Morning, "
name = "Rohit"
print(greet + name)

# String indexing and slicing

slice = "Ahire"
print(slice[0:])  # This is same as 0:5
# print(slice[-1:-4])
# print(slice[-4:-1])

a = "METBhujbal"
print(a[0::2])  # start from 0 and skip one letter
print(a[2:10:3]) # start from 2 and skip two letters

