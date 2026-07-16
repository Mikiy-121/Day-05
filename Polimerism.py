accounts = [
Account("Hanna", "CBE-1", 1500),
SavingsAccount("Almaz", "CBE-2", 1500),
CurrentAccount("Dawit", "CBE-3", 800),
]
for acc in accounts:
    acc.statement() # the right version runs