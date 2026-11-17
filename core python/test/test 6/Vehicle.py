
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def toll(self, persons):
        pass
class TwoWheeler(Vehicle):
    def toll(self, persons):
        total = 20
        if persons > 2:
            total = total + (persons - 2) * 10
        return total

class ThreeWheeler(Vehicle):
    def toll(self, persons):
        total = 30

        if persons > 3:
            total = total + (persons - 3) * 20
        return total

class FourWheeler(Vehicle):
    def toll(self, persons):
        total = 40
        if persons > 4:
            total = total + (persons - 4) * 40
        return total

class HeavyVehicle(Vehicle):
    def toll(self, persons):
        total = 60
        if persons > 6:
            total = total + (persons - 6) * 100
        return total

while True:
    print("\n----- TOLL TAX SYSTEM -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Thank You!")
        break
    elif choice == 1:
        obj = TwoWheeler()
    elif choice == 2:
        obj = ThreeWheeler()
    elif choice == 3:
        obj = FourWheeler()
    elif choice == 4:
        obj = HeavyVehicle()
    else:
        print("Invalid Choice")
        continue
    persons = int(input("Enter number of persons: "))
    if persons <= 0:
        print("Invalid number of persons")
        continue
    amount = obj.toll(persons)
    print("Total Toll Amount = Rs.", amount)
