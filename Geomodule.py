from Geometricshapes import Rectangle , Triangle , Circle , Square

def main():
    while True:
        print("1-Rectangle")
        print("2-Triangle")
        print("3-Circle")
        print("4-Square")
        print("5-Exit")
        option = int(input("choose from 1-5:"))
        if option == 1:
            r1 = Rectangle(int(input("enter width:")), int(input("enter height:")))
            print(r1.Area())
            print(r1.Perimeter())
        elif option == 2:
            t1 = Triangle(int(input("enter side1:")), int(input("enter side2:")), int(input("enter side3:")), 
            int(input("enter base:")), int(input("enter height:")))
            print(t1.Area())
            print(t1.Perimeter())
        elif option == 3:
            r1 = Circle(int(input("enter Radius::")))
            print(r1.Area())
            print(r1.Perimeter())
        elif option == 4:
            S1 = Square(int(input("enter a::")))
            print(S1.Area())
            print(S1.Perimeter())
        elif option == 5:
            print("finished")
        else:
            print("error!")

if __name__ == "__main__":
    main()
            
                
                    