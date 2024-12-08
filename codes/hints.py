import random
import mysql.connector
import mysql
from codes.check_if_correct import check_if_correct_weapon, check_if_correct_suspect
from database_connector import db_connection
from codes.get_from_sql import form_sql_suspects, from_sql_weapons


'''
EI OLE VIELÄ VALMIS
'''

class Hint:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def process_accusations(self, weapon_accusation, suspect_accusation):
        """
        Processes the accusations and always returns if they were correct or not.
        Sometimes, it also provides a random clue (hint).
        """
        weapon_feedback = self.check_weapon_accusation(weapon_accusation)
        suspect_feedback = self.check_suspect_accusation(suspect_accusation)

        # Randomly decide if a clue should be added
        clue = self.hint_or_no_hint(weapon_accusation, suspect_accusation)

        # Combine feedback and clue
        result = f"{weapon_feedback}\n{suspect_feedback}\n{clue}"
        return result

    def check_weapon_accusation(self, weapon_accusation):
        """
        Checks if the weapon accusation is correct and provides feedback.
        """
        correct = check_if_correct_weapon(weapon_accusation)
        correct_accusation = f"Interpol looked further into your claims and discovered evidence backing up your claim. The weapon accusation '{weapon_accusation}' is correct! Well done, detective!"
        false_accusation = f"Interpol looked further into your claims and discovered NO evidence backing up your claim. The weapon accusation '{weapon_accusation}' is incorrect. Keep investigating."
        if correct:
            return correct_accusation
        else:
            return false_accusation

    def check_suspect_accusation(self, suspect_accusation):
        """
        Checks if the suspect accusation is correct and provides feedback.
        """
        correct = check_if_correct_suspect(suspect_accusation)

        if correct:
            return f"The suspect accusation '{suspect_accusation}' is correct! Well done, detective!"
        else:
            return f"The suspect accusation '{suspect_accusation}' is incorrect. Keep investigating."

    def hint_or_no_hint(self, weapon_accusation, suspect_accusation):
        """
        Randomly decides whether to give an additional clue.
        """
        dice = random.randint(1, 10)
        if dice <= 2:  # 20% chance of giving a clue
            if dice == 1:
                return self.get_random_weapon_hint(weapon_accusation)
            elif dice == 2:
                return self.get_random_suspect_hint(suspect_accusation)
        return "No additional clues at this time."

    def get_random_weapon_hint(self, weapon_accusation):
        """
        Provides a random clue about the weapon accusation if incorrect.
        """
        cursor = self.db_connection.cursor()
        correct = check_if_correct_weapon(weapon_accusation)

        if not correct:
            weapons = from_sql_weapons(self.db_connection)


            if weapons:
                attribute = result[0]
                weapon_clue = (
                    f"CLUE: Interpol investigated your accusation and discovered that {weapon_accusation} "
                    f"can't be the murder weapon because no traces of {attribute} were found. "
                    f"Keep searching!"
                )
                return weapon_clue
        return "CLUE: No hints about the weapon right now."

    def get_random_suspect_hint(self, suspect_accusation):
        """
        Provides a random clue about the suspect accusation if incorrect.
        """
        cursor = self.db_connection.cursor()
        correct = check_if_correct_suspect(suspect_accusation)

        if not correct:
            query = f"SELECT sex FROM suspects WHERE names = '{suspect_accusation}'"
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                attribute = result[0]
                return (
                    f"CLUE: Interpol investigated your accusation and discovered that {suspect_accusation} "
                    f"can't be the killer because a witness testified the murderer was not {attribute}. "
                    f"Keep searching!"
                )
        return "CLUE: No hints about the suspect right now."


# Example of how to use the Hint system
# Assuming `db_connection` is a valid database connection
hint_system = Hint(db_connection)

# Example accusations
weapon_accusation = "Knife"
suspect_accusation = "Iida"

# Process accusations and get feedback
result = hint_system.process_accusations(weapon_accusation, suspect_accusation)
print(result)
