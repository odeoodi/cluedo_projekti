import mysql.connector
from codes.location_now import location_now
from database_connector import db_connection


def check_if_correct_weapon(weapon_accusation, connector):
    # Checks whether the weapon accusation is correct.
    connect = connector
    sql1 = f"SELECT id FROM weapons WHERE weapon = '{weapon_accusation}' "
    kursori = connect.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_weapons FROM right_answers WHERE id_weapons = '{accusation_id}' "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    if not accusations:
        return False
    elif accusations:
        return True

def check_if_correct_location(connector, game_id):
    # Checks whether the location accusation is correct.
    connect = connector
    sql1 = f"SELECT id FROM locations WHERE name = '{location_now(game_id)}'"
    kursori = connect.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_locations FROM right_answers WHERE id_locations = '{accusation_id}' "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    if not accusations:
        return False
    elif accusations:
        return True

def check_if_correct_suspect(suspect_accusation, connector):
    # Checks whether the suspect accusation is correct.
    connect = connector
    sql1 = f"SELECT id FROM suspects WHERE names = '{suspect_accusation}' "
    kursori = connect.cursor()
    kursori.execute(sql1)
    accusation_id = kursori.fetchone()[0]
    sql2 = f"SELECT id_suspects FROM right_answers WHERE id_suspects = {accusation_id} "
    kursori.execute(sql2)
    accusations = kursori.fetchone()
    if not accusations:
        return False
    elif accusations:
        return True
