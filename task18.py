class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f" {self.name} — {self.price} so'm")

p1 = Product("Smartfon", 2500000, "Electronics")
p2 = Product("Televizor", 4500000, "Electronics")
p3 = Product("Notebook", 6500000, "Electronics")
p4 = Product("Stol", 300000, "Furniture")
p5 = Product("Kiyim", 150000, "Apparel")
p6 = Product("Sovutkich", 5000000, "Appliance")

products = [p1, p2, p3, p4, p5, p6]

max_product = max(products, key=lambda product: product.price)
print(" Eng qimmat mahsulot:")
max_product.info()