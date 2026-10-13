class person():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def getid(self):
        return self.id
    def setid(self,nid):
        self.id=nid

    def getname(self):
        return self.name
    def setname(self,nname):
        self.name=nname

    def __str__(self):
        return f'Id={self.id}\t Name={self.name}'

class Emp(person):
    def __init__(self,id,name,sal):
        super().__init__(id,name)
        self.sal=sal
    def getsal(self):
        return self.sal 
    def setsal(self,nsal):
        self.sal=nsal
    def __str__(self):
        return super().__str__()+f"\tsal={self.sal}"

class Patient(person):
    def __init__(self,id,name,dis):
        super().__init__(id,name)
        self.dis=dis
    def getdis(self):
        return self.dis
    def setdis(self,ndis):
        self.dis=ndis

    def __str__(self):
        return super().__str__()+f"\t dis={self.dis}"
p1=person(1,'abc')
e1=Emp(2,'xyz',12000)
pa1=Patient(3,'qwwq','cancer')
print(p1)
print(e1)
print(pa1)
   