from math import sqrt

def Triangle(x, y, z):
    if x < y + z and y < x + z and z < y + x:
        print("Triangle")
        if x == y == z:
            print("mo_azlaa")
        elif x == y or y == z or z == x:
            print("mo_sagh")
        elif x**2 == y**2 + z**2 or y**2 == x**2 + z**2 or z**2 == y**2 + x**2:
            print("ghaem_zav")
        else:
            print("mokh_azlaa")
    else:
        print("not Triangle!")


        return Triangle(x, y, z)
    

def Routs(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
    else:
        print("error!!")

    return f"roots: {x1:.2f}, {x2:.2f}"



def Prime(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2,num):
            if num % i == 0:
                return False
            
        return True

    c = 0
    primes = []
    for i in lst:
        if is_prime(i):
            c+=1
            primes.append(i)

    return f"number of primes:{c},primes:{primes}"


def Note(*args):
    avg = sum(args) / len(args)

    result = []

    for Note in args:
        if Note > avg:
            result.append(Note)

    return f"average: {avg:.2f}, above average: {result}"
