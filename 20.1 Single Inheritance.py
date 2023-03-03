# Single inheritance occurs when a child class inherits only a single parent class.
# Base -> Derived

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee") 

class Programmer(Employee):
    language = "Python"

    def showLanguage(self):
        print(f"The language is {self.language}")

e = Employee()
p = Programmer()

p.showDetails()
