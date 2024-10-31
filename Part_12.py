#Exercises Lab Part - 12
#--------------------------Exercise 01--------------------------------#
import requests

def get_chuck_norris_joke():
    try:
        request = "https://api.chucknorris.io/jokes/random"
        response = requests.get(request)

        response.raise_for_status()

        joke_data = response.json()
        print(joke_data["value"])

    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    get_chuck_norris_joke()

#--------------------------Exercise 02--------------------------------#

def get_weather():
    api_key = "89563***********15ed80b################"
    city = input("Enter the name of a municipality: ")

    request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(request)
        response.raise_for_status()

        weather_data = response.json()
        description = weather_data["weather"][0]["description"]
        temp_kelvin = weather_data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15

        print(f"Weather in {city.capitalize()}:")
        print(f"Condition: {description.capitalize()}")
        print(f"Temperature: {temp_celsius:.2f} °C")

    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    get_weather()
