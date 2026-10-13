class Student():
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getfrn(self):
            return self.frn
    def setfrn(self,newfrn):
        self.frn=newfrn

    def getiname(self):
        return self.iname
    def setiname(self,newiname):
        self.iname=newiname

    def getbname(self):
        return self.bname
    def setbname(self,newbname):
        self.frn=newbname

    def display(self):
        print(f"frn={self.frn}\t Name={self.name}\t iname={self.iname}\t bname={self.bname}")
s1=Student(56,'shantanu','17 April','FBS')
s2=Student(61,'siddhesh','jul/aug','FBS')
s1.display()
print(s2.getName())
s2.display()
s1.setfrn(57)
s1.display()
