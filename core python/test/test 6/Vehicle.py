from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, persons):
        self.persons = persons

    @abstractmethod
    def calculate_toll(self):
        pass


class TwoWheeler(Vehicle):

    def calculate_toll(self):
        total = 20
        if self.persons > 2:
            total = total + (self.persons - 2) * 10
        return total


class ThreeWheeler(Vehicle):

    def calculate_toll(self):
        total = 30
        if self.persons > 3:
            total = total + (self.persons - 3) * 20
        return total


class FourWheeler(Vehicle):

    def calculate_toll(self):
        total = 40
        if self.persons > 4:
            total = total + (self.persons - 4) * 40
        return total


class HeavyVehicle(Vehicle):

    def calculate_toll(self):
        total = 60
        if self.persons > 6:
            total = total + (self.persons - 6) * 100
        return total


def main():
    while True:
        print("\n----- TOLL TAX SYSTEM -----")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle (> 4 wheels)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank You! Exiting program.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid Choice! Please enter a number between 1 and 5.")
            continue

        persons = int(input("Enter number of persons: "))
        if persons <= 0:
            print("Invalid number of persons.")
            continue

        if choice == "1":
            obj = TwoWheeler(persons)
        elif choice == "2":
            obj = ThreeWheeler(persons)
        elif choice == "3":
            obj = FourWheeler(persons)
        elif choice == "4":
            obj = HeavyVehicle(persons)

        amount = obj.calculate_toll()
        print("Total Toll Amount = Rs.", amount)


if __name__ == "__main__":
    main()
