# Q1. Write a program to find the greatest of four numbers entered by the user

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if(n1>n2):
    f1 = n1
else:
    f1 = n2

if(n3>n4):
    f2 = n3
else:
    f2 = n4


if(f1>f2):
    print(str(f1) + "is the greatest")
else:
    print(str(f2) + "is the greatest")

# Q2. A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

comment = input("Enter the comment: ")

if("make a lot of money" or "buy now" or "subscribe this" or "click this" in comment):
    print("SPAM!!")
else:
    pass

