# --- adds the accused weapon to accusations table
def check_if_correct_weapon(weapon_accusation):
    sql1 = f"SELECT id FROM weapons WHERE weapon = '{weapon_accusation}' "
    kursori = db_connection.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_weapons FROM right_answers WHERE id = '{accusation_id}' "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    matches = []
    if not accusations:
        return False
    elif accusations:
        return True


def check_if_correct_location(location_accusation):
    sql1 = f"SELECT id FROM locations WHERE name = '{location_accusation}' "
    kursori = db_connection.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    print(accusation_id)
    sql2 = f"SELECT id_locations FROM right_answers WHERE id = '{accusation_id}' "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    print(accusations)
    matches = []
    if not accusations:
        return False
    elif accusations:
        return True


def check_if_correct_suspect(suspect_accusation):
    sql1 = f"SELECT id FROM suspects WHERE names = '{suspect_accusation}' "
    kursori = db_connection.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    print(accusation_id)
    sql2 = f"SELECT id_suspects FROM right_answers WHERE id = {accusation_id} "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    print(accusations)
    matches = []
    if not accusations:
        return False
    elif accusations:
        return True


weapon_options = 'spoon', 'knife', 'poison', 'pencil', 'pistol'
suspect_options = 'Make', 'Iida', 'Ode', 'Angelina', 'Ville'
print("Weapons to choose from: spoon, knife, poison, pencil, pistol")
weapon_accusation = input("Make your weapon accusation: ")
while weapon_accusation not in weapon_options:
    print("Where did you find this? Put it back.")
    weapon_accusation = input("Make your weapon accusation: ")
print("Suspects to choose from: Make, Iida, Ode, Angelina, Ville")
suspect_accusation = input("Who do you suspect: ")
while suspect_accusation not in suspect_options:
    print("They are not here. Try again.")
    suspect_accusation = input("Who do you suspect: ")
airport_accusation = location_now(game_id)
sql = f'update accusations set weapon_accusations = "{weapon_accusation}",location_accusations = "{airport_accusation}",suspect_accusations = "{suspect_accusation}" WHERE id = {the_accusation + 1}'
cursor = db_connection.cursor()
cursor.execute(sql)
weapon_right = check_if_correct_weapon(weapon_accusation)
suspect_right = check_if_correct_suspect(suspect_accusation)
location_right = check_if_correct_location(airport_accusation)

if weapon_right:
    print("You have the correct weapon!")
if suspect_right:
    print("You have the correct suspect!")
if location_right:
    print("You have the correct airport!")
return
