# Add a static method in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"The square of {self.num} is {self.num**2}")

    def squareRoot(self):
        print(f"The square root of {self.num} is {self.num**0.5}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num**3}")

    @staticmethod
    def greet():
        print("Hello and welcome to the best calculator!!!!! ")

a = Calculator(4)
a.square()
a.squareRoot()
a.cube()
a.greet()
