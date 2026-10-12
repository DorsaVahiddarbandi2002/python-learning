def four_char_name():
    lst = []
    n = int(input("enter n :"))
    for i in range(1,n+1):
        name = input(f"enter name{i}:")
        lst.append(name)
    c = 0
    newlst = []
    for word in lst:
        if len(word) == 4:
            c += 1
            newlst.append(word)

    return f"number of four_char_names:{c},four_char_names:{newlst}"


def name_note(name, note):
    result = list(zip(name,note))
    result.sort(reverse=True)

    return f"sorted list name and notes:{result}"

lst = []
def Prime(lst):
    def is_prime(num):
        if num < 2:
            return False
        
        for i in range(2,num):
            if num % i == 0:
                return False
            
        return True

    result = []
    c = 0
    for i in lst:
        if is_prime(i):
            c+=1
            result.append(i)

    return f"number of primes:{c},primes:{result}"


def change_word(text):
    words = text.split()

    if words[2] == "python":
        words[2] = "cplusplus"
    if words[5] == "python":
        words[5] = "cplusplus"

    return " ".join(words)
