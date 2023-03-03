# When a child class becomes a parent for another child class.

class Child:
    name = "baccha"

    def chotaBaccha(self):
        print("I am a kid")

class Teen(Child):
    drive = "yes"

    def earning(self):
        print(f"The earning is {self.earning}")

    def chotaBaccha(self):
        print("I am bada baccha .... not kid anymore")

class Adult(Teen): 
    profession = "Businessman"

    def earning(self):
        print(f"No salary to adults")

c = Child()
print(c.name)

t = Teen()
print(t.name)

a = Adult()
print(a.name)
