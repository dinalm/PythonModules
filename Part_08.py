#Exercises Lab Part - 08
#---------------------Exercise 01------------------------#

from geopy.distance import geodesic
from tabulate import tabulate
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='256481@dinal',
    autocommit=True
    )

def get_airport_info(icao_code):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(sql_query, (icao_code,))
        result = cursor.fetchone()

        if result:
            name, municipality = result
            print(f'Airport name is: {name} and the location is: {municipality}')
        else:
            print("No Airport found")

    except mysql.connector.Error as err:
        print(err)

    finally:
        cursor.close()

try:
    icao_code = input('Enter ICAO code of the airport: ').upper()
    get_airport_info(icao_code)
finally:
    if connection and connection.is_connected():
        connection.close()

#---------------------Exercise 02------------------------#

def get_airports_by_country(area_code):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type ASC"
        cursor.execute(sql_query, (area_code,))
        result = cursor.fetchall()

        if result:
            print(f'Airports in the country with code {area_code}')
            headers = ["Airport Name", "Airport Type"]
            print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
        else:
            print('No airports found')

    except mysql.connector.Error as err:
        print(f'Error: {err}')

    finally:
        cursor.close()

try:
    area_code = input('Enter area code of the airport: ').upper()
    get_airports_by_country(area_code)
finally:
    if connection and connection.is_connected():
        connection.close()

#---------------------Exercise 03------------------------#

def get_airport_coordinates(icao_code):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
        cursor.execute(sql_query, (icao_code,))
        result = cursor.fetchone()

        if result:
            return result
        else:
            print(f'No data found for ICAO code {icao_code}')
            return None

    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None

    finally:
        if cursor is not None:
            cursor.close()

def main():
    try:
        icao_code1 = input('Enter ICAO code of the first airport: ').upper()
        icao_code2 = input('Enter ICAO code of the second airport: ').upper()

        coordinates1 = get_airport_coordinates(icao_code1)
        coordinates2 = get_airport_coordinates(icao_code2)

        if coordinates1 and coordinates2:
            distance = geodesic(coordinates1, coordinates2).kilometers
            print(f'The distance between {icao_code1} and {icao_code2} is {distance:.2f} kilometers')
        else:
            print('Unable to calculate distance')

    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    main()







