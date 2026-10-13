class Employee():
    def __init__(self, id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal

    def display(self):
        print(f"Id={self.id}\t Name:{self.name}\t SAl={self.sal}")
e1=Employee(10,"sachin",100000)
print(e1.getName())
e1.display()
e1.setSal(1032839)
e1.display()