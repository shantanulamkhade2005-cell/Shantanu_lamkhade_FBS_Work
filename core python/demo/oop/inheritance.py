class Student:
    stCount = 0
    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.batch = bname
        Student.stCount += 1
        
    def display(self):
        print(f"FRN={self.frn} \tName={self.name} \t Batch={self.batch} \tStudent Count={Student.stCount}")


class placedStudent(Student):
    def __init__(self,frn,name,bname,cname):
        super().__init__(frn,name,bname)
        self.cname=cname
    def setcname(self,cname):
        self.cname=cname
    def getcname(self):
        return self.cname
    def display(self):
        super().display()
        print(f'cname={self.cname}')
        


s1 = Student(12, "Gaurav", "April")
s2 = Student(1, "Atharva", "Jul/aug")
s3 = Student(53, "Rutika", "Jul/aug")

s4 = placedStudent(37, "Shivaraj", "Jul/aug", "TCS")
s5 = placedStudent(18, "Viart", "Jul/aug", "One8")

print(Student.stCount)
s4.display()