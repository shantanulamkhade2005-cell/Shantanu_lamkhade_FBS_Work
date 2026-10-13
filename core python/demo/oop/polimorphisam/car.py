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

    def carname(self):
        print(f'car name={self.name}')
class Sportcar(Car):
    def __init__(self,id,name,price,chassisno,power):
        super().__init__(id,name,price,chassisno)
        self.power=power
    def getpower(self):
        return self.power
    def setpower(self,newpower):
        self.power=newpower
    def carname(self):
        print(f'car name & power={self.name}{self.power}')
            

class Electriccar(Car):
    def __init__(self,id,name,price,chassicno,battery):
        super().__init__(id,name,price,chassicno)
        self.battery=battery
    def getbatt(self):
        return self.battery
    def setbatt(self,nbatt):
        self.battery=nbatt
    def carname(self):
            print(f'car name={self.name}')

    def carname(self):
        print(f'car name&Battery={self.name} {self.battery}')

e1=Car(10,"Toyota",200000,"CH123456")
s1=Sportcar(1,"BMW",21200000,"CH1234ww5",'145hp')
el1=Electriccar(4,"Tesla",2200000,"m12",'800kh')
e1.carname()
s1.carname()
el1.carname()