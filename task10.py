class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Sizning yangi balansingiz: {self.balance} so'm"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Hisobdan {amount} so'm yechildi. Qolgan: {self.balance} so'm"
        else:
            return f"Xatolik: hisobda yetarli mablag' yo'q! (Balans: {self.balance} so'm)"

account = BankAccount("Abdurauf", 100000)

print("1) Deposit\n2) Withdraw")
choice = int(input("Quyidagilardan birini tanlang: "))

if choice == 1:
    amount = int(input("Qoshmoqchi bolgan summani kiriting: "))
    print(account.deposit(amount))
elif choice == 2:
    amount = int(input("Yechmoqchi bolgan summani kiriting: "))
    print(account.withdraw(amount))
else:
    print("Notogri tanlov")
