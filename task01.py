class Car :
    def __init__(self, brand,model, year): 
        self.brend = brand
        self.model = model
        self.year = year
        
car_data = Car("GM", "onix", 2024)
print(car_data.brend)
print(car_data.model)
print(car_data.year)