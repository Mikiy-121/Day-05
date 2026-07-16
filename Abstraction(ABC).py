from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

# Account() -> TypeError: can't instantiate
# every child MUST implement calculate_interest