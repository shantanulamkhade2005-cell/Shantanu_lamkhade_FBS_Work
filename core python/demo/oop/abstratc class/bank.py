from abc import ABC,abstractmethod
class Bankaccount(ABC):
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
    @abstractmethod
    def ano(self):
        print(f'Account no={self.ac}')

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
    def ano(self):
        print(f'acconut no and rate={self.ac},{self.rate}')
    def __str__(self):
        return super().__str__()+f'\tAccount no={self.ac}\t Rate={self.rate}'

class Currentaccount(Bankaccount):
    def __init__(self,id,name,ac,ammount):
        super().__init__(id,name,ac)
        self.ammount=ammount
    def getamm(self):
        return self.ammount
    def setamm(self,nammount):
        self.ammount=nammount
    def ano(self):
        print(f'account no& ammount={self.ac},{self.ammount}')
    def __str__(self):
        return super().__str__()+f'\tAccount no={self.ac}\t Ammount={self.ammount}'

s1=Savingaccount(2,'HDFC',121,'15%')
c1=Currentaccount(3,'IDBI',121212,120000)
print(s1)
print(c1)