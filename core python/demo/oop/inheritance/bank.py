class Bankaccount():
    def __init__(self,id,name,ac):
        self.name=name
        self.id=id
        self.ac=ac
    def getID(self):
        return self.id
    def setID(self,newId):
        self.id=newId

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
 
    def getac(self):
        return self.ac
    def setac(self,newac):
        self.ac=newac


    def __str__(self):
        return f"Id={self.id}\t Name={self.name}\t ac={self.ac}"


class Savingaccount(Bankaccount):
    def __init__(self,id,name,ac,rate):
        super().__init__(id,name,ac)
        self.rate=rate
    def getrate(self):
        return self.rate
    def setrate(self,nrate):
        self.rate=nrate
    def display(self):
        print(f'Rate={self.rate}')
        super().display()

class Currentaccount(Bankaccount):
    def __init__(self,id,name,ac,ammount):
        super().__init__(id,name,ac)
        self.ammount=ammount
    def getamm(self):
        return self.ammount
    def setamm(self,nammount):
        self.ammount=nammount
    def display(self):
        print(f'Ammount={self.ammount}')
        super().display()
b1=Bankaccount(1,'IOB',1212)
s1=Savingaccount(2,'HDFC',121,'15%')
c1=Currentaccount(3,'IDBI',121212,120000)
print(b1)
