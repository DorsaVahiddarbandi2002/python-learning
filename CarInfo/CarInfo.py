class Car:
    def __init__(self, Brand, Color, Company, Price, Year):
        self.Brand = Brand
        self.Color = Color
        self.Company = Company
        self.Price = Price
        self.Year = Year

    def __str__(self):
        c = f"Brand:{self.Brand} , Color:{self.Color} , Company:{self.Company} , Price:{self.Price} , Year:{self.Year}"
        return c

class BMW(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

        
class Benz(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Rolls_Royce(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Utopia(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Bugatti(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Bentley(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class AstonMartin(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Koenigsegg(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Ferrari(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model

class Lamborghini(Car):
    def __init__(self, Brand, Color, Company, Price, Year, Model):
        super().__init__(Brand, Color, Company, Price, Year)
        self.Model = Model




            
