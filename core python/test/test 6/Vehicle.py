from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, num_persons):
        self.num_persons = num_persons

    @abstractmethod
    def calculate_toll(self):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass


class TwoWheeler(Vehicle):

    def calculate_toll(self):
        basic_toll = 20
        if self.num_persons > 2:
            extra_persons = self.num_persons - 2
            extra_charge = extra_persons * 10
        else:
            extra_charge = 0
        return basic_toll + extra_charge

    def get_vehicle_type(self):
        return "Two Wheeler"


class ThreeWheeler(Vehicle):

    def calculate_toll(self):
        basic_toll = 30
        if self.num_persons > 3:
            extra_persons = self.num_persons - 3
            extra_charge = extra_persons * 20
        else:
            extra_charge = 0
        return basic_toll + extra_charge

    def get_vehicle_type(self):
        return "Three Wheeler"


class FourWheeler(Vehicle):

    def calculate_toll(self):
        basic_toll = 40
        if self.num_persons > 4:
            extra_persons = self.num_persons - 4
            extra_charge = extra_persons * 40
        else:
            extra_charge = 0
        return basic_toll + extra_charge

    def get_vehicle_type(self):
        return "Four Wheeler"


class HeavyVehicle(Vehicle):

    def calculate_toll(self):
        basic_toll = 60
        if self.num_persons > 6:
            extra_persons = self.num_persons - 6
            extra_charge = extra_persons * 100
        else:
            extra_charge = 0
        return basic_toll + extra_charge

    def get_vehicle_type(self):
        return "Heavy Vehicle"


def process_toll(vehicle: Vehicle):
    print("\n--- Toll Receipt ---")
    print(f"Vehicle Type     : {vehicle.get_vehicle_type()}")
    print(f"Total Persons    : {vehicle.num_persons}")
    print(f"Total Toll Amount: Rs. {vehicle.calculate_toll()}")
    print("--------------------\n")


def main():
    total_collection = 0

    while True:
        print("====== TOLL PLAZA SYSTEM ======")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle (>4 wheels)")
        print("5. Exit")

        choice = input("Select vehicle type (1-5): ").strip()

        if choice == "1":
            persons = int(input("Enter number of persons in Two Wheeler: "))
            vehicle = TwoWheeler(persons)
            process_toll(vehicle)
            total_collection += vehicle.calculate_toll()

        elif choice == "2":
            persons = int(input("Enter number of persons in Three Wheeler: "))
            vehicle = ThreeWheeler(persons)
            process_toll(vehicle)
            total_collection += vehicle.calculate_toll()

        elif choice == "3":
            persons = int(input("Enter number of persons in Four Wheeler: "))
            vehicle = FourWheeler(persons)
            process_toll(vehicle)
            total_collection += vehicle.calculate_toll()

        elif choice == "4":
            persons = int(input("Enter number of persons in Heavy Vehicle: "))
            vehicle = HeavyVehicle(persons)
            process_toll(vehicle)
            total_collection += vehicle.calculate_toll()

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
