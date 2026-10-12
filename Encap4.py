class Car():
    def __init__(self, model, brand, speed):
        self.__model = model
        self.__brand = brand
        self.__speed = speed

    def getter_speed(self):
        return self.__speed

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
        else:
            print("Invalid amount!")

    def brake(self, amount):
        if amount > self.__speed:
            self.__speed = 0
        elif amount > 0:
            self.__speed -= amount
        else:
            print("Invalid amount!")
        return f"speed:{self.__speed}"
    
    def deleter_speed(self):
        del self.__speed
    


s1 = Car(input("whats the model:"), input("whats the brand:"), int(input("enter the speed:")))
#print(s1.getter_speed())
#print(s1.brake(50))
#print(s1.deleter_speed())
