import random
import mysql.connector



db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

class WinMoney:
    def __init__(self, select_game):
            self.select_game = select_game
            num = random.randint(0, 4)
            amount = [25, 50, 100, 150, 200]
            print(f'You have won {amount[num]}.')

            def win(amount, num,select_game):
                money = f'UPDATE game SET money = money+ %s WHERE id = %s'
                cursor = db_connection.cursor()
                cursor.execute(money, (amount[num], select_game))
                db_connection.commit()
                return

            win(amount, num, select_game)

class PayGambling:
    def __init__(self, select_game):
        self.select_game = select_game
        cost = 50
        print(f'You pay {cost}€ to try your luck.')

        def pay( cost, select_game):
            loose = f'UPDATE game SET money = money- %s WHERE id = %s'
            cursor = db_connection.cursor()
            cursor.execute(loose, (cost, select_game))
            db_connection.commit()
            return

        pay(cost, select_game)

def gambling(select_game):
        roll = random.randint(1, 10)
        paying = PayGambling(select_game)
        if roll <= 2:
           win = WinMoney(select_game)
        else:
            print('No win')




