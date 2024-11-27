import mysql.connector

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

def win(accusation_counter):
    # Shows whether the user has won or not.
    sql = f"SELECT weapon_accusations, suspect_accusations, location_accusations FROM accusations WHERE id = {accusation_counter};"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    last_accusations = cursor.fetchone()

    last_weapon = last_accusations[0]
    last_suspect = last_accusations[1]
    last_location = last_accusations[2]

    if last_accusations:
        right_weapon = check_if_correct_weapon(last_weapon)
        right_suspect = check_if_correct_suspect(last_suspect)
        right_location = check_if_correct_location(last_location)

        if right_weapon and right_suspect and right_location == True:
            print("You win!")
            return True
        else:
            return False
    else:
        return False