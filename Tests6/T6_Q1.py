from abc import ABC, abstractmethod


# Abstract Base Class so objects of Vehicle cannot be instantiated directly
class Vehicle(ABC):

    def __init__(self, num_persons):
        self.num_persons = num_persons

    @abstractmethod
    def calculate_toll(self):
        pass


class TwoWheeler(Vehicle):

    def calculate_toll(self):
        basic_toll = 20
        extra_persons = max(0, self.num_persons - 2)
        return basic_toll + (extra_persons * 10)


class ThreeWheeler(Vehicle):

    def calculate_toll(self):
        basic_toll = 30
        extra_persons = max(0, self.num_persons - 3)
        return basic_toll + (extra_persons * 20)


class FourWheeler(Vehicle):

    def calculate_toll(self):
        basic_toll = 40
        extra_persons = max(0, self.num_persons - 4)
        return basic_toll + (extra_persons * 40)


class HeavyVehicle(Vehicle):

    def __init__(self, num_persons, wheels):
        super().__init__(num_persons)
        if wheels <= 4:
            raise ValueError("Heavy vehicles must have more than 4 wheels.")
        self.wheels = wheels

    def calculate_toll(self):
        basic_toll = 60
        extra_persons = max(0, self.num_persons - 6)
        return basic_toll + (extra_persons * 100)


# Function demonstrating polymorphic behavior
def process_toll(vehicle: Vehicle):
    total = vehicle.calculate_toll()
    print(
        f"\n---> Vehicle Type: {vehicle.__class__.__name__} | Passengers:"
        f" {vehicle.num_persons}"
    )
    print(f"---> Total Toll Payable: Rs. {total}\n")


def main():
    while True:
        print("=== Toll Plaza Calculation Menu ===")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle (More than 4 wheels)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Exiting toll system. Drive safely!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a valid option.\n")
            continue

        try:
            persons = int(input("Enter total number of persons in vehicle: "))
            if persons < 1:
                print("Number of persons must be at least 1.\n")
                continue

            vehicle = None

            if choice == "1":
                vehicle = TwoWheeler(persons)
            elif choice == "2":
                vehicle = ThreeWheeler(persons)
            elif choice == "3":
                vehicle = FourWheeler(persons)
            elif choice == "4":
                wheels = int(input("Enter number of wheels: "))
                vehicle = HeavyVehicle(persons, wheels)

            # Polymorphic method call
            process_toll(vehicle)

        except ValueError as e:
            print(f"Input Error: {e}\n")


if __name__ == "__main__":
    main()
