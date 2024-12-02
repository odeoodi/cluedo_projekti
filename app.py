import json
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
from codes.start import start_money, start_location, start_accusations
import codes.config

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
    return 'OK'



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)