def save_game(note_text, narrator_text, game_id, connection):
    connect = connection
    note_save = 'UPDATE notepab_text SET content = %s WHERE id = %s'
    narrator_save = 'UPDATE narrator_text SET content = %s WHERE id = %s'
    cursor = connect.cursor()
    cursor.execute(note_save, (note_text, game_id))
    cursor.execute(narrator_save, (narrator_text, game_id))
    connect.commit()
    return 'saved'

def load_game(game_id, connection):
    connect = connection
    note_load = f'SELECT content FROM notepab_text WHERE id = {game_id}'
    narrator_load = f'SELECT content FROM narrator_text WHERE id = {game_id}'
    name_load = f'SELECT name FROM game WHERE id = {game_id}'
    cursor = connect.cursor()
    cursor.execute(note_load)
    note_text = cursor.fetchall()
    cursor.execute(narrator_load)
    narrator_text = cursor.fetchall()
    cursor.execute(name_load)
    name_load = cursor.fetchall()
    data_to_send = {
        'note_text': note_text,
        'narrator_text': narrator_text,
        'player_name': name_load,
    }
    return data_to_send
