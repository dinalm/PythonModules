#Exercises Lab Part - 03
#-------------------------------Exercise 01--------------------------------#
length = float(input('What is the length of the zander in centimeters: '))

if length < 42:
    print(f'The zander is {42-length:.2f} cm below the size limit. Please release it back into the lake')

else:
    print("The zander meets the size limit. You can keep the fish")

#------------------------------Exercise 02--------------------------------#
cabin_class = input('Enter the cabin class: ').upper()

if cabin_class == 'LUX':
    print('Upper-deck cabin with a balcony')
elif cabin_class == 'A':
    print('Above the car deck, equipped with a window')
elif cabin_class == 'B':
    print('Windowless cabin above the car deck')
elif cabin_class == 'C':
    print('Windowless cabin below the car deck')
else:
    print('Invalid cabin class')

#-----------------------------Exercise 03------------------------------#
gender = input('Enter your biological gender: ').lower()
hemoglobin_value = float(input('Enter your hemoglobin value: '))

if gender == 'female':
    if hemoglobin_value < 117:
        print('Your hemoglobin value is low')
    elif 117 <= hemoglobin_value <= 155:
        print('Your hemoglobin value is normal')
    else:
        print('Your hemoglobin value is high')
elif gender == 'male':
    if hemoglobin_value < 134:
        print('Your hemoglobin value is low')
    elif 134 <= hemoglobin_value <= 167:
        print('Your hemoglobin value is normal')
    else:
        print('Your hemoglobin value is high')
else:
    print('Invalid input')

#----------------------------Exercise 04------------------------------#
year = int(input('Enter a year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')