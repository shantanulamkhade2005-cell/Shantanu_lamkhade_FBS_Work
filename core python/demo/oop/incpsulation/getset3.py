class Bank():
    def __init__(self,id,name,add):
        self.name=name
        self.id=id
        self.add=add
    def getID(self):
        return self.id
    def setID(self,newId):
        self.id=newId

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
 
    def getadd(self):
        return self.add
    def setadd(self,newadd):
        self.add=newadd

    def display(self):
        print(f"Id={self.id}\t Name={self.name}\t add={self.add}")
b1=Bank(1,'IOB','bota')
b1.display()
print(b1.getName())
b1.setadd('alephata')
b1.display()
