import random
import mysql.connector
import mysql

'''
EI OLE VIELÄ VALMIS
'''

class Hint:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def hint_or_no_hint(self, weapon_accusation, suspect_accusation):
        dice = random.randint(1, 10)
        if dice == 1:
            result = self.get_random_weapon_hint(weapon_accusation)
        elif dice == 2:
            result = self.get_random_suspect_hint(suspect_accusation)
        else:
            result = "No hints"
        return result

    def get_random_weapon_hint(self, weapon_accusation):
        cursor = self.db_connection.cursor()
        correct = check_if_correct_weapon(weapon_accusation)
        if not correct:
            # aseen atribuuttii tsekkaa makelta
            query = f"SELECT attribute1 FROM weapons WHERE weapon = '{weapon_accusation}'"
            cursor.execute(query)
            result = cursor.fetchone()
            momo = str(
                f"Interpol couldn't find evidence supporting your accusation of {weapon_accusation}. Try a different approach.")

            if result:
                # pitää varmasti ottaa indeksi kysy make
                attribute = result[0]
                return (
                    f"Interpol investigated your accusations and discovered the weapon can't "
                    f"be {weapon_accusation}, because no traces of {attribute} were found on the body. "
                    f"Keep looking, detective."
                )
            else:
                return momo
        else:
            return (
                f"Interpol looked further into your accusation and found evidence backing up "
                f"your claim that {weapon_accusation} is the murder weapon. Well done, detective!"
            )

    def get_random_suspect_hint(self, suspect_accusation):
        cursor = self.db_connection.cursor()
        correct = check_if_correct_suspect(suspect_accusation)
        if not correct:
            # epäillyn atribuuttii tsekkaa makelta
            query = f"SELECT sex FROM suspects WHERE names = '{suspect_accusation}'"
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                # pitää varmasti ottaa indeksi kysy make
                attribute = result[0]
                return (
                    f"Interpol investigated your accusations and discovered the killer can't "
                    f"be {suspect_accusation}, because a witness came forward and testified the murderer not to be {attribute} "
                    f"Keep looking, detective."
                )
            else:
                return (
                    f"Interpol couldn't find evidence supporting your accusation of {suspect_accusation}. "
                    f"Try a different approach."
                )
        else:
            return (
                f"Interpol looked further into your accusation and found evidence backing up "
                f"your claim that {suspect_accusation} is the killer! Well done, detective!"
            )
