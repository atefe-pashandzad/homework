from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class mostatil(Shape):
    def __init__(self, arz, tol ):
        self.arz = arz
        self.tol = tol

    def calculate_area(self):
        return self.arz * self.tol

    def calculate_perimeter(self):
        return 2 * (self.arz + self.tol)

class dayere(Shape):
    def __init__(self, shoaa):
        self.shoaa = shoaa

    def calculate_area(self):
        return 3.14 * self.shoaa ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.shoaa
    
shapes = [mostatil(2, 4), dayere(4)]

for s in shapes:
    
    print("masaht", s.calculate_area(), "mohit", s.calculate_perimeter())
