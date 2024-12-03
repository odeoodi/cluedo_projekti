import mysql.connector

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)


def from_sql():
    get_info = f"SELECT weapon, attribute1, attribute2  FROM weapons"
    get_info2 = f"SELECT names, sex, age, glasses  FROM suspects"
    get_info3 = f"SELECT name, icao  FROM locations"
    kursori = db_connection.cursor()
    kursori.execute(get_info)
    get_weapons = kursori.fetchall()
    kursori.execute(get_info2)
    get_suspects = kursori.fetchall()
    kursori.execute(get_info3)
    get_locations = kursori.fetchall()
    print(get_weapons)
    print(get_suspects)
    print(get_locations)

from_sql()