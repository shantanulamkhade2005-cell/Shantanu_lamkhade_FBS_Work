class Shirt:
    increment = 0.10

    def __init__(self, sid=0, sname="", type="", price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", self.price)

    def calculate_price(self):
        sizes = {"small": 0, "medium": 1, "large": 2, "xlarge": 3}
        self.price = self.price * (1 + Shirt.increment * sizes[self.size.lower()])
        print("Price according to size:", self.price)

    def __del__(self):
        print("Shirt object destroyed")


s1 = Shirt(101, "Classic Shirt", "Formal", 1000, "small")
s1.ShowBook()

s2 = Shirt(102, "Casual Shirt", "Casual", 1000, "large")
s2.ShowBook()
s2.calculate_price()