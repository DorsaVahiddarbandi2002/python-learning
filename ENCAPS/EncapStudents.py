class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def getter_score(self):
        return self.__score

    def setter_score(self, score):
        if 0 < score <= 20:
            Newscore = int(input("enetr the new score :"))
            self.__score = Newscore
        else:
            print("Invalid score!")
        print("new score is:",Newscore)

s1 = Student(input("enter the name of the student:"),int(input("enter the score of the student:")))
#print(s1.getter_score())
print(s1.setter_score(12))
