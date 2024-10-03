from tabnanny import check

import mysql.connector
import random


def start_location():
    # Empties locations tabel. Selects 5 random location from airport tabel and adds them to locations table,
    # selects one of the airports as starting airport.
    sql1 = (f"UPDATE locations SET name = (SELECT name FROM airport WHERE continent = 'EU' AND type = 'large_airport' ORDER BY RAND()LIMIT 1);")
    sql2 = (f"UPDATE locations SET icao = (SELECT ident FROM airport WHERE locations.name = airport.name LIMIT 1);")
    sql3 = (f"UPDATE game SET location = (SELECT name FROM locations ORDER BY RAND() limit 1);")
    cursor = db_connection.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    db_connection.commit()
    return

def start_accusations():
    sql1 = f"update accusations set weapon_accusations = NULL, suspect_accusations = NULL, location_accusations = NULL"
    #sql2 = f"alter table accusations auto_increment = 1"
    cursor = db_connection.cursor()
    cursor.execute(sql1)
    hints = cursor.fetchall()
    return hints

def start_money(game_id):
    sql = (f'UPDATE game SET money = 500 WHERE id = "{game_id}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    current_location = cursor.fetchall()
    return


def check_money(saved_game):
    sql = f'select money from game where id = "{saved_game}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    money = cursor.fetchone()
    money_now = int(money[0])
    return money_now


def location_now(game_id):
    sql = (f'SELECT location from game where id = "{game_id}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    current_location = cursor.fetchall()[0][0]
    return current_location


def accuse_weapon_suspect(game_id, the_accusation):
    # --- adds the accused weapon to accusations table
    print("Weapons to choose from: spoon, knife, poison, pencil, pistol")
    weapon_accusation = input("Make your weapon accusation: ")
    print("Suspects to choose from: Make, Iida, Ode, Angelina, Ville")
    suspect_accusation = input("Who do you suspect: ")
    airport_accusation = location_now(game_id)
    sql = f'update accusations set weapon_accusations = "{weapon_accusation}",location_accusations = "{airport_accusation}",suspect_accusations = "{suspect_accusation}" WHERE id = {the_accusation}'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    #fff = cursor.fetchone()
    #check_accusations(game_id)
    return

def check_accusations(game_id):
    sql = (f'select weapon_accusations,location_accusations,suspect_accusations from accusations where weapon_accusations is not NULL')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    made_accusations = cursor.fetchall()
    for acc in made_accusations:
        print(f"| {acc[0]} | ", end="")
        print(f"{acc[1]} | ", end="")
        print(f"{acc[2]} |", end="")
        print("")
    print("")
    return made_accusations



def fly():
# Druing this funktion player can fly to the new location.

    def locations_available():
        # This print all the airports and their ICAO-codes where player can fly.
        # Execludin the location where player is currently
        availabled = (f"SELECT icao, name FROM locations LEFT JOIN game ON locations.name = game.location WHERE game.location IS NULL ;")
        cursor = db_connection.cursor()
        cursor.execute(availabled)
        airports = cursor.fetchall()
        for airport in airports:
            print(f'Icao: {airport[0]}, {airport[1]}. ')

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
        print(f'You are currently at the {location_now(1)}.')
        print(f'Available airports for you to fly are:')
        locations_available()
        destination = input("Where would you like to fly next, use the Icao-code: ")
        destination = destination.upper()
        if icao_in_locations(destination) == True:
            if location_check(destination) == True:
                flying_new_port(destination)
                cost_of_flying()
                print(f'Welcome to {location_now(1)} you have {check_money(1)} euros.')

                break
            elif location_check(destination) == False:
                print("You cannot stay at the same airport. If you do party people will leave and case won't be solved.")
        else :
            print("Sorry your Icao-code was not in the list, please try again.")



'''
angelinan koodi check if correct

def win():
    if check_if_correct has all three correct -> 
    victory = True
    return victory
'''

"""
pseudo code for one round:

intro() 


while money > 0 or not right_answers in accusations:
    print(check_money())

    round = input("What would you like to do: ")
    print('See the options by typing "help"')

    if round == "help":
        print(help())
    elif round == "accuse":
        weapon_accusation = input("Make your weapon accusations: ")
        suspect_accusation = input("Make your suspect accusations: ")
        location_accusation = location_now()
        print(check_if_correct())
    elif round == "fly":
        destination = input("Where would you like to travel: ")
        fly()
    elif round == "check accusations":
        print(accusations)
    elif round == "end game":
        end_game()

if money <= 0:
    print("you lost the game")
else:
    print("you won")
"""

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)
# intro()

victory = False
select_game = 1
# accusation_counter = 0
start_location()
start_money(select_game)
#print(location_now(select_game))
start_accusations()
print('See the options by typing "help".\n')
print(f"You have {check_money(select_game)}€ left.\n")
accusation_counter = 0

while check_money(select_game) > 0 and not victory:
    # saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    game_round = input("What would you like to do: ")
    command_counter = 0

    while command_counter == 0:
        if game_round.lower() == "accuse":
            accusation_counter += 1
            print(accusation_counter)
            command_counter += 1
            accuse_weapon_suspect(select_game,accusation_counter)
            # print(check_if_correct())
            # game_round = input("What would you like to do: ")
        elif game_round.lower() == "fly":
            fly()
            command_counter = 0
            game_round = input("What would you like to do: ")
        elif game_round.lower() == "check accusations":
            check_accusations(select_game)
            game_round = input("What would you like to do: ")
        elif game_round == "help":
            print("hello")  # this is only here to keep the game intact until we have a working help function
            game_round = input("What would you like to do: ")
            # print(help_ville())
        else:
            print("Check spelling on your command.")
            game_round = input("What would you like to do: ")
    if command_counter == 1:
        print("Here are your current accusations.")
        check_accusations(select_game)
        print("")
        fly()
        command_counter = 0

# These can be changed to work better with the outro.
if check_money(select_game) <= 0:
    print("You ran out of money.")
elif victory:
    print("You solved the mystery!")


