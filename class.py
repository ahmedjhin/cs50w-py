class point:
    def __init__(self, capacity,): 
        self.capacity = capacity
        self.passanger = []
        
    def add_passengerss(self, name):
        if not self.open_seats():
            return False
        self.passanger.append(name) 
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passanger)

flight = point(5)

pepole = ["Harry", "ron", "jetty", "kubo"]

for person in pepole:
    Success = flight.add_passengerss(person)
    if Success:
        print(f"Add {person} to flight successfully.")
    else:
        print(f"no   avalibale seats for {person}")


