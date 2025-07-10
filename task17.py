class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} hisobidagi balans: {self.balance} so'm")

    def get_balance(self):
        return self.balance
    

acc1 = BankAccount("Abdurauf", 150000)
acc2 = BankAccount("Artur", 225000)
acc3 = BankAccount("Jahon", 50000)
acc4 = BankAccount("Guli", 100000)
acc5 = BankAccount("Feride", 175000)

accounts = [acc1, acc2, acc3, acc4, acc5]

total_balance = 0

for account in accounts:
    total_balance += account.get_balance()
print(f" Barcha hisoblar boyicha jami balans: {total_balance} so'm")
for account in accounts:
    account.show_balance()