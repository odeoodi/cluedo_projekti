def check_money(select_game, connector):
    # Tells the user how much money they have left.
    connect = connector
    sql = f'select money from game where id = %s'
    cursor = connect.cursor()
    cursor.execute(sql, select_game)
    money = cursor.fetchone()
    money_now = int(money[0])
    return money_now
