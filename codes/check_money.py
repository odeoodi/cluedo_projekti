def check_money(game_id, connector):
    # Tells the user how much money they have left.
    connect = connector
    sql = f'select money from game where id = "{game_id}"'
    cursor = connect.cursor()
    cursor.execute(sql)
    money = cursor.fetchone()
    money_now = int(money[0])
    return money_now

