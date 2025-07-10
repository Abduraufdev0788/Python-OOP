class Movie:
    def __init__(self,title,genre,duration:float,rating:int):
        self.title = title
        self.genre = genre
        self.duration = duration 
        self.rating = rating
        
full_movies = Movie("Uyda yolgiz", "interesting",150, 5.5)
a = full_movies.duration % 60
b = full_movies.duration //60
print(f" film nomi {full_movies.title} \n filmning janri {full_movies.genre} \n filning davomizligi {a}h : {b}min \n reyting darajasi {full_movies.rating}")
        