import mysql.connector
import location_now


db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

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
