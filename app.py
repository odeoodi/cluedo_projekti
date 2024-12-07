import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from database_connector import db_connection
import codes.config
from the_game import Game
from codes.start import start_money, start_location, start_accusations, insert_right_answers
from codes.get_from_sql import from_sql_weapons, form_sql_suspects,from_sql_locations
from codes.check_if_correct import check_if_correct_location, check_if_correct_weapon, check_if_correct_suspect
from codes.check_money import check_money
from codes.fly import flying_new_port, cost_of_flying
from codes.gambling import if_winning, pay, add_money
from codes.api import get_api_data



thisgame = Game(codes.config.game_id, codes.config.name)

app = Flask(__name__)
cors = CORS(app)

@app.route('/new_game')
def new_game(connection = db_connection):
    connect = connection
    start_location(connect)
    start_accusations(connect)
    start_money(thisgame.id,codes.config.money, connect)
    insert_right_answers(connect)
    return 'ok'

@app.route('/getweapons')
def weapons_data(connector = db_connection):
    connect = connector
    data = from_sql_weapons(connect)
    jsondata = json.dumps(data)
    return jsondata

@app.route('/getsuspects')
def suspects_data(connector = db_connection):
    connect = connector
    data = form_sql_suspects(connect)
    jsondata = json.dumps(data)
    return jsondata

@app.route('/getlocations')
def locations_data(connector = db_connection):
    connect = connector
    data = from_sql_locations(connect)
    pop_up_text=get_api_data(data)
    data.append(pop_up_text)
    jsondata = json.dumps(data)
    return jsondata

@app.route('/checkmoney')
def check_money_sql(connector = db_connection):
    connect = connector
    playermoney = check_money(thisgame.id, connect)
    jsonmoney = json.dumps(playermoney)
    return jsonmoney

@app.route('/game_status')
def game_status(connector = db_connection):
    connect = connector
    winnig = thisgame.winning()
    loosing = thisgame.losing(connect)
    if winnig:
        return jsonify({'status': 'win'})
    elif winnig != True and loosing == True:
        return jsonify({'status': 'loose'})
    else:
        return jsonify({'status': 'continue'})


@app.route ('/hints/<weapon>/<suspect>/<location>')
def hints(weapon, suspect, location):
    weapon =(weapon)
    suspect = (suspect)
    location = (location)
    # hint_list = (here iidas function which will take as parameter weapon, suspect and location.)
                # code will hints as return list with two paragraphs, 1. Text which comes to game box, 2. Text which goes to notebook.
    # return hint_list

@app.route('/fly/<icao>')
def in_game_fly(icao):
    icao = icao
    flying_new_port(icao)
    cost_of_flying(codes.config.fly_cost)
    return 'ok'

@app.route('/gamble_winning/<int:dice1>/<int:dice2>/<int:dice3>')
def gamble_winning(dice1, dice2, dice3,):
    try:
        winpoint, wintext = if_winning(dice1, dice2, dice3)
        response = {
            'points': winpoint,
            'message': wintext
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pay/<cost>/<select_game>') # this function deducts the gambling cost from the players money amount
def pay_gamble(cost, connection = db_connection):
    connect = connection
    cost = cost
    select_game = thisgame.id
    payed = pay(cost,select_game, connect)
    print("gamble payed")
    return payed

@app.route('/add-money-gamble/<added>/<select_game>')
def add_money_gamble(added, connection = db_connection):
    connect = connection
    added = added
    select_game = thisgame.id
    ok_money = add_money(added, select_game, connect)
    print('win money added')
    return ok_money


@app.route('/accuse/<weapon>/<suspect>/<location>')
def accuse(weapon, suspect, location, connector = db_connection):
    connect = connector
    weapon = weapon
    suspect = suspect
    location = location
    is_weapon = check_if_correct_weapon(weapon, connect)
    is_suspect = check_if_correct_suspect(suspect, connect)
    is_location = check_if_correct_location(location, connect)
    jsonanwsver = json.dumps([is_weapon, is_suspect, is_location])
    return jsonanwsver



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)