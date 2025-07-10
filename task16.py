class Book:
    def __init__(self , title , outhor , is_read =False):
        self.title = title
        self.outhor = outhor
        self.is_read = is_read


    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} , oqildi deb hisoblandi")

    def status(self):
        if self.is_read :
            print(f"{self.title}, oqildi")      
        else:
            print(f"{self.title} , oqilmadi")



book1 = Book("Alkimyogar", "Paulo Coelho")
book2 = Book("Shum bola", "G'afur G'ulom")
book3 = Book("Dunyo ishlari", "O'tkir Hoshimov")
book4 = Book("Ikki eshik orasi", "O'tkir Hoshimov")
book5 = Book("Oq kema", "Chingiz Aytmatov")

books = [book1, book2, book3, book4, book5]

book1.mark_as_read()
book4.mark_as_read()

print("barcha kitoblar holati")
for book in books:
    book.status()           


        