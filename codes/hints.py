import random
import mysql.connector
import mysql
from codes.check_if_correct import check_if_correct_weapon, check_if_correct_suspect
from database_connector import db_connection
from codes.get_from_sql import from_sql_suspects, from_sql_weapons

'''
EI OLE VIELÄ VALMIS
'''


class Hint:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def hint_or_no_hint(self, weapon_accusation, suspect_accusation):
        """
        Always returns whether the accusation is correct or not and, by random chance, gives a clue.
        """
        # Get feedback on the accusation
        accusation_result = self.get_accusation_feedback(weapon_accusation, suspect_accusation)

        # Randomly decide if a hint should be provided
        dice = random.randint(1, 10)  # Adjust probability as needed
        if dice <= 2:  # 20% chance to give a hint
            if dice == 1:
                hint = self.get_random_weapon_hint(weapon_accusation)
            else:
                hint = self.get_random_suspect_hint(suspect_accusation)
            return accusation_result + "\n" + hint

        return accusation_result  # No hint provided

    def get_accusation_feedback(self, weapon_accusation, suspect_accusation):
        """
        Checks the correctness of the weapon and suspect accusations.
        """
        weapon_correct = check_if_correct_weapon(weapon_accusation)
        suspect_correct = check_if_correct_suspect(suspect_accusation)

        feedback = []
        if weapon_correct:
            feedback.append(f"Correct! The weapon '{weapon_accusation}' is the murder weapon.")
        else:
            feedback.append(f"Wrong! The weapon '{weapon_accusation}' is not the murder weapon.")

        if suspect_correct:
            feedback.append(f"Correct! '{suspect_accusation}' is the killer.")
        else:
            feedback.append(f"Wrong! '{suspect_accusation}' is not the killer.")

        return "\n".join(feedback)

    def get_random_weapon_hint(self, weapon_accusation):
        """
        Provides a random weapon-related hint using weapon attributes.
        """
        weapons = from_sql_weapons(self.db_connection)
        weapon_correct = check_if_correct_weapon(weapon_accusation)

        if not weapon_correct:
            accused_weapon = next((w for w in weapons if w[0] == weapon_accusation), None)
            if accused_weapon:
                attribute1, attribute2 = accused_weapon[1], accused_weapon[2]
                return (
                    f"Interpol investigated your accusation and found that '{weapon_accusation}' can't be the weapon. "
                    f"No traces of '{attribute1}' or '{attribute2}' were found on the victim. Keep looking!"
                )
            else:
                return f"Interpol couldn't find any details about the weapon '{weapon_accusation}'."
        else:
            random_weapon = random.choice(weapons)
            return (
                f"HINT: Did you know that the weapon '{random_weapon[0]}' has the attributes "
                f"'{random_weapon[1]}' and '{random_weapon[2]}'? It might be useful later!"
            )

    def get_random_suspect_hint(self, suspect_accusation):
        """
        Provides a random suspect-related hint using suspect attributes.
        """
        suspects = from_sql_suspects(self.db_connection)
        suspect_correct = check_if_correct_suspect(suspect_accusation)

        if not suspect_correct:
            accused_suspect = next((s for s in suspects if s[0] == suspect_accusation), None)
            if accused_suspect:
                sex, age, glasses = accused_suspect[1], accused_suspect[2], accused_suspect[3]
                return (
                    f"Interpol investigated your accusation and found that '{suspect_accusation}' can't be the killer. "
                    f"Witnesses described the murderer as someone {'wearing glasses' if glasses else 'not wearing glasses'}, "
                    f"and not '{sex}' aged around '{age}'. Keep searching!"
                )
            else:
                return f"Interpol couldn't find any details about the suspect '{suspect_accusation}'."
        else:
            random_suspect = random.choice(suspects)
            return (
                f"HINT: Did you know that the suspect '{random_suspect[0]}' has the attributes "
                f"sex: '{random_suspect[1]}', age: '{random_suspect[2]}', "
                f"and {'wears glasses' if random_suspect[3] else 'does not wear glasses'}? This might help!"
            )
