class MyClass:
    def Lines(self, filename1, filename2):
        try:
            with open(filename1, "r") as f1 ,open(filename2, "w") as f2:
                n = len(f1.readlines()) 
                f2.write(f"number of lines : {n}")
        except Exception as e:
            print(e)


    def Primes(self, filename1, filename2):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2,n):
                if n % i == 0:
                    return False
            return True

        try:
            with open(filename1, "r") as f1 ,open(filename2, "w") as f2:
                lst = f1.read().split()
                c = 0
                primes = []
                for i in lst:
                    if i.isnumeric():
                        i = int(i)
                        if is_prime(i):
                            c += 1
                            primes.append(i)
                f2.write(f"number of primes : {c}, primes : {primes}")
        except Exception as e:
            primes(e)


    def four_char_names(self, filename1, filename2):
        try:
            with open(filename1, "r") as f1 ,open(filename2, "w") as f2:
                four_characs = []
                c = 0
                s = f1.read().split()
                for word in s:
                    if len(word) == 4:
                        c += 1
                        four_characs.append(word)
                f2.write(f"number of the four_char_names : {c}, four_char_names : {four_characs}")
        except Exception as e:
            print(e)


    def change_word(self, filename1, filename2):
        try:
            with open(filename1, "r") as f1 ,open(filename2, "w") as f2:
                s = f1.read().split()
                new_words = []
                for word in s:
                    if word.lower() == "python":
                        word = "cplusplus"
                    new_words.append(word)
                f2.write(" ".join(new_words))
        except Exception as e:
            print(e)
            


                    

                

                
        