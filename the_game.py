import mysql.connector
from codes.location_now import location_now
from codes.start import start_location, start_money, start_accusations, insert_right_answers
from codes.rules import rules
from codes.check_if_correct import check_if_correct_location,check_if_correct_weapon,check_if_correct_suspect
from codes.print_story import print_story
from codes.press_enter import press_enter_to_continue
from codes.help_command import help_command
from codes.random_hints import random_hints
from codes.gambling import Gambling
from codes.check_money import check_money
from codes.check_accustations import check_accusations
from codes.acccuse import accuse_weapon_suspect
from codes.win import win
import codes.config

class Game:
    right_answers = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.money_neede = codes.config.gamble_cost

    def checkmony(self, connector):
        connect = connector
        game_id = self.id
        sql = f'select money from game where id = "{game_id}"'
        cursor = connect.cursor()
        cursor.execute(sql)
        money = cursor.fetchone()
        money_now = int(money[0])
        return money_now

    def losing(self, connector):
        needed = self.money_neede
        connect = connector
        current_money = self.checkmony(connect)
        if current_money < needed:
            return True
        else:
            return False

    def winning(self, connector, weapon, suspect, location):
        connect = connector
        weapon = 'rope'
        suspect = 'Emmet'
        location = 'Vnukovo International Airport'
        is_weapon = check_if_correct_weapon(weapon)
        is_suspect = check_if_correct_suspect(suspect)
        is_location = check_if_correct_location(location)
        answer = [is_weapon, is_suspect, is_location]

        for i in answer:
            if i is True:
                Game.right_answers += 1
        if Game.right_answers == 3:
            return True
        else:
            return False








'''
# Start of game:
victory = False
select_game = 1
# accusation_counter = 0
start_location()
start_money(select_game)
#print(location_now(select_game))
start_accusations()
insert_right_answers()
rules()
print_story()
press_enter_to_continue()
random_hints()

print('\nSee the options by typing "help".\n')
print(f"You have {check_money(select_game)} € left.\n"
      f"You are now at {location_now(select_game)}.")
print("Here are your current clues, these are not part of the crime:")

check_accusations(select_game)
accusation_counter = 1
command_counter = 0
game_round = ""
# Game loop.
while check_money(select_game) > 0 and not victory and game_round != "end game":
    # saved_game = input("Select saved game: ") // possible if we want to save games to the game table and identify them by id number.
    game_round = input("What would you like to do: ").lower()
    command_counter = 0
    while command_counter == 0 and not victory:
        if check_money(select_game) == 0:
            print("\nMake your final accusations.")
            accusation_counter += 1
            accuse_weapon_suspect(select_game, accusation_counter)
            victory = win(accusation_counter)
            break
        if game_round.lower() == "accuse":
            accusation_counter += 1
            command_counter += 1
            accuse_weapon_suspect(select_game,accusation_counter)
            victory = win(accusation_counter)
            if victory:
                break
            # game_round = input("What would you like to do: ")
        elif game_round.lower() == "fly":
            fly()
            command_counter = 0
            if check_money(select_game) > 0:
                game_round = input("What would you like to do: ").lower()
        elif game_round.lower() == "check accusations":
            check_accusations(select_game)
            game_round = input("What would you like to do: ").lower()
        elif game_round == "help":
            help_command()
            game_round = input("What would you like to do: ").lower()
        elif game_round == "gamble":
            rungame = Gambling(select_game)
            rungame.gamble(select_game)
            game_round = input("What would you like to do: ").lower()
        elif game_round == "end game":
            break
        else:
            print("Check spelling on your command.")
            game_round = input("What would you like to do: ").lower()
        if command_counter == 1 and check_money(select_game) > 0:
            print("\nHere are your current accusations:")
            check_accusations(select_game)
            print("")
            press_enter_to_continue()
            fly()
            game_round = input("What would you like to do: ").lower()
            command_counter = 0



#End of the game.
if check_money(select_game) <= 0 and not victory:
    print("OH NO! Unfortunately, your money has run out, and the criminal gets away without punishment… You tried your best, better luck next time!")
elif victory:
    print("Congratulations! You've identified the culprit, and the police can now press charges. \nYou've done an amazing job, and I hope you're proud of yourself. Keep up the great work!")
'''