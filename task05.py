class Product:
    def __init__(self, name, price:int, category, in_stock):
        self.name = name
        self.price = price 
        self.category = category
        self.in_stock = in_stock
    
fruit = Product("apple", 10000, "fruits", True)
veg = Product("potatoe", 6500, "vegatables", False)
print(f"meva nomi {fruit.name} \n narxi {fruit.price}")
print(f"sabzavot turi {veg.name} \n narxi {veg.price}")