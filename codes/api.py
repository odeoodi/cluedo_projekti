import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

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
        list = [capital, flag_url, country]
        jsonlist = json.dumps(list)

        return jsonlist

    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]

def get_api_data(data):
    pop_up_text = []
    for i in data:
        info = api(i[2], i[3])
        pop_up_text.append(info)
    return pop_up_text

'''

longitude = -3.372288
latitude = 55.950145

result = api(longitude, latitude)

if "Error" in result[0]:
    print(result[0])
else:
    print(f"Capital: {result[0]}, Flag: {result[1]}, Country: {result[2]}")

'''
