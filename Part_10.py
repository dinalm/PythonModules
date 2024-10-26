#Exercises Lab Part - 10
#--------------------------Exercise 01--------------------------------#

# class Elevator:
#     def __init__(self, bottom, top):
#         self.bottom_floor = bottom
#         self.top_floor = top
#         self.current_floor = bottom
#
#     def floor_up(self):
#         if self.current_floor < self.top_floor:
#             self.current_floor += 1
#             print(f"Elevator is now at floor {self.current_floor}")
#         else:
#             print("Elevator is already at the top floor.")
#
#     def floor_down(self):
#         if self.current_floor > self.bottom_floor:
#             self.current_floor -= 1
#             print(f"Elevator is now at floor {self.current_floor}")
#         else:
#             print("Elevator is already at the bottom floor.")
#
#     def go_to_floor(self, target_floor):
#         if target_floor > self.top_floor or target_floor < self.bottom_floor:
#             print(f"Floor {target_floor} is out of range.")
#             return
#
#         while self.current_floor < target_floor:
#             self.floor_up()
#         while self.current_floor > target_floor:
#             self.floor_down()
#
# if __name__ == "__main__":
#
#     elevator = Elevator(0, 10)
#     elevator.go_to_floor(5)
#     elevator.go_to_floor(0)

#--------------------------Exercise 02--------------------------------#

# class Elevator:
#     def __init__(self, bottom, top):
#         self.bottom_floor = bottom
#         self.top_floor = top
#         self.current_floor = bottom
#
#     def floor_up(self):
#         if self.current_floor < self.top_floor:
#             self.current_floor += 1
#             print(f"Elevator is now at floor {self.current_floor}")
#         else:
#             print("Elevator is already at the top floor.")
#
#     def floor_down(self):
#         if self.current_floor > self.bottom_floor:
#             self.current_floor -= 1
#             print(f"Elevator is now at floor {self.current_floor}")
#         else:
#             print("Elevator is already at the bottom floor.")
#
#     def go_to_floor(self, target_floor):
#         if target_floor > self.top_floor or target_floor < self.bottom_floor:
#             print(f"Floor {target_floor} is out of range. The elevator can only go between floor {self.bottom_floor} and {self.top_floor}.")
#             return
#
#         while self.current_floor < target_floor:
#             self.floor_up()
#         while self.current_floor > target_floor:
#             self.floor_down()
#
# class Building:
#     def __init__(self, bottom, top, number_of_elevators):
#         self.elevators = [Elevator(bottom, top) for _ in range(number_of_elevators)]
#         self.bottom_floor = bottom
#         self.top_floor = top
#         self.number_of_elevators = number_of_elevators
#
#     def run_elevator(self, elevator_number, target_floor):
#         elevator_index = elevator_number - 1
#         if elevator_index >= self.number_of_elevators or elevator_index < 0:
#             print("Invalid elevator number.")
#         else:
#             print(f"Running elevator {elevator_number} to floor {target_floor}.")
#             self.elevators[elevator_index].go_to_floor(target_floor)
#
# if __name__ == "__main__":
#
#     building = Building(0, 10, 3)
#     building.run_elevator(1, 5)
#     building.run_elevator(2, 7)
#     building.run_elevator(3, 8)

#--------------------------Exercise 03--------------------------------#

# class Elevator:
#     def __init__(self, bottom, top):
#         self.bottom_floor = bottom
#         self.top_floor = top
#         self.current_floor = bottom
#
#     def floor_up(self):
#         if self.current_floor < self.top_floor:
#             self.current_floor += 1
#             print(f"Elevator is now at floor {self.current_floor}")
#         else:
#             print("Elevator is already at the top floor.")
#
#     def floor_down(self):
#         if self.current_floor > self.bottom_floor:
#             self.current_floor -= 1
#             print(f"Elevator is now at floor {self.current_floor}")
#         else:
#             print("Elevator is already at the bottom floor.")
#
#     def go_to_floor(self, target_floor):
#         if target_floor > self.top_floor or target_floor < self.bottom_floor:
#             print(f"Floor {target_floor} is out of range. The elevator can only go between floor {self.bottom_floor} and {self.top_floor}.")
#             return
#
#         while self.current_floor < target_floor:
#             self.floor_up()
#         while self.current_floor > target_floor:
#             self.floor_down()
#
# class Building:
#     def __init__(self, bottom, top, number_of_elevators):
#         self.elevators = [Elevator(bottom, top) for _ in range(number_of_elevators)]
#         self.bottom_floor = bottom
#         self.top_floor = top
#         self.number_of_elevators = number_of_elevators
#
#     def run_elevator(self, elevator_number, target_floor):
#         elevator_index = elevator_number - 1
#         if elevator_index >= self.number_of_elevators or elevator_index < 0:
#             print("Invalid elevator number.")
#         else:
#             print(f"Running elevator {elevator_number} to floor {target_floor}.")
#             self.elevators[elevator_index].go_to_floor(target_floor)
#
#     def fire_alarm(self):
#         print("Fire alarm activated! Moving all elevators to the bottom floor.")
#         for i, elevator in enumerate(self.elevators):
#             print(f"Moving elevator {i + 1} to the bottom floor.")
#             elevator.go_to_floor(self.bottom_floor)
#
# if __name__ == "__main__":
#
#     building = Building(0, 10, 3)
#     building.run_elevator(1, 5)
#     building.run_elevator(2, 7)
#     building.run_elevator(3, 8)
#     building.fire_alarm()

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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        table_data = [
            [
                car.registration_number,
                car.maximum_speed,
                car.current_speed,
                f"{car.travelled_distance:.1f} km"
            ] for car in self.cars
        ]
        headers = ["Registration", "Max Speed (km/h)", "Current Speed (km/h)", "Travelled Distance"]
        print(tabulate(table_data, headers, tablefmt="grid"))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

if __name__ == "__main__":

    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()  # Simulate one hour passing
        hours_passed += 1

        # Print status every 10 hours
        if hours_passed % 10 == 0:
            print(f"\n--- Status at {hours_passed} hours ---")
            race.print_status()

    # Print the final status at the end of the race
    print("\n--- Final Status ---")
    race.print_status()
