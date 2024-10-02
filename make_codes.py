from shutil import which
from tabnanny import check

import mysql.connector

db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='detective_game2',
         user='heikki',
         password='pekka',
         autocommit=True
         )

'''
def start_location():
    # Empties locations tabel. Selects 7 random location from airport tabel and adds them to locations table,
    # selects one of the airports as starting airport.
    sql1= (f"UPDATE locations SET name = (SELECT name FROM airport WHERE continent = 'EU' AND type = 'large_airport' ORDER BY RAND()LIMIT 1);")
    sql2= (f"UPDATE locations SET icao = (SELECT ident FROM airport WHERE locations.name = airport.name LIMIT 1);")
    sql3= (f"UPDATE game SET location = (SELECT name FROM locations ORDER BY RAND() limit 1);")
    cursor = db_connection.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    db_connection.commit()
    return




start_location()
'''




def location_now(game_id):
    sql = (f'SELECT location from game where id = "{game_id}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    current_location = cursor.fetchall()[0][0]
    return current_location






'''
def is_location_current(destination):
    sql = (f'SELECT icao, FROM locations;')
    sql2 = (f'SELECT icao, FROM game;')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.execute(sql2)
    your_airport = cursor.fetchall()
    if destination in airports and destination not in your_airport:
        return True
'''

def fly():

    def locations_available():
        sql = (
            f"SELECT icao, name FROM locations LEFT JOIN game ON locations.name = game.location WHERE game.location IS NULL;")
        cursor = db_connection.cursor()
        cursor.execute(sql)
        airports = cursor.fetchall()
        for airport in airports:
            print(f'{airport[1]}, Icao: {airport[0]}. ')
        return

    def location_check(destination):
        sql = (f'SELECT location FROM game ;')
        sql2 = (f'SELECT name FROM locations WHERE icao = "{destination}";')
        cursor = db_connection.cursor()
        cursor.execute(sql)
        location_game = cursor.fetchall()
        cursor.execute(sql2)
        locations = cursor.fetchall()
        if location_game != locations:
            return True
        elif location_game == locations:
            return False

    def flying_new_port(destination):
        sql = (f'UPDATE game SET location = (SELECT name FROM locations WHERE icao = "{destination}");')
        cursor = db_connection.cursor()
        cursor.execute(sql)
        db_connection.commit()
        return
        

    print(f'You are currently at the {location_now(1)}.')
    print(f'Available airports for you to fly are:')
    print(locations_available())
    destination = input("Where would you like to fly next, use the Icao-code: ")
    if location_check(destination) == True:
        flying_new_port(destination)
        print(f'Welcome to {location_now(1)}.')
    elif location_check(destination) == False:
        print("You cannot stay at the same airport. If you do party people will leave and case won't be solved.")
        fly()


while True:
    fly()




