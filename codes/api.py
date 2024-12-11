import json
import requests
import os
from dotenv import load_dotenv

from codes.config import game_id

load_dotenv()
from database_connector import db_connection
game_id = game_id

def api(lat, long):
    key =os.environ.get('API_KEY')
    try:
        geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{long}&key={key}"
        geocode_response = requests.get(geocode_url)

        if geocode_response.status_code != 200:
            return ["Error: Unable to fetch location data"]

        geocode_data = geocode_response.json()
        country_name = geocode_data['results'][0]['components']['country']

        country_url = f"https://restcountries.com/v3.1/name/{country_name}"
        country_response = requests.get(country_url)

        if country_response.status_code != 200:
            return ["Error: Unable to fetch country data"]

        country_data = country_response.json()[0]


        capital = country_data.get("capital", ["Unknown"])[0]
        flag_url = country_data.get("flags", {}).get("png", "No flag available")
        country = country_data.get("name", {}).get("common", "Unknown")
        list = {
            'city': capital,
            'country' : country,
            'flag_url': flag_url,}
        #jsonlist = json.dumps(list)

        return list

    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]

def get_api_data( connection = db_connection):
    connect = connection
    lat_lon = (f'SELECT latitude_deg, longitude_deg FROM locations')
    cursor = connect.cursor()
    cursor.execute(lat_lon)
    results = cursor.fetchall()
    loca_data = []
    numb = int(1)
    for i in results:
        info = api(i[0], i[1])
        loca_data.append(info)
    for d in loca_data:
        city = d["city"]
        country = d["country"]
        flag = d["flag_url"]
        add_me1 = f"UPDATE locations SET city = '{city}' WHERE id = {numb};"
        add_me2 = f"UPDATE locations SET country = '{country}' WHERE id = {numb};"
        add_me3 = f"UPDATE locations SET flag = '{flag}' WHERE id = {numb};"
        cursor.execute(add_me1)
        cursor.execute(add_me2)
        cursor.execute(add_me3)
        connect.commit()
        numb += 1
    return