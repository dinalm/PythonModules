#Exercises Lab Part - 04
import random
import math
#--------------------------Exercise 01--------------------------------#
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i = i + 1
#--------------------------Exercise 02--------------------------------#
while True:
    num = float(input('Enter a value in inches: '))
    if num < 0:
        break
    centimeters = num * 2.54
    print(f'{num} inches is equal to {centimeters} centimeters')

#--------------------------Exercise 03--------------------------------#
smallest = None
largest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break

    num = float(user_input)

    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

if smallest is not None and largest is not None:
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")

#--------------------------Exercise 04--------------------------------#
random_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > random_number:
        print("Too high!")
    elif guess < random_number:
        print("Too low!")
    else:
        print("Correct!")
        break

#--------------------------Exercise 05--------------------------------#
correct_username = "python"
correct_password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")
    if username == correct_username and password == correct_password:
        print("welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect username or password. Attempts left: {max_attempts - attempts}")
    if attempts == max_attempts:
        print('Access denied')

#--------------------------Exercise 06--------------------------------#
N = int(input("Enter the number of random points to generate: "))
n = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    i += 1

pi_approx = 4 * n / N

print(f'Approximation of pi is: {pi_approx}, the difference with math pi is: {math.pi - pi_approx}' )



