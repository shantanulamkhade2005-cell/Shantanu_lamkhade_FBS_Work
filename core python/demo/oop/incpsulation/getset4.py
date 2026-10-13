class Ecommarce():
    def __init__(self,id,name,age,gender):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender

    def getID(self):
        return self.id  
    def setID(self,newId):
        self.id=newId

    def getName(self):
        return self.name    
    def setName(self,newName): 
        self.name=newName   

    def getAge(self):
        return self.age
    def setAge(self,newAge):
        self.age=newAge

    def getGender(self):
        return self.gender
    def setGender(self,newGender):
        self.gender=newGender

    def display(self):
        print(f"Id={self.id}\t Name={self.name}\t Age={self.age}\t Gender={self.gender}")
b1=Ecommarce(1,'join',25,'male')
b1.display()
b1.setAge(14)
b1.display()
print(b1.getName())