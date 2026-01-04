
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Year:", self.year)
class Car(Vehicle):
    def __init__(self, brand, year, num_dors):
        super().__init__(brand, year)
        self.num_dors = num_dors

    def display_info(self):
        super().display_info()
        print("tedad dr:", self.num_dors)


class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print("Has sidecar:", self.has_sidecar)

Vehicle = Vehicle("sm", 1337)
car = Car("samand", 1384 , 4)
Motorcycle = Motorcycle("apachi", 1357 , "Yes")

print("etelat")
Vehicle.display_info()
print("etelat")
car.display_info()
print("etelat")
Motorcycle.display_info()

