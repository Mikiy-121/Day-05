from abc import ABC, abstractmethod

from Interface import SavingsAccount
class Account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

# Account() -> TypeError: can't instantiate
# every child MUST implement calculate_interest

def total_interest(accounts):
    return sum(a.calculate_interest()
               for a in accounts)

accounts = [SavingsAccount(...),
CurrentAccount(...)]
total_interest(accounts) # just works