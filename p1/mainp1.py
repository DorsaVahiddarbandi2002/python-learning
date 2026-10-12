from p1 import Triangle , Routs , Prime , Note


def main():
    while True:
        print("1-Triangle")
        print("2-Routs")
        print("3-Prime")
        print("4-Note")
        print("5-Exit")
        option = int(input("choose from 1-5 :"))
        if option == 1:
            x = int(input("enter x:"))
            y = int(input("enter y:"))
            z = int(input("enter z:"))
            print(Triangle(x, y, z))
        elif option == 2:
            a = int(input("enter a:"))
            b = int(input("enter b:"))
            c = int(input("enter c:")) 
            print(Routs(a, b, c))
        elif option == 3:
            num = list(map(int , input("enter numbers with space between them :").split()))
            print(Prime(num))
        elif option == 4:
            notes = list(map(float , input("enter notes with space between them :").split()))
            print(Note(*notes))
        elif option == 5:
            print("finished")
        else:
            print("error!!!")


if __name__ == "__main__":
    main()
