from math import sqrt
from math import pi

class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def Area(self):
        area = self.w * self.h
        return f"area:{area}"

    def Perimeter(self):
        perimeter = (self.w + self.h)*2
        return f"perimeter:{perimeter}"

class Triangle():
    def __init__(self, side1, side2, side3, base, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height

    def Area(self):
        if self.side1 == self.side2 == self.side3:
            print("mot_azlaa")
            area = (sqrt(3)/4)(self.side1 **2 )
        elif self.side1 == self.side2 or self.side3 == self.side2 or self.side1 == self.side3:
            print("mot_sagh")
            area = (self.base * self.height)/2
        elif (self.side1**2) == (self.side2**2) + (self.side3**2) or (self.side2**2) == (self.side1**2) + (self.side3**2) or (self.side3**2) == (self.side2**2) + (self.side1**2):
            print("ghaem_zavie")
            area = (self.side1*self.base)/2
        else:
            print("mokh_azlaa")
            area = (self.base * self.height)/2


        return f"area : {area}"
        
    def Perimeter(self):
        if self.side1 == self.side2 == self.side3:
            perimeter = self.side1 * 3
        elif self.side1 == self.side2 or self.side3 == self.side2 or self.side1 == self.side3:
            perimeter = (2 * self.side1) + self.side2
        elif (self.side1**2) == (self.side2**2) + (self.side3**2) or (self.side2**2) == (self.side1**2) + (self.side3**2) or (self.side3**2) == (self.side2**2) + (self.side1**2):
            perimeter = self.side1 + self.side2 + self.side3
        else:
            perimeter = self.side1 + self.side2 + self.side3


        return f"perimeter : {perimeter}"

class Circle():
    def __init__(self, r):
        self.r = r

    def Area(self):
        area = pi * self.r * self.r
        return f"area : {area:.2f}"

    def Perimeter(self):
        perimeter = 2 * pi * self.r
        return f"perimeter : {perimeter:.2f}"


class Square():
    def __init__(self, a):
        self.a = a

    def Area(self):
        area = self.a ** 2
        return f"area : {area}"
    
    def Perimeter(self):
        perimeter = 4 * self.a
        return f"perimeter : {perimeter}"
