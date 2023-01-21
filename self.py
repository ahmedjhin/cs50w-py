class point:
    def __init__(self, passengersCount,):
        self.passengersCount = passengersCount
        self.namesOfPassengers = []


    def addPassengers(self, name):
        if not openSeats(self):
           return False
        self.namesOfPassengers.append(name)
        return True


flightf = point(5)

users = ["ali", "ahmed", "mohamed"]


def openSeats(self):
     return self.passengersCount - len(self.namesOfPassengers)

for names in users:
    succesc = flightf.addPassengers(names)
    if succesc:
        print(f"add {names} succsfle")
    else:
        print(f"no avalibale seats for {names}") 

