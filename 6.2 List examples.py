# Q1. Write a program to store seven fruits in a list entered by the user.

f1 = input("Enter fruit number 1: ")
f2 = input("Enter fruit number 2: ")
f3 = input("Enter fruit number 3: ")
f4 = input("Enter fruit number 4: ")
f5 = input("Enter fruit number 5: ")
f6 = input("Enter fruit number 6: ")
f7 = input("Enter fruit number 7: ")

mylist = [f1, f2, f3, f4, f5, f6, f7]
print(mylist)

# Q2. Write a program to accept the marks of 6 students and display them in a sorted manner.

s1 = input("Enter marks of student 1: ")    
s2 = input("Enter marks of student 2: ")    
s3 = input("Enter marks of student 3: ")    
s4 = input("Enter marks of student 4: ")        
s5 = input("Enter marks of student 5: ")    
s6 = input("Enter marks of student 6: ")    

marks = [s1, s2, s3, s4, s5, s6]
marks.sort()
print(marks)

# Q3. Write a program to sum a list with numbers.

s = [25, 75, 100, 85 ,741 ,25, 1, -99, 5.305]
print(sum(s))