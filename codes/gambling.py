import random
import mysql.connector
from flask import Flask, request
from flask_cors import CORS
import codes.config


db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

class Gambling:
    def __init__(self, select_game):
        self.select_game = 1
        dice1 = 0
        dice2 = 0
        dice3 = 0
        self.rolls = 2

    def gambling_rule(self):
            print(f'\nAt the start of the game you will roll three dices.\nAfter that you have two re-rolls. Select dice which you want to roll.\n'
                  f'\nIf you get 3 times 1, you win the grand prize of 250€.'
                  f'\nIf you get 2 times 6, you  win 150€.'
                  f'\nIf you get 2 times 5, you win 100€.\n')
            return
    @staticmethod
    def if_winning(dice1,dice2,dice3):
            if dice1 == 1 and dice2 == 1 and dice3 == 1:
                wintext = "You have 3 times 1, you are winning 250€"
                winpoint = 3
                return winpoint, wintext
            elif dice1 == 5 and dice2 == 5 or (dice3 == 5 and dice2 == 5 or(dice1 == 5 and dice3 == 5 )):
                wintext = "You have 2 times 5, you are winning 100€ "
                winpoint = 1
                return winpoint, wintext
            elif dice1 == 6 and dice2 == 6 or (dice3 == 6 and dice2 == 6 or(dice1 == 6 and dice3 == 6 )):
                wintext = "You have 2 times 6, you are winning 150€ "
                winpoint = 2
                return winpoint, wintext
            else:
                wintext = f"You have nothing..."
                winpoint = 0
                return winpoint, wintext


    def roll(self):
            dice = random.randint(1, 6)
            return dice

    def playing(self, select_game):
            print()
            PayGambling(select_game)
            dice1 = self.roll()
            dice2 = self.roll()
            dice3 = self.roll()
            while self.rolls > 0:
                print(f'\nYou have rolled: \nDice 1 - {dice1} \nDice 2 - {dice2} \nDice 3 - {dice3}\n')
                self.if_winning(dice1, dice2, dice3)
                next = input(f"\nWhat would you like to do? 'End' to end gambling, "
                             f"\n'Reroll' to roll dice ({self.rolls} - left):").lower()
                if next == 'end':
                    self.rolls = 0
                elif next == 'reroll':
                    run = True
                    while run:
                        select_die = input(f'\nSelect dice you want to roll. Use dice number.\n'
                                           f'Dice 1 = {dice1}\n'
                                           f'Dice 2 = {dice2}\n'
                                           f'Dice 3 = {dice3}\n'
                                           f'\nWhich dice?:')
                        if select_die =='1':
                            dice1 = self.roll()
                            self.rolls -= 1
                            run = False
                        elif select_die == '2':
                            dice2 = self.roll()
                            self.rolls -= 1
                            run = False
                        elif select_die == '3' :
                            dice3 = self.roll()
                            self.rolls -= 1
                            run = False
                        else:
                            print(f'Check your input.')

                else:
                    print(f'Check your input.')
            print()
            print(f'\nYou have: \nDice 1 - {dice1} \nDice 2 - {dice2} \nDice 3 - {dice3}\n')
            self.if_winning(dice1, dice2, dice3)
            winpoint = self.if_winning(dice1, dice2, dice3)
            WinMoney(select_game, winpoint)
            return

    def gamble(self, select_game):
            start_text = 'Are you ready to start? Write "yes" or "no". "Rules" if you want to read rules:'
            while True:
                start = input(f'Are you ready to start?\nWrite "yes" or "no". "Rules" if you want to read rules:').lower().strip()

                if start == 'yes':
                    self.playing(select_game)
                    break

                elif start == 'no':
                    break

                elif start == 'rules':
                    self.gambling_rule()

                else :
                    print(f'\nCheck your input.\n')
            return

class WinMoney(Gambling):
    def __init__(self, select_game, num):
            super().__init__(select_game)
            num = num
            amount = [0, 100, 150, 250]
            print(f'You won {amount[num]}€.')



def pay(cost, select_game):
    loose = f'UPDATE game SET money = money- %s WHERE id = %s'
    cursor = db_connection.cursor()
    cursor.execute(loose, (cost, select_game))
    db_connection.commit()
    print(f'You pay {cost}€ to try your luck.')
    return {"status": "ok"}, 200

def add_money(added,select_game):
        money = f'UPDATE game SET money = money+ %s WHERE id = %s'
        cursor = db_connection.cursor()
        cursor.execute(money, (added, select_game))
        db_connection.commit()
        return 'ok'



'''
app = Flask(__name__)
cors = CORS(app)

@app.route('/gamble')
def gamble_java():
    start_text = 'Are you ready to start?'
    gamer= Gambling(codes.config.game_id)
    yield start_text
    #args = request.args
    #yes = args.get('yes')



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


'''