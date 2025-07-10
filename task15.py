class Product:
    def __init__(self, name , price , in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

p1 = Product("Telefon", 250.00, True)
p2 = Product("Quloqchin", 15.50, False)
p3 = Product("Noutbuk", 1200.00, True)
p4 = Product("Sichqoncha", 20.00, True)
p5 = Product("Monitor", 180.00, False)

products = [p1, p2 ,p3 , p4 , p5 ]

jami_price = sum(product.price for product in products if product.in_stock)
print(f"Ombordagi mahsulotlar narxi: {jami_price:.2f}")


        