# Create a class programmer for storing information of a few programmers working at Microsoft.

class programmer:
    company = "Microsoft"
    def __init__(self, name, company):
        self.name = name
        self.company = company
    
    def getInfo(self):
        print(f"Name of Employee is {self.name}")
        print(f"Company name is : {self.company}")

rohit = programmer("Rohit", "Github")
harry = programmer("Harry", "YouTube")

# programmer.getInfo()
harry.getInfo()