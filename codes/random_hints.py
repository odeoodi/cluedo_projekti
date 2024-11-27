import mysql.connector

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

def random_hints():
    # Gives the user hints by randomly selecting a location, a weapon and a suspect then checking if it is in the right_answers
    # and telling the result.
    cursor = db_connection.cursor()
    cursor.execute("SELECT id_locations, id_weapons, id_suspects FROM right_answers")
    exclusions = cursor.fetchall()
    excluded_locations = [row[0] for row in exclusions]
    excluded_weapons = [row[1] for row in exclusions]
    excluded_suspects = [row[2] for row in exclusions]

    if excluded_locations:
        cursor.execute(f"SELECT * FROM locations WHERE id NOT IN ({','.join(map(str, excluded_locations))}) ORDER BY RAND() LIMIT 1")
    else:
        cursor.execute("SELECT * FROM locations ORDER BY RAND() LIMIT 1")
    random_location = cursor.fetchone()

    if excluded_weapons:
        cursor.execute(f"SELECT * FROM weapons WHERE id NOT IN ({','.join(map(str, excluded_weapons))}) ORDER BY RAND() LIMIT 1")
    else:
        cursor.execute("SELECT * FROM weapons ORDER BY RAND() LIMIT 1")
    random_weapon = cursor.fetchone()

    if excluded_suspects:
        cursor.execute(f"SELECT * FROM suspects WHERE id NOT IN ({','.join(map(str, excluded_suspects))}) ORDER BY RAND() LIMIT 1")
    else:
        cursor.execute("SELECT * FROM suspects ORDER BY RAND() LIMIT 1")
    random_suspect = cursor.fetchone()

    cursor.execute(
        """
        UPDATE accusations
        SET weapon_accusations = %s, location_accusations = %s, suspect_accusations = %s
        WHERE id = %s
        """,
        (random_weapon[1], random_location[1], random_suspect[1], 1))

    return random_location[1], random_weapon[1], random_suspect[1]