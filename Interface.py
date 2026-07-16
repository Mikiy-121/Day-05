class Account(ABC):
    @abstractmethod
    def calculate_interest(self): ...
class SavingsAccount(Account):
    def calculate_interest(self): # fulfils contract
        return self.balance * 0.05
class CurrentAccount(Account):
    def calculate_interest(self): # different rule
        return 0 # current accounts earn no interest