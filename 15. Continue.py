# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the program to “skip this iteration.”

# ‘break’ is used to come out of the loop when encountered. It instructs the program to – Exit the loop now

# for i in range(0, 11):                 # Here 0 to 11 is range
#     if (i == 5):
#         continue
#     print(i)


# Multiplication using for loop

num = int(input("Enter the number : "))
for i in range(1, 11):
    print(str(num) + " * " + str(i) + " = " + str(i*num))