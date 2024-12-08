def from_sql_weapons(connector):
    connect = connector
    get_info = f"SELECT weapon, attribute1, attribute2  FROM weapons"
    kursori = connect.cursor()
    kursori.execute(get_info)
    get_weapons = kursori.fetchall()
    return get_weapons

def from_sql_suspects(connector):
    connect = connector
    get_info2 = f"SELECT names, sex, age, glasses  FROM suspects"
    kursori = connect.cursor()
    kursori.execute(get_info2)
    get_suspects = kursori.fetchall()
    return get_suspects

def from_sql_locations(connector):
    connect = connector
    get_info3 = f"SELECT name, icao, latitude_deg,longitude_deg   FROM locations"
    kursori = connect.cursor()
    kursori.execute(get_info3)
    get_locations = kursori.fetchall()
    return get_locations