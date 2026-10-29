class Shirt:
    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)

    def __del__(self):
        print("Shirt object destroyed")


s1 = Shirt()
s1.ShowBook()

s2 = Shirt(101, "Classic Shirt", "Formal", 800, "Large")
s2.ShowBook()