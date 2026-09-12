class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
book1 = Book("Atomic Habits", "James clear", 256)
book2 = Book("The psychology of money", "Morgan Housel", 412)
print(f"{book1.title} by {book1.author}, has {book1.pages} pages")
print(f"{book2.title} by {book2.author}, has {book2.pages} pages")
