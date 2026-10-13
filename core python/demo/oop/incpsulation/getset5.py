class Collage():
    def __init__(self,rollno,name,add):
        self.name=name
        self.rollno=rollno
        self.add=add
    def getRollno(self):
        return self.rollno
    def setRollno(self,newRollno):
        self.rollno=newRollno

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getadd(self):
        return self.add
    def setadd(self,newadd):
        self.add=newadd

    def display(self):
        print(f"Rollno={self.rollno}\t Name={self.name}\t add={self.add}")
c1=Collage(1,'shantanu','bota')
c1.display()
print(c1.getName())
c1.setName('siddhesh')
c1.setadd('kholapur')
c1.setRollno(2)
c1.display()