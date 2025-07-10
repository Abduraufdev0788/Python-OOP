class Product:
    def __init__(self, name, price:int, category, in_stock):
        self.name = name
        self.price = price 
        self.category = category
        self.in_stock = in_stock
        
    def check_stock(self):
        if self.in_stock == True :
            print(f"{self.name} dokonda mavjud")
        else:
            print(f"{self.name} hozirda mavjud emas")
    
fruit = Product("apple", 10000, "fruits", True)
veg = Product("potatoe", 6500, "vegatables", False)

fruit.check_stock()
veg.check_stock()
