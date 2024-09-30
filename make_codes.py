from shutil import which
from tabnanny import check

import mysql.connector

db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='detective_game',
         user='heikki',
         password='pekka',
         autocommit=True
         )

'''
def location():
    # Empties locations tabel. Selects 5 random location from airport tabel and adds them to locations table.
    sql1= (f'DELETE FROM LOCATIONS;')
    sql2= (f'insert into locations(name) SELECT name FROM airport WHERE continent = "EU" and type = "large_airport" ORDER BY RAND() limit 5;')
    cursor = db_connection.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    db_connection.commit()
    return

location()
'''

def start_location():
    # select one random loaction from locations tabel as location where the game starts
    sql= (f'insert into game(location) SELECT name FROM locations ORDER BY RAND() limit 1;')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    db_connection.commit()
    return

# def fly():

start_location()




