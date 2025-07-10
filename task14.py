class Student:
    def __init__(self , name , age ):
        self.name = name
        self.age = age
        


    def show_info(self):
        print(f"{self.name} , {self.age} yoshda") 

s1 = Student("Abdurauf", 19)
s2 = Student("Artur", 20)
s3 = Student("Jahongir", 21)
s4 = Student("Guli", 18)
s5 = Student("Feride", 20)

students = [s1, s2, s3, s4, s5]

kattasi = max(students, key=lambda student: student.age)
print("Eng katta yoshdagi talaba:")
kattasi.show_info()