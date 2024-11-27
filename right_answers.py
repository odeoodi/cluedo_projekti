def insert_right_answers():
# Randomly sets the right answers at the start of the game.
    def random_location():
        sql = f"SELECT id FROM locations ORDER BY RAND() LIMIT 1;"
        kursori=db_connection.cursor()
        kursori.execute(sql)
        result=kursori.fetchone()
        sql2 = f"UPDATE right_answers SET id_locations = {result[0]};"
        kursori.execute(sql2)
        db_connection.commit()
        return result

    def random_weapon():
        sql = f"SELECT id FROM weapons ORDER BY RAND() LIMIT 1"
        kursori=db_connection.cursor()
        kursori.execute(sql)
        result=kursori.fetchone()
        sql2 = f"UPDATE right_answers SET id_weapons = {result[0]};"
        kursori.execute(sql2)
        db_connection.commit()
        return result

    def random_suspect():
        sql = f"SELECT id FROM suspects ORDER BY RAND() LIMIT 1"
        kursori=db_connection.cursor()
        kursori.execute(sql)
        result=kursori.fetchone()
        sql2 = f"UPDATE right_answers SET id_suspects = {result[0]};"
        kursori.execute(sql2)
        db_connection.commit()
        return result
