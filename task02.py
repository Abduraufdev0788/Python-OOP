class Student : 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
def text():
    return f"Salom mening ismim {student_data.name} va mening yoshim {student_data.age}. Men {student_data.grade}man."


student_data = Student("Abdurauf", 19, "2-kurs")

print(text())