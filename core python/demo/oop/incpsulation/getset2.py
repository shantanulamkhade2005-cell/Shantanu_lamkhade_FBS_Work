class Car():
    def __init__(self, id,name,Price,ChassisNo):
        self.id=id
        self.name=name
        self.Price=Price
        self.ChassisNo=ChassisNo
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getPrice(self):
        return self.Price
    def setPrice(self,newprice):
        self.Price=newprice

    def getChassisNo(self):
        return self.ChassisNo
    def setChassisNo(self,newchassisno):
        self.ChassisNo=newchassisno

    def display(self):
        print(f"Id={self.id}\t Name:{self.name}\t Price={self.Price}\t ChassisNo={self.ChassisNo}")
e1=Car(10,"Toyota",200000,"CH123456")
print(e1.getName())
e1.display()
e1.setName('BMW')
e1.setPrice(250000)
e1.display()