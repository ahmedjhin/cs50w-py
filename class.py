class point:
    def __init__(self, capacity,): 
        self.capacity = capacity
        self.passenger = []
        
        
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name) 
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passenger)

flight = point(5)

pepole = ["Harry", "botter", "jetty"]

for person in pepole:
    Success = flight.add_passengers(person)
    if Success:
        print(f"Add {person} to flight successfully.")
    else:
        print(f"no   avalibale seats for {person}")


