# The block keeps executing until the condition is true/false. In while loops, the condition is checked first.
# If it evaluates to true, the body of the loop is executed, otherwise not!
# If the loop is entered, the process of condition check and execution is continued until the condition becomes false.

# Printing 1 to 50
# i = 1
# while(i<51):
#     print(i)
#     i = i+1


# Multiplication Table

num = int(input("Enter the number: "))
i = 1
while(i<=10):
    print(str(num) + " * " + str(i) + " = " + str(num * i))
    i+=1