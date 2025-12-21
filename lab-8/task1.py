class Bank:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостатньо коштів")

    def get_balance(self):
        return self._balance

if __name__ == "__main__":
    account = Bank(1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Поточний баланс: {account.get_balance()}")