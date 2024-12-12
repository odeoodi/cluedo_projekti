import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from codes.config import gamble_cost
from codes.game_saves import save_game, load_game
from codes.hints import *
from codes.location_now import location_now
from database_connector import db_connection
import codes.config
from the_game import Game
from codes.start import start_money, start_location, start_accusations, insert_right_answers, player_insert
from codes.get_from_sql import from_sql_weapons, from_sql_suspects,from_sql_locations
from codes.check_if_correct import check_if_correct_location, check_if_correct_weapon, check_if_correct_suspect
from codes.check_money import check_money
from codes.fly import flying_new_port, cost_of_flying
from codes.gambling import if_winning, pay, add_money
from codes.api import get_api_data

thisgame = Game(codes.config.game_id, codes.config.name)

app = Flask(__name__)
cors = CORS(app)

@app.route('/new_game')
def new_game():
    connect = db_connection
    start_location(connect)
    get_api_data(connect)
    start_accusations(connect)
    start_money(thisgame.id,codes.config.money, connect)
    insert_right_answers(connect)
    return 'ok'

@app.route('/save_name/<player_name>')
def save_name(player_name):
    connect = db_connection
    player_name = player_name
    player_insert(connect, player_name, thisgame.id)
    return 'saved'

@app.route('/getweapons')
def weapons_data():
    connect = db_connection
    data = from_sql_weapons(connect)
    jsondata = json.dumps(data)
    return jsondata

@app.route('/getsuspects')
def suspects_data():
    connect = db_connection
    data = from_sql_suspects(connect)
    jsondata = json.dumps(data)
    return jsondata

@app.route('/getlocations')
def locations_data():
    connect = db_connection
    data = from_sql_locations(connect)
    jsondata = json.dumps(data)
    return jsondata

@app.route('/checkmoney')
def check_money_sql():
    connect = db_connection
    playermoney = check_money(thisgame.id, connect)
    jsonmoney = json.dumps(playermoney)
    return jsonmoney

@app.route('/game_status')
def game_status():
    connect = db_connection
    winnig = thisgame.winning()
    loosing = thisgame.losing(connect)
    if winnig:
        return jsonify({'status': 'win'})
    elif winnig != True and loosing == True:
        return jsonify({'status': 'loose'})
    else:
        return jsonify({'status': 'continue'})

@app.route('/fly/<icao>')
def in_game_fly(icao):
    connect = db_connection
    icao = icao
    flying_new_port(icao, connect)
    cost_of_flying(codes.config.fly_cost, connect)
    return 'ok'

@app.route('/gamble_winning/<int:dice1>/<int:dice2>/<int:dice3>')
def gamble_winning(dice1, dice2, dice3):
    try:
        winpoint, wintext = if_winning(dice1, dice2, dice3)
        response = {
            'points': winpoint,
            'message': wintext
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pay/') # this function deducts the gambling cost from the players money amount
def pay_gamble():
    connect = db_connection
    select_game = thisgame.id
    pay(select_game, connect)
    print("gamble payed")
    return 'ok'

@app.route('/add-money-gamble/<added>')
def add_money_gamble(added):
    connect = db_connection
    added = added
    select_game = thisgame.id
    ok_money = add_money(added, select_game, connect)
    print('win money added')
    return ok_money

@app.route('/player-location-now')
def player_location_now():
    connect = db_connection
    select_game = thisgame.id
    player_location = location_now(select_game, connect)
    return player_location

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    note_text = data.get('note_text')
    narr_text = data.get('narr_text')
    print(note_text)
    print(narr_text)
    save_game(note_text, narr_text, thisgame.id,db_connection)
    return jsonify({'status': 'success'}), 200

@app.route('/load')
def load():
    save_data = load_game(thisgame.id, db_connection)
    print (save_data)
    return jsonify(save_data)


@app.route('/accuse/', methods=['POST'])
def accuse():
    data = request.get_json()
    print(data)
    suspect = data.get('suspect')
    weapon = data.get('weapon')
    accuse_suspect = check_if_correct_suspect(suspect, db_connection)
    accuse_weapon = check_if_correct_weapon(weapon, db_connection)
    accuse_location = check_if_correct_location(db_connection, thisgame.id)
    print(accuse_suspect)
    print(accuse_weapon)
    print(accuse_location)
    print(suspect)
    print(weapon)
    gethints = Hint(db_connection).generate_hints(weapon, suspect, location_now(thisgame.id, db_connection))
    print(gethints)
    answers_list = [accuse_location, accuse_suspect, accuse_weapon]
    thisgame.right_answer_add(answers_list)
    win_or_not = thisgame.winning()
    print(win_or_not)
    return_thisplz = [win_or_not,gethints]
    print(return_thisplz)
    return jsonify(return_thisplz), 200

@app.route ('/hints/<weapon>/<suspect>/<location>')
def hints(weapon, suspect, location):
    connect = db_connection
    hint_system = Hint(connect)
    gethints = hint_system.generate_hints(weapon, suspect, location)
    return jsonify({
        "game_box": gethints[0],
        "notebook": gethints[1]
    })

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)