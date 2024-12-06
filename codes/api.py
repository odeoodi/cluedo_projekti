import requests

def api(long, lat):
    info = ()
    key = "0aaa6428b03947689af5ae726e15192c"
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

        return list

    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]


longitude = -0.1278
latitude = 51.5074

result = api(longitude, latitude)

if "Error" in result[0]:
    print(result[0])
else:
    print(f"Capital: {result[0]}, Flag: {result[1]}, Country: {result[2]}")
