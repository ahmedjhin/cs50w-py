class flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassengers(self, name):
        if  not self.openseats():
            return False
        self.passengers.append(name)
        return True
    
    def openseats(self):
        return self.capacity - len(self.passengers)
    
pepole = ["ali", "naser" ,"ahmed"]
point = flight(2)



for person in pepole:
    sucss = point.addPassengers(person)
    if  sucss:
         print(f"added {person}")
    else:
        print(f"not add {person}")



name = ['one','tow','three']      