# The random access memory(RAM) is volatile, and all its contents are lost once a program terminates.
# THe HDD is non volatile, and contents are saved after program is terminated.
# In order to persist the data forever, we use files.

# A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

# There are 2 types of files:

#     Text files (.txt, .c, etc)
#     Binary files (.jpg, .dat, etc)

# Python has a lot of functions for reading, updating, and deleting files.

# Opening a file 
# Python has an open() function for opening files. It takes 2 parameters: filename and mode.

open("18.1 text.txt", "r")

# Here, "18.1 text.txt" is the file name and "r" is the mode of opening (read mode)

# Reading a file in Python

f = open("18.1 text.txt", "r")     #Opens the file in r mode

text = f.read()          #Read its content

print(text)     #Print its contents

# We can also specify the number of characters in read() function:

f.read(2)       #Reads first 2 characters

# We can also use f.readline() function to read one full line at a time.

f.readline()  


f.close()         #Close the fie

