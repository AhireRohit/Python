# Set is a collection of non repetitive elements
# If set has 2 same values it will print only once

# Properties of Sets

#     Sets are unordered # Elements order doesn’t matter
#     Sets are unindexed # Cannot access elements by index
#     There is no way to change items in sets
#     Sets cannot contain duplicate values


a = {74, 5, 12, 2.03, 5}
print(type(a))
print(a)

b = {}
print(type(b))              # When no elements in curly braces then type is dictionary

c = set()
print(type(c))              # This is syntax for empty set

# Adding values to set

c.add(33)
c.add(100)

# c.add([58, 85])           # We cannot add list to sets
# c.add({3:5})                # We cannot add dictionary to sets

c.add((45, 85))             # We can add tuple to sets
print(c)

# Set methods
print(len(c))               # Prints the length of set

c.remove(100)          
print(c)                    # Removes the element

print(c.pop())              # It pops any random element
