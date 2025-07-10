class BankAccount :
    def __init__(self, owner, balance :int):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance +=amount
        return f"{self.owner} yangi hisobingiz {self.balance} sum"
        
    
    def withdraw(self, amount):
        if self.balance > amount :
            self.balance -= amount
            return f"{self.owner} yangi hisobingiz {self.balance} sum"
        else:
            return "sizda xatolik vujudga keldi"
    def show_balance(self):
        return f"{self.owner} hisobingizda {self.balance} summa bor"
    
amount = int(input("summani kiriting: "))
obj1 =BankAccount("Abdurauf", 1000)
obj2 =BankAccount("Artur", 2000)
obj3 =BankAccount("Jahon", 3000)

print(obj1.deposit(amount))
print(obj2.withdraw(amount))
print(obj3.show_balance())




