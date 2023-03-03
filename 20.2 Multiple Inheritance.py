# Multiple inheritances occurs when the child class inherits from more than one parent class

class Employee:
    company = "Google"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 2

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
# p.upgradeLevel()
print(p.company)