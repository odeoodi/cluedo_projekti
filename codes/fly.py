import mysql.connector
from location_now import location_now
from check_money import check_money
from press_enter import press_enter_to_continue

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

def fly():
# Druing this function player can fly to the new location.

    def locations_available():
        # This print all the airports and their ICAO-codes where player can fly.
        # Execludin the location where player is currently
        availabled = (f"SELECT icao, name FROM locations LEFT JOIN game ON locations.name = game.location WHERE game.location IS NULL ;")
        cursor = db_connection.cursor()
        cursor.execute(availabled)
        airports = cursor.fetchall()
        for airport in airports:
            print(f'ICAO: {airport[0]}, {airport[1]}. ')

    def icao_in_locations(destination):
        # Checks if the icao code is writen correctly.
        check = (f'SELECT name FROM locations; ')
        getname = (f'SELECT name FROM locations WHERE icao = "{destination}";')
        cursor = db_connection.cursor()
        cursor.execute(check)
        locations_check = cursor.fetchall()
        cursor.execute(getname)
        locations_icao_name = cursor.fetchall()
        if not locations_icao_name:
            return False
        elif locations_icao_name[0] in locations_check:
            return True


    def location_check(destination):
        # Checks if the destination where player wants to go is current location or not.
        # Returns True or False.
        getlocation = (f'SELECT location FROM game ;')
        getname = (f'SELECT name FROM locations WHERE icao = "{destination}";')
        cursor = db_connection.cursor()
        cursor.execute(getlocation)
        location_game = cursor.fetchall()
        cursor.execute(getname)
        locations_icao = cursor.fetchall()
        if location_game != locations_icao:
            return True
        else:
            return False

    def flying_new_port(destination):
        # Uppdates a new location to the database where player has flown.
        flying = (f'UPDATE game SET location = (SELECT name FROM locations WHERE icao = "{destination}");')
        cursor = db_connection.cursor()
        cursor.execute(flying)
        db_connection.commit()
        return

    def cost_of_flying():
        # Subtracts flying cost from the money player has.
        # Change (SELECT money -'125'....) to change cost.
        moneycost=(f'UPDATE game SET money =( SELECT money -125 FROM game ) ')
        cursor = db_connection.cursor()
        cursor.execute(moneycost)
        db_connection.commit()
        return


    while True:
        print(f'\nYou are currently at the {location_now(1)}.')
        press_enter_to_continue()
        print()
        print(f'Available airports for you to fly are:')
        locations_available()
        destination = input("\nWhere would you like to fly next, use the ICAO-code: ")
        destination = destination.upper()
        if icao_in_locations(destination) == True:
            if location_check(destination) == True:
                flying_new_port(destination)
                cost_of_flying()
                print(f'\nWelcome to {location_now(1)} you have {check_money(1)} euros.')
                press_enter_to_continue()
                print()
                break
            elif location_check(destination) == False:
                print("\nYou cannot stay at the same airport. If you do party people will leave and case won't be solved.")
                press_enter_to_continue()
                print()
        else :
            print("\nSorry your ICAO-code was not in the list, please try again.")
            press_enter_to_continue()
            print()
