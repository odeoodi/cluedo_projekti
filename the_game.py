import mysql.connector
from codes import intro_story, random_hints, rules, help_command, win
from codes.start import start_location, start_money, start_accusations
from codes.right_answers import insert_right_answers


# Functions:

def press_enter_to_continue():
    # Makes prints to take breaks and look pretty :3
    while True:
        enter=input(f"Press Enter to Continue:")
        if enter=='':
            break
        else:
            continue
    return




def check_if_correct_weapon(weapon_accusation):
    # Checks whether the weapon accusation is correct.
    sql1 = f"SELECT id FROM weapons WHERE weapon = '{weapon_accusation}' "
    kursori = db_connection.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_weapons FROM right_answers WHERE id_weapons = '{accusation_id}' "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    matches = []
    if not accusations:
        return False
    elif accusations:
        return True

def check_if_correct_location(airport_accusation):
    # Checks whether the location accusation is correct.
    sql1 = f"SELECT id FROM locations WHERE name = '{location_now(1)}' "
    kursori = db_connection.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_locations FROM right_answers WHERE id_locations = '{accusation_id}' "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    if not accusations:
        return False
    elif accusations:
        return True

def check_if_correct_suspect(suspect_accusation):
    # Checks whether the suspect accusation is correct.
    sql1 = f"SELECT id FROM suspects WHERE names = '{suspect_accusation}' "
    kursori = db_connection.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_suspects FROM right_answers WHERE id_suspects = {accusation_id} "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    matches = []
    if not accusations:
        return False
    elif accusations:
        return True

def accuse_weapon_suspect(game_id, the_accusation):
    # --- adds the accused weapon to accusations table
    cursor = db_connection.cursor()
    sql1 = f'select weapon from weapons'
    sql2 = f'select names from suspects'
    cursor.execute(sql1)
    weapon_options = []
    results_one = cursor.fetchall()
    weapon_options = [i[0] for i in results_one]
    cursor.execute(sql2)
    results_two = cursor.fetchall()
    suspect_options = [i[0] for i in results_two]
    print(f"Weapons to choose from: {', '.join(weapon_options)}")
    weapon_accusation = input("Make your weapon accusation: ").lower()
    while weapon_accusation not in weapon_options:
        print("Where did you find this? Put it back.")
        weapon_accusation = input("Make your weapon accusation: ").lower()
    print(f"Suspects to choose from: {', '.join(suspect_options)}")
    suspect_accusation = input("Who do you suspect: ").capitalize()
    while suspect_accusation not in suspect_options:
        print("They are not here. Try again.")
        suspect_accusation = input("Who do you suspect: ").capitalize()
    airport_accusation = location_now(1)
    sql = f'update accusations set weapon_accusations = "{weapon_accusation}",location_accusations = "{airport_accusation}",suspect_accusations = "{suspect_accusation}" WHERE id = {the_accusation}'
    cursor.execute(sql)
    weapon_right = check_if_correct_weapon(weapon_accusation)
    suspect_right = check_if_correct_suspect(suspect_accusation)
    location_right = check_if_correct_location(airport_accusation)

    if weapon_right:
        print("You have the correct weapon!")
    elif not weapon_right:
        print("This was not the murder weapon.")
    if suspect_right:
        print("You have the correct suspect!")
    elif not suspect_right:
        print("They are innocent.")
    if location_right:
        print("You have the correct airport!")
    elif not location_right:
        print("The murder did not happen here.")
    press_enter_to_continue()
    return

def check_accusations(game_id):
    # Shows the user what they have already guessed.
    sql = (f'select weapon_accusations,location_accusations,suspect_accusations from accusations where weapon_accusations is not NULL')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    made_accusations = cursor.fetchall()
    for acc in made_accusations:
        print(f"| {acc[0]} | ", end="")
        print(f"{acc[1]} | ", end="")
        print(f"{acc[2]} |", end="")
        print("")
    print("")
    return made_accusations

def fly():
# Druing this funktion player can fly to the new location.

    def locations_available():
        # This print all the airports and their ICAO-codes where player can fly.
        # Execludin the location where player is currently
        availabled = (f"SELECT icao, name FROM locations LEFT JOIN game ON locations.name = game.location WHERE game.location IS NULL ;")
        cursor = db_connection.cursor()
        cursor.execute(availabled)
        airports = cursor.fetchall()
        for airport in airports:
            print(f'ICAO: {airport[0]}, {airport[1]}. ')

    def icao_in_locations(destination):
        # Checks if the icao code is writen correctly.
        check = (f'SELECT name FROM locations; ')
        getname = (f'SELECT name FROM locations WHERE icao = "{destination}";')
        cursor = db_connection.cursor()
        cursor.execute(check)
        locations_check = cursor.fetchall()
        cursor.execute(getname)
        locations_icao_name = cursor.fetchall()
        if not locations_icao_name:
            return False
        elif locations_icao_name[0] in locations_check:
            return True


    def location_check(destination):
        # Checks if the destination where player wants to go is current location or not.
        # Returns True or False.
        getlocation = (f'SELECT location FROM game ;')
        getname = (f'SELECT name FROM locations WHERE icao = "{destination}";')
        cursor = db_connection.cursor()
        cursor.execute(getlocation)
        location_game = cursor.fetchall()
        cursor.execute(getname)
        locations_icao = cursor.fetchall()
        if location_game != locations_icao:
            return True
        else:
            return False

    def flying_new_port(destination):
        # Uppdates a new location to the database where player has flown.
        flying = (f'UPDATE game SET location = (SELECT name FROM locations WHERE icao = "{destination}");')
        cursor = db_connection.cursor()
        cursor.execute(flying)
        db_connection.commit()
        return

    def cost_of_flying():
        # Subtracts flying cost from the money player has.
        # Change (SELECT money -'125'....) to change cost.
        moneycost=(f'UPDATE game SET money =( SELECT money -125 FROM game ) ')
        cursor = db_connection.cursor()
        cursor.execute(moneycost)
        db_connection.commit()
        return


    while True:
        print(f'\nYou are currently at the {location_now(1)}.')
        press_enter_to_continue()
        print()
        print(f'Available airports for you to fly are:')
        locations_available()
        destination = input("\nWhere would you like to fly next, use the ICAO-code: ")
        destination = destination.upper()
        if icao_in_locations(destination) == True:
            if location_check(destination) == True:
                flying_new_port(destination)
                cost_of_flying()
                print(f'\nWelcome to {location_now(1)} you have {check_money(1)} euros.')
                press_enter_to_continue()
                print()
                break
            elif location_check(destination) == False:
                print("\nYou cannot stay at the same airport. If you do party people will leave and case won't be solved.")
                press_enter_to_continue()
                print()
        else :
            print("\nSorry your ICAO-code was not in the list, please try again.")
            press_enter_to_continue()
            print()

def print_story():
    #Asks if the user wants to know the intro then prints it
    while True:
        question = input('Do you wish to read the introduction story? "yes" or "no": ')
        question = question.lower()
        if question == 'yes':
            for line in intro_story.getStory():
                print(line)
            break
        elif question == 'no':
            print("\nLet the game begin!")
            break
        else:
            print("check spelling.")
    return

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


