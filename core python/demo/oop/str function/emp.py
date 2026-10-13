class Employee():
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getId(self):
        return self.id
    def setId(self,nid):
        self.id=nid
    def getName(self):
        return self.name
    def setName(self,nname):
        self.name=nname
    def getsal(self):
        return self.sal
    def setsal(self,nsal):
        self.sal=nsal

    def __str__(self):
        return f'Id={self.id}\tename={self.name}\t esal={self.sal}'

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcom(self):
        return self.com
    def setcom(self,com):
        self.com=com
    def __str__(self):
        return super().__str__()+f"\t Com={self.com}"

class Dev(Employee):
    def __init__(self,id,name,sal,bonas):
        super().__init__(id,name,sal)
        self.bonas=bonas
    def getbonas(self):
        return self.bonas
    def setcom(self,bonas):
        self.bonas=bonas
    def __str__(self):
            return super().__str__()+f"\t bonas={self.bonas}"
e1=Employee(1,"Rahul",1232)
h1=Hr(2,"Harman",121,211)
print(e1)
print(h1)
