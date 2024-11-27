import mysql.connector

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)

def location_now(game_id):
    # Tells the user what airport they are at.
    sql = (f'SELECT location FROM game WHERE id = "{game_id}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        current_location = results[0][0]
        return current_location
    else:
        print(f"No location found for game_id {game_id}.")
        return None
