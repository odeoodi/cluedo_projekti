from tabnanny import check

import mysql.connector
import random

def check_money(game_id):
    sql = f'select money from game where id = "{game_id}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    money = cursor.fetchone()
    money_now = money[0]
    return money_now

def win():
    #tarvitsen right_answers taulusta oikeat vastaukset ja accusations taulusta syytökset. Vertaan, onko kaikki right_answers
    # taulun tiedot accusations taulussa. Periaatteessa toimii, jos yhdistän taulut ja katson onko right_answers.id_weapons
    # (ja sama kuin weapons -taulun id, josta saadaan weaponin nimi) myös accusations taulussa ja sama locationille ja suspecteille.
    sql = f''
    cursor = db_connection.cursor()
    cursor.execute(sql)
    game_won = cursor.fetchall()
    if game_won:
        victory = True
    return victory






"""
pseudo code for one round:

intro() 


while money > 0 or right_answers in accusations:
    print(check_money())
    
    round = input("What would you like to do: ")
    print('See the options by typing "help"')
    
    if round == "help":
        print(help())
    elif round == "accuse":
        accusation = input("Make your accusations: ")
        print(check_if_correct())
    elif round == "fly":
        destination = input("Where would you like to travel: ")
        fly()
    elif round == "check accusations":
        print(accusations)
    elif round == "end game":
        end_game()
    
if money == 0:
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


while check_money(1) > 0 and not victory:
    #saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    print(f"You have {check_money(1)}€ left.")