import csv

class MyClass():
    def __init__(self):
        self.todoLIST = []

    def Task(self):
        while True:
            name = input("Enter the subject: ")
            explanation = input("What is your explanation? ")
            priority = input("Priority (high, normal, low): ")

            task = {
                "name": name,
                "explanation": explanation,
                "priority": priority
            }
            self.todoLIST.append(task)
            
            again = input("Do you want to add another task? (yes/no): ")
            if again.lower() == "no":
                print("finished")
                break

        print(self.todoLIST)
                    

    
    def add(self):
        while True:
            name = input("Enter the subject: ")
            explanation = input("What is your explanation? ")
            priority = input("Priority (high, normal, low): ")

            task = {
                "name": name,
                "explanation": explanation,
                "priority": priority
            }

            self.todoLIST.append(task)
            again = input("Do you want to add another work? (yes/no): ")
            if again.lower() == "no":
                print("finished")
                break


    def remove(self):
        work = input("what is the work?")
        if work in self.todoLIST:
            self.todoLIST.remove(work)
        else:
            print("This work is not in the list.")


    def show(self):
        print(self.todoLIST)


    def save(self):
        print(self.todoLIST)
        
        with open("tasks.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "explanation", "priority"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.todoLIST)
        print("Tasks saved successfully!")
            



