import mysql.connector


db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)


def start_location():
    # Selects 7 random location from airport tabel, checks that they are all uniques and adds them to locations table,
    # selects one of the airports as starting airport.
    while True:
        sql1= (f"UPDATE locations SET name = (SELECT name FROM airport WHERE continent = 'EU' AND type = 'large_airport' ORDER BY RAND()LIMIT 1);")
        sql1_1= (f"SELECT name FROM locations;")
        cursor = db_connection.cursor()
        cursor.execute(sql1)
        cursor.execute(sql1_1)
        sql1_1 = cursor.fetchall()
        db_connection.commit()
        dubles=0
        for outter in sql1_1:
            if sql1_1.count(outter) > 1:
                dubles += 1
            if dubles != 0:
                continue
        if dubles <= 0:
            break
    sql2= (f"UPDATE locations SET icao = (SELECT ident FROM airport WHERE locations.name = airport.name LIMIT 1);")
    sql3= (f"UPDATE game SET location = (SELECT name FROM locations ORDER BY RAND() limit 1);")
    cursor = db_connection.cursor()
    cursor.execute(sql2)
    cursor.execute(sql3)
    db_connection.commit()
    return

def start_accusations():
    # Empties previous accusations for a new game.
    sql1 = f"update accusations set weapon_accusations = NULL, suspect_accusations = NULL, location_accusations = NULL"
    #sql2 = f"alter table accusations auto_increment = 1"
    sql1 = f'update accusations set weapon_accusations = NULL, suspect_accusations = NULL, location_accusations = NULL'
    #sql2 = f'alter table accusations auto_increment = 1'
    cursor = db_connection.cursor()
    cursor.execute(sql1)
    #hints = cursor.fetchall()
    return

def start_money(game_id, money):
    # Gives the user 500 money at the start of the game
    sql = (f'UPDATE game SET money = "{money}" WHERE id = "{game_id}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    return

