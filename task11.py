class Book:
    def __init__(self, title, author, isread = False ):
        self.title = title
        self.author = author
        self.isread = isread
        
    def mark_as_read(self):
        self.isread = True
        print(f"{self.isread} kitob oqilgan deb belgilandi")
    def status(self):
        if self.isread :
            print(f"{self.title} o'qildi")
        else:
            print(f"{self.title} o'qilmadi")

book1 = Book("Sariq devni minib", "Xudoberdi Tuxtaboyev")
book1.status()
book1.mark_as_read()
book1.status()
