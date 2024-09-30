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

def accuse_weapon():
    #adds the accused weapon to accusations table
    weapon_accusation = input("Make your weapon accusation: ")
    sql = f'insert into accusations(weapon_accusations) values("{weapon_accusation}")'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    #fff = cursor.fetchone()
    return

def accuse_suspect():
    suspect_accusation = input("Who do you suspect: ")
    sql = f'insert into accusations(suspect_accusations) values("{suspect_accusation}")'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    #fff = cursor.fetchone()
    return
'''
def accuse_location():
    airport_accusation = location_now()
    sql = f'insert into accusations(airport_accusations) values("{airport_accusation}")'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    #fff = cursor.fetchone()
    return
'''


'''
angelinan koodi check if correct
def win():
    loc_true = correct_location()
    sus_true = correct_suspect()
    wea_true = correct_weapon()
    if loc_true and sus_true and wea_true:
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

while check_money(1) > 0 and not victory:
    #saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    print(f"You have {check_money(1)}€ left.")
    print("")
    print('See the options by typing "help".')
    game_round = input("What would you like to do: ")

    if game_round.lower() == "accuse":
        accuse_weapon()
        accuse_suspect()
        #accuse_location()
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


