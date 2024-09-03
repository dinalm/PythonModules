#Exercises Lab Part - 05
import random

#----------------------Exercise 01--------------------------#
num_of_dice = int(input('How many dice do you want to roll: '))
total_sum = 0
for _ in range(num_of_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print('The total sum of the dice rolls is', total_sum)

#----------------------Exercise 02--------------------------#
import itertools
numbers = []
for _ in itertools.count():
    user_input = input('Enter a number: ')
    if user_input == "":
        break
    numbers.append(int(user_input))

numbers.sort(reverse=True)
top_five = numbers[:5]

print('The top five greatest numbers are: ', top_five)

#----------------------Exercise 03--------------------------#
number = int(input("Enter an integer: "))

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if number > 1 and is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#----------------------Exercise 04--------------------------#
cities = []

for i in range(5):
    city = input(f'Enter the name of the city {i+1}: ')
    cities.append(city)

print("\nThe names of the cities you entered are:")
for city in cities:
    print(city)







