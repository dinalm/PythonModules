#Exercise Lab Part - 02
import math
import random

#Exercise 01
name = input('what is your name: ')
print(f"Hello, {name}!")

#Exercise 02
radius = float(input('what is the radius of the circle? '))
print(f"Area of the circle is: {math.pi*radius**2:.2f}")

#exercise 3
rec_length = float(input('what is the length of the rectangle? '))
rec_width = float(input('what is the width of the rectangle? '))
peri_rec = 2*rec_length + 2*rec_width
area_rec = rec_length*rec_width
print(f"The perimeter of the rectangle is: {peri_rec:.1f}")
print(f"The area of the rectangle is: {area_rec:.1f}")

#exercise 4
print("Give three integer numbers")
num1 = int(input('First number: '))
num2 = int(input('second number: '))
num3 = int(input('third number: '))
print(f"Sum of three number is {num1+num2+num3}, Product of three numbers is {num1*num2*num3}, Average of three numbers is {(num1+num2+num3)/3}")

#exercise 5
print("Enter talents: ")
talents = float(input())
print("Enter pounds: ")
pounds = float(input())
print("Enter lots: ")
lots = float(input())
kg_weight = ((talents*20+pounds)*32 + lots)*0.0133
gr_weight = 1000.0*(kg_weight - int(kg_weight))
print(f"The weight in modern units: \n{int(kg_weight)} kilograms and {gr_weight:.2f} grams")

#exercise 6
#Method 01
print(f"First combination of lock number: {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}")
print(f"Second combination of lock number: {random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}")

#Method 02
print(f"First combination of lock number: {random.sample(range(1, 9), 3)}")
print(f"Second combination of lock number: {random.sample(range(1, 6), 4)}")










