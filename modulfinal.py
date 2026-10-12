from finalexamtamrin import MyClass

def main():
    while True:
        print("1-Lines")
        print("2-Primes")
        print("3-four_char_names")
        print("4-change_word")
        print("5-exit")
        option = int(input("choose from 1-5 :"))
        if option == 1:
            mc1 = MyClass()
            mc1.Lines(input("choose filename1 :"), input("choose filename2 :"))
        elif option == 2:
            mc1 = MyClass()
            mc1.Primes(input("choose filename1 :"), input("choose filename2 :"))
        elif option == 3:
            mc1 = MyClass()
            mc1.four_char_names(input("choose filename1 :"), input("choose filename2 :"))
        elif option == 4:
            mc1 = MyClass()
            mc1.change_word(input("choose filename1 :"), input("choose filename2 :"))
        elif option == 5:
            print("finished")
        else:
            print("error")

if __name__ == "__main__":
    main()
