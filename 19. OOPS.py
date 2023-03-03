# Solving a problem by creating objects is one of the most popular approaches in programming. This is called object-oriented programming.
# This concept focuses on using reusable code. (Implements DRY[Dont't repeat yourself] principle)

# Class
# A class is a blueprint for creating objects.

# Object
# An object is an instantiation of a class. When class is defined, a template(info) is defined. Memory is allocated only after object instantiation.

# Modelling a problem in OOPs
# We identify the following in our problem
# Noun -> Class -> Employee
# Adjective -> Attributes -> name,age,salary
# Verbs -> Methods -> getSalary(), increment()

class railwayForm:
    formType = "Railwayform"                # --> Class Attributes -->  An attribute that belongs to the class rather than a particular object.


    def printData(self):
        print(f"Name is: {self.name}")
        print(f"Name is: {self.train}")

rohitapp = railwayForm()
rohitapp.name = "Rohit"                    # --> Instance Attributes --> An attribute that belongs to the Instance (object) Assuming the class from the previous example:
rohitapp.train = "Rajdhani Exp"
rohitapp.printData()

class company:
   salary = 200
   dept = "R&D"

harry = company()
# harry.salary = 500
print(harry.dept)
company.dept = "HR"
# print(harry.salary) 
print(harry.dept)

# ‘self’ parameter
# self refers to the instance of the class. It is automatically passed with a function call from an object.
# here, self is harry, and the above line of code is equivalent to Employee.getSalary(harry)

# This function getsalary is defined as:

class Employee:
	company = "“Google”"
	def getSalary(self):
		print("“Salary is not there”")
harry = Employee()
harry.getSalary()