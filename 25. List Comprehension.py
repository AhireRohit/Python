# It is an elegant way to create list using existing lists.
# It is used for list, tuples, sets and even dictionary.

a = [45, 562 ,41 ,45, 55 ,44, 98, 78, 25, 100, 3, 79]

b = [i for i in a if i%2 == 0]
c = [i for i in a if i>8]
print(b)
print(c)