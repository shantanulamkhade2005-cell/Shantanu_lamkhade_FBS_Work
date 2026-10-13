class Student():
    iname="FBS"
    @staticmethod
    def setInName(niname):
        Student.iname=niname
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname
    def display(self):
        print(f"frn={self.frn}\t name={self.name}\tbname={self.bname}\t Inname={Student.iname}")
s1=Student(1,'a',12)
s1.display()