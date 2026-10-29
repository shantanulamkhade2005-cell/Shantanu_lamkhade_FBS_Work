
class Book:
    count = 0

    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    def __del__(self):
        print("Book object destroyed")

b1 = Book()
b1.ShowBook()

b2 = Book(101, "Python", 500, "Guido")
b2.ShowBook()

print("Total objects created:", Book.count)
