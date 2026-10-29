class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print(self)

    def CalculateRank(self):
        if self.Percentage >= 75:
            print("Rank: Distinction")
        elif self.Percentage >= 60:
            print("Rank: First Class")
        elif self.Percentage >= 50:
            print("Rank: Second Class")
        elif self.Percentage >= 35:
            print("Rank: Pass Class")
        else:
            print("Rank: Fail")

    def __str__(self):
        return (f"Student ID: {self.StudentId}\n"
                f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Percentage: {self.Percentage}%")


s1 = Student(0, "", 0, 0) 
s1.Accept() 
s1.Display() 
s1.CalculateRank()