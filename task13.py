class Book:
    def __init__(self, title, author, ):
        self.title = title
        self.author = author
        self.is_read = False
        
    def mask_as_read(self):
        self.is_read = True
    def status(self):
        if self.is_read:
            print(f"{self.title} — Oqilgan")
        else:
            print(f"{self.title} — Oqilmagan")
    
book1 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")
book2 = Book("Dunyo ishlari", "O'tkir Hoshimov")
book3 = Book("Alkimyogar", "Paulo Koelho")
book4 = Book("Jimjitlik", "Erkin A'zam")

books = [book1, book2, book3, book4]
print("Kitoblar ro'yxati va o'qilish holati:\n")
for book in books:
    book.status()