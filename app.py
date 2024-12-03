import json
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import codes.config
from codes.start import start_money, start_location, start_accusations, insert_right_answers
from codes.get_from_sql import from_sql_weapons, form_sql_suspects,from_sql_locations
from codes.check_if_correct import check_if_correct_location, check_if_correct_weapon, check_if_correct_suspect

from codes.fly import flying_new_port, cost_of_flying



app = Flask(__name__)
cors = CORS(app)

db_connection = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='detective_game2',
    user='heikki',
    password='pekka',
    autocommit=True
)


@app.route('/new_game')
def new_game():
    start_location()
    start_accusations()
    start_money(codes.config.game_id,codes.config.money)
    insert_right_answers()
    return 'ok'

@app.route('/getweapons')
def weapons_data():
    data = from_sql_weapons()
    jsondata = json.dumps(data)
    return jsondata

@app.route('/getsuspects')
def suspects_data():
    data = form_sql_suspects()
    jsondata = json.dumps(data)
    return jsondata

@app.route('/getlocations')
def locations_data():
    data = from_sql_locations()
    jsondata = json.dumps(data)
    return jsondata


@app.route('/fly/<icao>')
def in_game_fly(icao):
    icao = (icao)
    flying_new_port(icao)
    cost_of_flying(codes.config.fly_cost)
    return 'ok'

@app.route('/accuse/<weapon>/<suspect>/<location>')
def accuse(weapon, suspect, location):
    weapon = (weapon)
    suspect = (suspect)
    location = (location)
    is_weapon = check_if_correct_weapon(weapon)
    is_suspect = check_if_correct_suspect(suspect)
    is_location = check_if_correct_location(location)
    jsonanwsver = [is_weapon, is_suspect, is_location]
    return jsonanwsver










if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)