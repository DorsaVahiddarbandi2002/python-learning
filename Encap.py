class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 < score <= 20:
            self.__score = score
        else:
            print("Invalid score!")

student = Student("Dorsa", 18)
#print(student.get_score())
student.set_score(20)
print(student.get_score())

#student.set_score(25)