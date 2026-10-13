class Collagem():
    def __init__(self,id,name,add):
        self.name=name
        self.id=id
        self.add=add
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getadd(self):
        return self.add
    def setadd(self,newadd):
        self.add=newadd

    def display(self):
        print(f"id={self.id}\t Name={self.name}\t add={self.add}")

class Student(Collagem):
    def __init__(self,id,name,add,marks):
        super().__init__(id,name,add)
        self.marks=marks
    def getmarks(self):
        return self.marks
    def setmarks(self,nmarks):
        self.marks=nmarks
    def display(self):
        super().display()
        print(f'Marks={self.marks}')
#student class end here

class Teacher(Collagem):
    def __init__(self,id,name,add,sal):
        super().__init__(id,name,add)
        self.sal=sal
    def getsal(self):
        return self.sal
    def setsal(self,nsal):
        self.sal=nsal
    def display(self):
        super().display()
        print(f'salary={self.sal}')
c1=Collagem(1,'shantanu','bota')
s1=Student(2,'siddesh','kholapur',200)
t1=Teacher(3,'prdeep','xyz',50000)
c1.display()
s1.display()
t1.display()