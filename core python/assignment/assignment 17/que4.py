class College:
    def __init__(self, n):
        self.students = []
        self.n = n

    def AddStudent(self, student):
        if len(self.students) < self.n:
            self.students.append(student)
            print("Student added successfully")
        else:
            print("College is full")

    def GetStudent(self, sid):
        for student in self.students:
            if student.StudentId == sid:
                return student
        return "Student not found"

    def RemoveStudent(self, sid):
        for student in self.students:
            if student.StudentId == sid:
                self.students.remove(student)
                print("Student removed successfully")
                return
        print("Student not found")

    def __str__(self):
        if not self.students:
            return "No students in college"
        return "\n".join(str(student) for student in self.students)


class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def __str__(self):
        return f"ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}%"


c = College(3)

s1 = Student(101, "Rahul", 20, 85)
s2 = Student(102, "Amit", 21, 75)

c.AddStudent(s1)
c.AddStudent(s2)

print("\nCollege Students:")
print(c)

print("\nSearch Student:")
print(c.GetStudent(101))

c.RemoveStudent(102)

print("\nAfter Removing Student:")
print(c)