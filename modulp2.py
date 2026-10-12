from p2 import four_char_name , name_note , Prime , change_word


def main():
    while True:
        print("1-four_char_name")
        print("2-name_note")
        print("3-Prime")
        print("4-change_word")
        print("5-Exit")
        option = int(input("choose from 1-5 :"))
        if option == 1:
            print(four_char_name())
        elif option == 2:
            names = []
            notes = []
            n = int(input("enter number of names and notes :"))
            for i in range(1,n+1):
                name = input(f"enter name{i}:")
                names.append(name)
            for i in range(1,n+1):
                note = int(input(f"enter note{i}:"))
                notes.append(note)
            print(name_note(names,notes))
        elif option == 3:
            num = list(map(int, input("enter numbers with space between them :").split()))
            print(Prime(num))
        elif option == 4:
            text = input("enter your text:")
            print(change_word(text))
        elif option == 5:
            print("finished")
        else:
            print("error!!!")


if __name__ == "__main__":
    main()
