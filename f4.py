class MyClass:
    @staticmethod
    def Triangle(filename1, filename2):
        with open(filename1, 'r') as f1, open(filename2, "w") as f2:
            s = f1.read()
            s = s.split()
            a = int(s[0])
            b = int(s[1])
            c = int(s[2])
            if a < b + c and b < a + c and c < b + a:
                f2.write("is triangle and its ")
                if a == b == c:
                    f2.write("mot_azlaa")
                elif a == b or b == c or a == c:
                    f2.write("mot_saghein")
                elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
                    f2.write("gheam_zavie")
                else:
                    f2.write("mokh_azlaa")
            else:
                f2.write("not triangle!")

tr1 = MyClass()
print(tr1.Triangle("text.txt","newfile2.txt"))
