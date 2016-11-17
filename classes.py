class Vehicle:
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        return "%s braking." %self.vtype +"\n"

    def drive(self):
        return "Im driving a "+self.color + " " + self.vtype + "\n"

#if __name__ == "__main__":
#    car = Vehicle("blue", 4, 5, "car")
#    print(car.brake())
#    print(car.drive())

#    truck = Vehicle("red", 3, 6, "truck")
#    print(truck.drive())
#    print(truck.brake())
    
class Car(Vehicle):

    def brake(self):    
        return "The car class is breaking slowly!"
    
if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    print(car.brake())
    print(car.drive())
