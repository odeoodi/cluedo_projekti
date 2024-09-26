import mysql.connector
import random

db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='detective_game',
         user='heikki',
         password='pekka',
         autocommit=True
         )

#intro()

#the game starts here:

"""
pseudo code:
money = 500
while money > 0 or right_answers in accusations:
    print(money)
    
    round = input("What would you like to do: ")
    print('See the options by typing "help"')
    
    if round == "help":
        print(help())
    elif round == "accuse":
        accusation = input("Make your accusations: ")
        print(check_if_correct())
    elif round == "fly":
        destination = input("Where would you like to travel: ")
        travel()
    elif round == "check accusations":
        print(accusations)
    elif round == "end game":
        end_game()
    
if money = 0:
    print("you lost the game")
else:
    print("you won")
"""