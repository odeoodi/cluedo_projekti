from tabnanny import check

import mysql.connector
import random
def location():
    # Empties locations tabel. Selects 5 random location from airport tabel and adds them to locations table.
    sql1= (f'DELETE FROM LOCATIONS;')
    sql2= (f'insert into locations(name) SELECT name FROM airport WHERE continent = "EU" and type = "large_airport" ORDER BY RAND() limit 5;')
    cursor = db_connection.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    db_connection.commit()
    return

def check_money(saved_game):
    sql = f'select money from game where id = "{saved_game}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    money = cursor.fetchone()
    money_now = money[0]
    return money_now

def location_now():
    sql = (f'SELECT airport.name from airport inner join locations on airport.ident = locations.icao '
           f'inner join right_answers on right_answers.id_locations = locations.id '
           f'inner join goal_reached on goal_reached.right_answers_id = right_answers.id '
           f'inner join game on goal_reached.game_id = game.location '
           f'where game.location = airport.ident')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    current_location = cursor.fetchall()
    return

def accuse_weapon_suspect():
    #adds the accused weapon to accusations table
    weapon_accusation = input("Make your weapon accusation: ")
    suspect_accusation = input("Who do you suspect: ")
    #suspect_airport =
    sql = f'insert into accusations(weapon_accusations,location_accusations,suspect_accusations) values("{weapon_accusation}","{suspect_airport}","{suspect_accusation}")'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    #fff = cursor.fetchone()
    return

def check_accusations():
    sql = f'select weapon_accusations,suspect_accusations,airport_accusations from accusations'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    made_accusations = cursor.fetchall()
    for acc in made_accusations:
        print(f"{acc[0]} ", end="")
        print(f"{acc[1]} ", end="")
        print(f"{acc[2]} ", end="")
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
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='detective_game',
         user='heikki',
         password='pekka',
         autocommit=True
         )


#intro()

victory = False
#accusation_counter = 0

while check_money(1) > 0 and not victory:
    #saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    location()
    print(f"You have {check_money(1)}€ left.\n")
    print('See the options by typing "help".\n')
    game_round = input("What would you like to do: ")
    command_counter = 0

    while command_counter == 0:
        if game_round.lower() == "accuse":
            accuse_weapon_suspect()
            #accusation_counter += 1
            #print(check_if_correct())
            command_counter += 1
            game_round = input("What would you like to do: ")
        elif game_round.lower() == "fly":
            destination = input("Where would you like to fly next: ")
            command_counter = 0
            game_round = input("What would you like to do: ")
            #fly()
        elif game_round.lower() == "check accusations":
            check_accusations()
            game_round = input("What would you like to do: ")
        elif game_round == "help":
            print("hello")
            game_round = input("What would you like to do: ")
            #print(help_ville())
        else:
            print("Check spelling on your command.")
            game_round = input("What would you like to do: ")
    if command_counter == 1:
        destination = input("Where would you like to fly next: ")
        command_counter = 0
        # fly()

#These can be changed to work better with the outro.
if check_money(1) <= 0:
    print("You ran out of money.")
elif victory:
    print("You solved the mystery!")


