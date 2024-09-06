#Exercises Lab Part - 06
#---------------------Exercise 01------------------------#
import random

def roll_dice():
    result = random.randint(1,6)
    return result

def main():

    result = 0
    while result != 6:
        result = roll_dice()
        print(f'Rolled: {result}')

main()

#---------------------Exercise 02------------------------#
def roll_dice(sides):
    result = random.randint(1,sides)
    return result

def main():

    sides = int(input('Enter the number of sides: '))
    result = 0
    while result != sides:
        result = roll_dice(sides)
        print(f'Rolled: {result}')

main()

#---------------------Exercise 03------------------------#
def gal_to_lit(gallons):
    liters = gallons * 3.785
    return liters

def main():
    while True:
        gallons = float(input('Enter the amount in gallons: '))
        if gallons < 0:
            print('You must enter a positive value')
            break
        liters = gal_to_lit(gallons)
        print(f'{gallons} gallons of liters is equal to: {liters:.2f} liters')

main()

#---------------------Exercise 04------------------------#
def sum_of_list(numbers):
    return sum(numbers)

def main():
    random_list = [1, 2, 3, 4, 5]

    total_sum = sum_of_list(random_list)

    print(f'The total sum of the list is: {total_sum}')

main()

#---------------------Exercise 05------------------------#
def remove_odds(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_num_list = remove_odds(test_list)

    print(f'The original list is: {test_list}')
    print(f'The cut down list is: {even_num_list}')

main()

#---------------------Exercise 06------------------------#
import math
def calculate_unit_price(diameter,  price):
    radius = diameter / 2
    area = math.pi * (radius ** 2) / 10000
    unit_price = price / area
    return unit_price

def main():
    diameter1 = float(input("Enter diameter of the first pizza in cm: "))
    price1 = float(input("Enter price of the first pizza in euro: "))
    diameter2 = float(input("Enter diameter of the second pizza in cm: "))
    price2 = float(input("Enter price of the second pizza in euro: "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f'Unit price of the first pizza is {unit_price1:.2f} euros per square meter')
    print(f'Unit price of the second pizza is {unit_price2:.2f} euros per square meter')

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money")
    else:
        print("Both pizza offer the same value for money")

main()









