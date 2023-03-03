# Super method is used to access the methods of a superclass in the derived class.

class Child:
    name = "baccha"

    def chotaBaccha(self):
        print("I am a kid")

class Teen(Child):
    drive = "yes"

    def earning(self):
        print(f"The earning is {self.earning}")

    def chotaBaccha(self):
        super().chotaBaccha()
        print("I am bada baccha .... not kid anymore")

class Adult(Teen): 
    profession = "Businessman"

    

    def earning(self):
        print(f"No salary to adults")

    def chotaBaccha(self):
        super().chotaBaccha()
        print("I am a Father!!!")


# c = Child()
# print(c.name)

t = Teen()
# print(t.name)
t.chotaBaccha()

a = Adult()
# print(a.name)
a.chotaBaccha()
