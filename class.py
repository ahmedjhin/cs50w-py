# class point:
#     def __init__(self, capacity,): 
#         self.capacity = capacity
#         self.passenger = []
        
        
#     def add_passengers(self, name):
#         if not self.open_seats():
#             return False
#         self.passenger.append(name) 
#         return True
    
#     def open_seats(self):
#         return self.capacity - len(self.passenger)

# flight = point(5)

# pepole = ["Harry", "botter", "jetty"]

# for person in pepole:
#     Success = flight.add_passengers(person)
#     if Success:
#         print(f"Add {person} to flight successfully.")
#     else:
#         print(f"no   avalibale seats for {person}")


# class point():
#     def __init__(self,input1, input2):
#         self.x = input1
#         self.y = input2

# p = point(2,8)

# print(p.x)
# print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    
    def addpasengers(self, name):
        self.passengers.append(name)\
    
    def openseats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
pasengerzz = ['ahmed', 'moaz','abdo']
flight.addpasengers(pasengerzz)