import mysql.connector
from codes.start import start_location, start_money, start_accusations
from codes.right_answers import insert_right_answers
from codes.location_now import location_now
from codes.random_hints import random_hints
from codes.check_money import check_money
from codes.press_enter import press_enter_to_continue
from codes.print_story import print_story
from codes.fly import fly
from codes.win import win
from codes.rules import rules
from codes.help_command import help_command
from codes.acccuse import accuse_weapon_suspect
from codes.check_accustations import check_accusations

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

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


