def if_winning(dice1,dice2,dice3):
        if dice1 == 6 and dice2 == 6 or (dice3 == 6 and dice2 == 6 or(dice1 == 6 and dice3 == 6 )):
            wintext = "You have two sixes, you are winning 250€"
            winpoint = 3
            return winpoint, wintext
        elif dice1 == 5 and dice2 == 5 or (dice3 == 5 and dice2 == 5 or(dice1 == 5 and dice3 == 5 )):
            wintext = "You have 2 times 5, you are winning 100€ "
            winpoint = 1
            return winpoint, wintext
        elif dice1 == 5 or dice2 == 5 or dice3 == 5 or dice1 == 6 or dice2 == 6 or dice3 == 6:
            wintext = "You have at least one six or one five you are winning 150€ "
            winpoint = 2
            return winpoint, wintext
        else:
            wintext = f"You have nothing..."
            winpoint = 0
            return winpoint, wintext

def pay(cost, select_game, connection):
    connect = connection
    loose = f'UPDATE game SET money = money- %s WHERE id = %s'
    cursor = connect.cursor()
    cursor.execute(loose, (cost, select_game))
    connect.commit()
    return {"status": "ok"}, 200

def add_money(added,select_game, connection):
    connect = connection
    money = f'UPDATE game SET money = money+ %s WHERE id = %s'
    cursor = connect.cursor()
    cursor.execute(money, (added, select_game))
    connect.commit()
    return 'ok'
