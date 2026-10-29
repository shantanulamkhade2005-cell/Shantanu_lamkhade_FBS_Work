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
        return f"Student ID: {self.StudentId}\nName: {self.Name}\nAge: {self.Age}\nPercentage: {self.Percentage}%"


class MedicalStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Specialization, MarksOfInternship):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Internship Marks: "))

    def Display(self):
        print(self)

    def CalculateRank(self):
        total = self.Percentage + self.MarksOfInternship

        if total >= 150:
            print("Rank: Distinction")
        elif total >= 120:
            print("Rank: First Class")
        elif total >= 100:
            print("Rank: Second Class")
        else:
            print("Rank: Pass Class")

    def __str__(self):
        return super().__str__() + f"\nSpecialization: {self.Specialization}\nInternship Marks: {self.MarksOfInternship}"


m1 = MedicalStudent(101, "Rahul", 22, 80, "Cardiology", 18)
m1.Display()
m1.CalculateRank()
