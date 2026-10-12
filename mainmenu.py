from toDoList import MyClass

def main():
    mc1 = MyClass()
    while True:
        print("1-Task")
        print("2-ToDoList")
        print("3-exit")
        option = int(input("choose from 1-3 :"))
        if option == 1:
            mc1.Task()
        elif option == 2:
            print("1-add")
            print("2-remove")
            print("3-show")
            print("4-save")
            new2option = int(input("choose from 1-4 :"))
            if new2option == 1:
                mc1.add()
            elif new2option == 2:
                mc1.remove()
            elif new2option == 3:
                mc1.show()
            elif new2option == 4:
                mc1.save()
                break
            else:
                print("error!")
        elif option == 3:
            print("finished")
        else:
            print("error")

if __name__ == "__main__":
    main()