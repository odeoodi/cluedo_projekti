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
    sql1 = f"delete from accusations"
    #sql2 = (f"")
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


def random_location(locations):
    sql = f"SELECT name FROM locations ORDER BY RAND() LIMIT 1";
    kursori=db_connection.cursor()
    kursori.execute(sql)
    result=kursori.fetchone()
    return result

def random_weapon(weapons):
    sql = f"SELECT weapon FROM weapons ORDER BY RAND() LIMIT 1";
    kursori=db_connection.cursor()
    kursori.execute(sql)
    result=kursori.fetchone()
    return result

def random_suspect(suspects):
    sql = f"SELECT names FROM suspects ORDER BY RAND() LIMIT 1";
    kursori=db_connection.cursor()
    kursori.execute(sql)
    result=kursori.fetchone()
    return result


def check_money(saved_game):
    sql = f'select money from game where id = "{saved_game}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    money = cursor.fetchone()
    if money is None:
        print(f"No money found for game ID: {saved_game}. Returning 0.")
        return 0
    money_now = int(money[0])
    return money_now


def location_now(game_id):
    sql = (f'SELECT location from game where id = "{game_id}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    current_location = cursor.fetchall()[0][0]
    return current_location


def accuse_weapon_suspect(game_id):
    # --- adds the accused weapon to accusations table
    weapon_accusation = input("Make your weapon accusation: ")
    suspect_accusation = input("Who do you suspect: ")
    airport_accusation = location_now(game_id)
    #testi airport_accusation = "Belgium"
    sql = f'insert into accusations(weapon_accusations,location_accusations,suspect_accusations) values("{weapon_accusation}","{airport_accusation}","{suspect_accusation}")'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    #fff = cursor.fetchone()
    check_accusations(game_id)
    return

def check_accusations(game_id):
    sql = (f'select weapon_accusations,location_accusations,suspect_accusations from accusations')
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
print(location_now(select_game))
start_accusations()

while check_money(select_game) > 0 and not victory:
    # saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    print(f"You have {check_money(select_game)}€ left.\n")
    print('See the options by typing "help".\n')
    game_round = input("What would you like to do: ")
    accusation_counter = command_counter = 0


    while command_counter == 0:
        if game_round.lower() == "accuse":
            accusation_counter += 1
            command_counter += 1
            accuse_weapon_suspect(select_game)
            # accusation_counter += 1
            # print(check_if_correct())
            command_counter += 1
            game_round = input("What would you like to do: ")
        elif game_round.lower() == "fly":
            destination = input("Where would you like to fly next: ")
            command_counter = 0
            game_round = input("What would you like to do: ")
            # fly()
        elif game_round.lower() == "check accusations":
            check_accusations(select_game)
            game_round = input("What would you like to do: ")
        elif game_round == "help":
            print("hello")
            game_round = input("What would you like to do: ")
            # print(help_ville())
        else:
            print("Check spelling on your command.")
            game_round = input("What would you like to do: ")
    if command_counter == 1:
        print("Here are your current accusations.")
        check_accusations(select_game)
        print("")
        destination = input("Where would you like to fly next: ")
        command_counter = 0
        # fly()

# These can be changed to work better with the outro.
if check_money(1) <= 0:
    print("You ran out of money.")
elif victory:
    print("You solved the mystery!")


