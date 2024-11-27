import mysql.connector
from codes.location_now import location_now
from codes.press_enter import press_enter_to_continue
from codes.check_if_correct import check_if_correct_location, check_if_correct_weapon, check_if_correct_suspect


db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)



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