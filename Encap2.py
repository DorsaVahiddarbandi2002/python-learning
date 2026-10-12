class BankAccount():
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

account = BankAccount("Dorsa", 1000)
print(account.get_balance())
