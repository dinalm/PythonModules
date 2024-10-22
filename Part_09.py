#Exercises Lab Part - 09
#--------------------------Exercise 01--------------------------------#

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def display_car_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

car = Car("ABC-123", 142)
car.display_car_info()

#--------------------------Exercise 02--------------------------------#

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

    def display_car_info(self):
        # Print out all the properties of the car
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("After accelerating:")
car.display_car_info()

car.accelerate(-200)
print("\nAfter emergency brake:")
car.display_car_info()

#--------------------------Exercise 03--------------------------------#

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

    def display_car_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

car = Car("ABC-123", 142)

car.accelerate(60)
car.drive(1.5)

print("After driving:")
car.display_car_info()

#--------------------------Exercise 04--------------------------------#
import random
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

cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
            break

table_data = []
for car in cars:
    table_data.append([car.registration_number, car.maximum_speed, car.current_speed, f"{car.travelled_distance:.1f} km"])

headers = ["Registration", "Max Speed (km/h)", "Current Speed (km/h)", "Travelled Distance"]
print(tabulate(table_data, headers, tablefmt="grid"))
