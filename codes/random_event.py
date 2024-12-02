import random
import mysql.connector
from gambling import WinMoney

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

class RandomEvent:
    def __init__(self, select_game):
        self.select_game = select_game
        roll = random.randint(1, 10)
        print(roll)
        roll = 1
        if roll == 1:
            event = random.randint(1, 5)
            print(event)
            if event == 1:
                CleanNotebok.clean(self.select_game)
            elif event == 2:
                print (2)
            elif event == 3:
                print (3)
            elif event == 4:
                print (4)
            elif event == 5:
                print(5)
            else:
                print ('Wtf')
        else:
            return

class CleanNotebok:
    def __init__(self, select_game):
        super().__init__(select_game)

    def clean (self):
        empty = f'update accusations set weapon_accusations = NULL, suspect_accusations = NULL, location_accusations = NULL'
        cursor = db_connection.cursor()
        cursor.execute(empty)
        print(f'During your break you search your pocket for a notebook, to check out your clues.'
              f'\nHorror fills your mind when you realize that your pocket is empty.'
              f'\nYou have lost your notebook. All your clues are now gone!')
        return

class OldWallet:
    def __init__(self, select_game):
        super().__init__(select_game)

    def whatsinside(self, select_game):
        walletroll = random.randint(1, 10)
        print(f'Yuo have found a old wallet from the ground.')
        print (walletroll)
        while True:
            checkwallet = input(f'Would you like to check out your wallet? (Yes/No):').lower()
            if checkwallet == 'yes':
                if 1 < walletroll <= 8 :
                    print(f'You have found 100€ inside the wallet.')
                    addmoney = 100
                    money = f'UPDATE game SET money = money+ %s WHERE id = %s'
                    cursor = db_connection.cursor()
                    cursor.execute(money, (addmoney, select_game))
                    db_connection.commit()
                    break




            elif checkwallet == 'no':
                print('You leave a dirty old wallet alone.')
                break
            else:
                print('Check out your input.')




RandomEvent(1)
