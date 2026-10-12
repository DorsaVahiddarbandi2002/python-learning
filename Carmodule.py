from CarInfo import Car, BMW, Benz, Rolls_Royce, Utopia, Bugatti, Bentley, AstonMartin, Koenigsegg, Ferrari, Lamborghini

def main():
    while True:
        print("1-BMW")
        print("2-Benz")
        print("3-Rolls_Royce")
        print("4-Utopia")
        print("5-Bugatti")
        print("6-Bentley")
        print("7-Aston")
        print("8-Koenigsegg")
        print("9-Ferrari")
        print("10-Lamborghini")
        print("11-Exit")
        option = int(input("choose from 1-11:"))
        if option == 1:
            bMW = BMW("BMW", "Black", "BMW AG", 75000, 2025, "X5")
            print("bMW:",bMW)
        elif option == 2:
            benz = Benz("Benz", "Gray", "Mercedes-Benz", 68000, 2026, "C200")
            print("benz:",benz)
        elif option == 3:
            rolls_royce = Rolls_Royce("Rolls-Royce", "Black", "Rolls-Royce Motor Cars", 500000, 2026, "Phantom")
            print("rolls_royce:",rolls_royce)
        elif option == 4:
            utopia = Utopia("Pagani", "Blue", "Pagani Automobili", 2500000, 2026, "Utopia")
            print("Utopia:",utopia)
        elif option == 5:
            bugatti = Bugatti("Bugatti", "Black", "Bugatti Automobiles", 3800000, 2026, "Tourbillon")
            print("Bugatti:",bugatti)
        elif option == 6:
            bentley = Bentley("Bentley", "Dark Green", "Bentley Motors", 250000, 2026, "Flying Spur")
            print("Bentley:",bentley)
        elif option == 7:
            aston = AstonMartin("Aston Martin", "Green", "Aston Martin", 3000000, 2026, "Valkyrie")
            print("AstonMartin:",aston)
        elif option == 8:
            koenigsegg = Koenigsegg("Koenigsegg", "Silver", "Koenigsegg Automotive", 3000000, 2026, "Jesko Absolut")
            print("Koenigsegg:",koenigsegg)
        elif option == 9:
            ferrari = Ferrari("Ferrari", "Red", "Ferrari", 400000, 2026, "Purosangue")
            print("Ferrari:",ferrari)
        elif option == 10:
            lamborghini = Lamborghini("Lamborghini", "Yellow", "Automobili Lamborghini", 600000, 2026, "Revuelto")
            print("Lamborghini:",lamborghini)
        elif option == 11:
            print("finished")
            break
        else:
            print("error!!")

if __name__ == "__main__":
    main()