class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.balance}")

Joe = User("Joe", 500)
John = User("John", 1000)
Ana = User("Ana", 5000)
Joe.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200)
John.make_deposit(2000).make_deposit(5000).make_withdrawal(1600).make_withdrawal(400)
Ana.make_deposit(2000).make_withdrawal(500).make_withdrawal(160).make_withdrawal(40)
Joe.display_user_balance()
John.display_user_balance()
Ana.display_user_balance()