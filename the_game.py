from tabnanny import check

import mysql.connector
import random

def check_money(saved_game):
    sql = f'select money from game where id = "{saved_game}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    money = cursor.fetchone()
    money_now = money[0]
    return money_now

#def accuse_weapon():
    #adds the accused weapon to accusations table


def correct_weapon():
    # tarvitsen right_answers taulusta oikeat vastaukset ja accusations taulusta syytökset. Vertaan, onko kaikki right_answers
    # taulun tiedot accusations taulussa. Periaatteessa toimii, jos yhdistän taulut ja katson onko right_answers.id_weapons
    # (ja sama kuin weapons -taulun id, josta saadaan weaponin nimi) myös accusations taulussa ja sama locationille ja suspecteille.
    sql = f'from right_answers inner join goal_reached on goal_reached.right_answers_id = right_answers.id_weapons inner join weapons on weapons.id = right_answers.id_weapons where right_answers.id_weapons = weapons.id'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    right_weapon = cursor.fetchall()
    if len(right_weapon) == 1:
        first_right = True
    return first_right

def correct_suspect():
    #tarvitsen right_answers taulusta oikeat vastaukset ja accusations taulusta syytökset. Vertaan, onko kaikki right_answers
    # taulun tiedot accusations taulussa. Periaatteessa toimii, jos yhdistän taulut ja katson onko right_answers.id_weapons
    # (ja sama kuin weapons -taulun id, josta saadaan weaponin nimi) myös accusations taulussa ja sama locationille ja suspecteille.
    sql = f''
    cursor = db_connection.cursor()
    cursor.execute(sql)
    right_suspect = cursor.fetchall()
    if right_suspect:
        second_right = True
    return second_right

def correct_location():
    #tarvitsen right_answers taulusta oikeat vastaukset ja accusations taulusta syytökset. Vertaan, onko kaikki right_answers
    # taulun tiedot accusations taulussa. Periaatteessa toimii, jos yhdistän taulut ja katson onko right_answers.id_weapons
    # (ja sama kuin weapons -taulun id, josta saadaan weaponin nimi) myös accusations taulussa ja sama locationille ja suspecteille.
    sql = f''
    cursor = db_connection.cursor()
    cursor.execute(sql)
    right_location = cursor.fetchall()
    if right_location:
        third_right = True
    return third_right

def win():
    loc_true = correct_location()
    sus_true = correct_suspect()
    wea_true = correct_weapon()
    if loc_true and sus_true and wea_true:
        victory = True
    return victory







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

while check_money(1) > 0 and not victory:
    #saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    print(f"You have {check_money(1)}€ left.")
    print("")
    print('See the options by typing "help".')
    game_round = input("What would you like to do: ")

    if game_round.lower() == "accuse":
        weapon_accusation = input("Make your weapon accusation: ")
        suspect_accusation = input("Who do you suspect: ")
        location_accusation = location_now()
        #print(check_if_correct())
    elif game_round.lower() == "fly":
        destination = input("Where would you like to fly next: ")
        #fly()
    elif game_round.lower() == "check accusations":
        #print(accusations())
    #elif game_round == "help":
        #print(help())
    #else:
        print("Check spelling on your command.")

#These can be changed to work better with the outro.
if check_money(1) <= 0:
    print("You ran out of money.")
elif victory:
    print("You solved the mystery!")


