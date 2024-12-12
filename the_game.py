from codes.config import game_id
import codes.config

class Game:
    right_answers_num = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.money_neede = codes.config.gamble_cost

    def right_answer_add(self, list):
        Game.right_answers_num = 0
        for i in list:
            if i:
                Game.right_answers_num += 1
        return Game.right_answers_num

    def checkmony(self, connector):
        connect = connector
        game_id = self.id
        sql = f'select money from game where id = "{game_id}"'
        cursor = connect.cursor()
        cursor.execute(sql)
        money = cursor.fetchone()
        money_now = int(money[0])
        return money_now

    def losing(self, connector):
        needed = self.money_neede
        connect = connector
        current_money = self.checkmony(connect)
        if current_money < needed:
            return True
        else:
            return False

    def winning(self):
        if Game.right_answers_num == 3:
            return True
        else:
            return False