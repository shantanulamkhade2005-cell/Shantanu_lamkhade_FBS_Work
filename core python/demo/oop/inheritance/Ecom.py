class Product():
    def __init__(self,id,name,price):
        self.name=name
        self.id=id
        self.price=price

    def getID(self):
        return self.id  
    def setID(self,newId):
        self.id=newId

    def getName(self):
        return self.name    
    def setName(self,newName): 
        self.name=newName   

    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice

    def display(self):
        print(f"Id={self.id}\t Name={self.name}\t price={self.price}\t")

class Digital(Product):
    def __init__(self,id,name,price,link):
        super().__init__(id,name,price)
        self.link=link
    def getlink(self):
        return self.link
    def setlink(self,nlink):
        self.link=nlink
    def display(self):
        print(f'Link={self.link}')
        super().display()

class PhyicPro(Product):
    def __init__(self,id,name,price,add):
        super().__init__(id,name,price)
        self.add=add
    def getadd(self):
        return self.add
    def setadd(self,nadd):
        self.add=nadd
    def display(self):
        print(f'add={self.add}')
        super().display()

b1=Product(1,'join',250)
d1=Digital(2,'tv',12000,'link')
p1=PhyicPro(3,'laptop',100000,'abc')
b1.display()

d1.display()
p1.display()