class Account:
    def statement(self):
        print(f"{self.owner}: {self.balance} ETB")

class CurrentAccount(Account):
    def statement(self): # override
        print(f"[Current] {self.owner}: "
f"{self.balance} ETB "
f"(overdraft {self.overdraft})")