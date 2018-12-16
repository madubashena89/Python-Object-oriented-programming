class Book:
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Title: {}, Authur: {}, Pages: {}" .format(self.title, self.author, self.pages)

    def  Read(self):
        print("Hi please read this book")

    def __len__(self):
       return self.pages

b = Book("Python", "Jose", 200)
print(b)

b.Read()
print(len(b))
