#Exercises Lab Part - 11
#--------------------------Exercise 01--------------------------------#

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")

if __name__ == "__main__":

    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    print("Magazine Information:")
    donald_duck.print_information()
    print("\nBook Information:")
    compartment_no_6.print_information()

#--------------------------Exercise 02--------------------------------#
from tabulate import tabulate

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed, current_speed, travelled_distance)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed, current_speed, travelled_distance)
        self.tank_volume = tank_volume

if __name__ == "__main__":

    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(120)
    gasoline_car.accelerate(150)

    electric_car.drive(3)
    gasoline_car.drive(3)

    table_data = [
        ["Electric Car", electric_car.registration_number, electric_car.maximum_speed, electric_car.current_speed,
         electric_car.battery_capacity, electric_car.travelled_distance],
        ["Gasoline Car", gasoline_car.registration_number, gasoline_car.maximum_speed, gasoline_car.current_speed,
         gasoline_car.tank_volume, gasoline_car.travelled_distance]
    ]

    headers = ["Car Type", "Registration", "Max Speed (km/h)", "Current Speed (km/h)",
               "Battery Capacity (kWh) / Tank Volume (l)", "Travelled Distance (km)"]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))













