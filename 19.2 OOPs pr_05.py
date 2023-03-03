# Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getTrainInfo(self):
        print(f"The name of train is {self.name}")
        print(f"{self.seats} seats are available")

    def getFareInfo(self):
        print(f"Your fare is {self.fare}$ ")


rjdexp = Train("Rajdhani Express: 14085", 5, 25)
# rjdexp.Train()
rjdexp.getTrainInfo()
rjdexp.getFareInfo()