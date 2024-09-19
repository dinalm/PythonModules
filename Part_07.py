#Exercises Lab Part - 07
#---------------------Exercise 01------------------------#

seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of the month (1-12): "))

if month in (12,1,2):
    print(seasons[0])
elif month in (3,4,5):
    print(seasons[1])
elif month in (6,7,8):
    print(seasons[2])
elif month in (9,10,11):
    print(seasons[3])
else:
    print("Invalid input")

#---------------------Exercise 02------------------------#

names = set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break

    if name in names:
        print("Existing Name")
    else:
        print("New Name")
        names.add(name)

print("\nList of names you entered: ")
for name in names:
    print(name)

#---------------------Exercise 03------------------------#

airports = {"DAAG":"Alger", "DAAT":"Tamanrasset", "EBBR":"Brussels", "FMCH":"Moroni"}
while True:
    print("1. Enter a New airport \n2. Fetch airport information \n3. Quit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter the Airport name: ")
        airports[icao] = name
        print(f'Airport {name} with ICAO code {icao} has been added to airports.')

    elif choice == "2":
        icao = input("Enter ICAO code to fetch data: ").upper()
        if icao in airports:
            print(f'Airport: {airports[icao]}')
        else:
            print('Airport not found.')

    elif choice == "3":
        print("Have a nice day!")
        break

    else:
        print("Please enter a valid option.")


