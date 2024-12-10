

def location_now(game_id, connection):
    # Tells the user what airport they are at.
    connect = connection
    sql = (f'SELECT location FROM game WHERE id = "{game_id}"')
    cursor = connect.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        #print(results[0][0])
        current_location = results[0][0]
        return current_location
    else:
        print(f"No location found for game_id {game_id}.")
        return None