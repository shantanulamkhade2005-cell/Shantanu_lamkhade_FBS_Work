class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        total_cm = (self.km * 100000 + self.m * 100 + self.cm) + (other.km * 100000 + other.m * 100 + other.cm)
        return Distance(total_cm // 100000, (total_cm % 100000) // 100, total_cm % 100)

    def __sub__(self, other):
        total_cm = (self.km * 100000 + self.m * 100 + self.cm) - (other.km * 100000 + other.m * 100 + other.cm)
        return Distance(total_cm // 100000, (total_cm % 100000) // 100, total_cm % 100)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    def __del__(self):
        print("Object destroyed")


d1 = Distance(2, 300, 50)
d2 = Distance(1, 200, 70)

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)
