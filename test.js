class Shape {
 let width = 10;
 let height = 10;
 rectangle(){
    this.width * this.height;
 }


 circle(){
    // 
 }

 init(){
    rectangle();
    circle()
 }
}
myClass(1,2,4).init();

// https://leetcode.com/problems/divide-two-integers/
10 / 5 % *
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

pepole = ["Harry", "jetty", "jetty"]

for person in pepole:
    Success = flight.add_passengers(person)
    if Success:
        print(f"Add {person} to flight successfully.")
    else:
        print(f"no   avalibale seats for {person}")


