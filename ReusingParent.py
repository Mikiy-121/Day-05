class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance) # parent
        self.rate = rate # extra

    def add_interest(self):
        self.balance += self.balance * self.rate