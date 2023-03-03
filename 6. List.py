# Python Lists are containers to store a set of values of any data type.

a = [12, 'Raj', 'Water', 40, 3.14, False, True ]   # This is list
print(a)
print(a[2])                    # Access list content using indexing

a[1] = "AAA"                   # We can change the value in list    
print(a[1])

a[2] = 15
print(a[2])

# List Slicing
print(a[0::2])