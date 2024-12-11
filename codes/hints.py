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

        # Random chance for a clue
        dice = random.randint(1, 10)
        if dice in [1, 2]:  # Adjust chances as needed
            clue = self.get_random_hint(weapon_accusation, suspect_accusation)
            return f"{accusation_result}\nAdditional clue: {clue}"
        else:
            return accusation_result

    def get_accusation_feedback(self, weapon_accusation, suspect_accusation):
        """
        Check both weapon and suspect accusations.
        """
        weapon_feedback = self.get_weapon_feedback(weapon_accusation)
        suspect_feedback = self.get_suspect_feedback(suspect_accusation)
        return f"{weapon_feedback}\n{suspect_feedback}"

    def get_weapon_feedback(self, weapon_accusation):
        """
        Check if the weapon accusation is correct. If incorrect, compare attributes.
        """
        cursor = self.db_connection.cursor()

        # Fetch the accused weapon's ID
        sql1 = f"SELECT id, attribute1, attribute2 FROM weapons WHERE weapon = '{weapon_accusation}'"
        cursor.execute(sql1)
        accused_weapon = cursor.fetchone()

        if not accused_weapon:
            return f"No weapon named {weapon_accusation} exists in the database."

        accusation_id, accused_attr1, accused_attr2 = accused_weapon

        # Check if the accused weapon is correct
        sql2 = f"SELECT id_weapons FROM right_answers WHERE id_weapons = {accusation_id}"
        cursor.execute(sql2)
        correct_weapon_id = cursor.fetchone()

        if correct_weapon_id:
            return f"Correct! {weapon_accusation} is the murder weapon."

        # Fetch the attributes of the correct weapon
        sql3 = f"SELECT attribute1, attribute2 FROM weapons WHERE id = (SELECT id_weapons FROM right_answers)"
        cursor.execute(sql3)
        correct_attributes = cursor.fetchone()

        correct_attr1, correct_attr2 = correct_attributes

        # Compare attributes
        matching_attributes = []
        if accused_attr1 in [correct_attr1, correct_attr2]:
            matching_attributes.append(accused_attr1)
        if accused_attr2 in [correct_attr1, correct_attr2]:
            matching_attributes.append(accused_attr2)

        if matching_attributes:
            return (
                f"{weapon_accusation} is not the murder weapon, but it shares the following attributes "
                f"with the correct weapon: {', '.join(matching_attributes)}."
            )
        else:
            return f"{weapon_accusation} is not the murder weapon. It shares no attributes with the correct weapon."

    def get_suspect_feedback(self, suspect_accusation):
        """
        Check if the suspect accusation is correct. If incorrect, compare attributes.
        """
        cursor = self.db_connection.cursor()

        # Fetch the accused suspect's ID and attributes
        sql1 = f"SELECT id, sex, age, glasses FROM suspects WHERE names = '{suspect_accusation}'"
        cursor.execute(sql1)
        accused_suspect = cursor.fetchone()

        if not accused_suspect:
            return f"No suspect named {suspect_accusation} exists in the database."

        accusation_id, accused_sex, accused_age, accused_glasses = accused_suspect

        # Check if the accused suspect is correct
        sql2 = f"SELECT id_suspects FROM right_answers WHERE id_suspects = {accusation_id}"
        cursor.execute(sql2)
        correct_suspect_id = cursor.fetchone()

        if correct_suspect_id:
            return f"Correct! {suspect_accusation} is the murderer."

        # Fetch the attributes of the correct suspect
        sql3 = f"SELECT sex, age, glasses FROM suspects WHERE id = (SELECT id_suspects FROM right_answers)"
        cursor.execute(sql3)
        correct_attributes = cursor.fetchone()

        correct_sex, correct_age, correct_glasses = correct_attributes

        # Compare attributes
        matching_attributes = []
        if accused_sex == correct_sex:
            matching_attributes.append("sex")
        if accused_age == correct_age:
            matching_attributes.append("age")
        if accused_glasses == correct_glasses:
            matching_attributes.append("glasses")

        if matching_attributes:
            return (
                f"{suspect_accusation} is not the murderer, but they share the following attributes with the real suspect: "
                f"{', '.join(matching_attributes)}."
            )
        else:
            return f"{suspect_accusation} is not the murderer. They have no matching attributes with the real suspect."

    def get_random_hint(self, weapon_accusation, suspect_accusation):
        """
        Provides a random hint about either a weapon or a suspect.
        """
        if random.choice([True, False]):
            return self.get_random_weapon_hint(weapon_accusation)
        else:
            return self.get_random_suspect_hint(suspect_accusation)

    def get_random_weapon_hint(self, weapon_accusation):
        """
        Provide a hint by revealing an attribute of the correct weapon.
        """
        cursor = self.db_connection.cursor()

        # Get the ID of the accused weapon
        accusation_query = f"SELECT id FROM weapons WHERE weapon = '{weapon_accusation}'"
        cursor.execute(accusation_query)
        accusation_result = cursor.fetchone()

        if not accusation_result:
            return f"No information found for weapon '{weapon_accusation}'."

        accusation_id = accusation_result[0]

        # Get the correct weapon's ID
        correct_weapon_query = "SELECT id_weapons FROM right_answers"
        cursor.execute(correct_weapon_query)
        correct_weapon_result = cursor.fetchone()

        if not correct_weapon_result:
            return "No correct weapon data found for hints."

        correct_weapon_id = correct_weapon_result[0]

        # Fetch the correct weapon's attributes
        correct_weapon_attributes_query = f"SELECT weapon, attribute1, attribute2 FROM weapons WHERE id = {correct_weapon_id}"
        cursor.execute(correct_weapon_attributes_query)
        correct_weapon_data = cursor.fetchone()

        if not correct_weapon_data:
            return "No attributes found for the correct weapon."

        correct_weapon, attribute1, attribute2 = correct_weapon_data

        # Randomly pick one of the correct weapon's attributes to reveal
        attribute = random.choice([attribute1, attribute2])

        return (
            f"The correct weapon is associated with the attribute '{attribute}'. "
            f"Keep this in mind for your investigation!"
        )

    def get_random_suspect_hint(self, suspect_accusation):
        def get_random_suspect_hint(self, suspect_accusation):
            """
            Provide a hint by revealing a random attribute of the murderer.
            """
            cursor = self.db_connection.cursor()

            # First, check if the accusation is correct by checking the correct suspect
            correct = check_if_correct_suspect(suspect_accusation)

            if correct:
                # Fetch the attributes of the murderer
                suspect_query = f"SELECT names, sex, age, glasses FROM suspects WHERE names = '{suspect_accusation}'"
                cursor.execute(suspect_query)
                suspect_data = cursor.fetchone()

                if not suspect_data:
                    return f"No information found for suspect '{suspect_accusation}'."

                name, sex, age, glasses = suspect_data

                # Randomly select one of the suspect's attributes
                random_attribute = random.choice(
                    [f"sex: {sex}", f"age: {age}", f"wears glasses: {glasses}"]
                )

                return (
                    f"Hint: The murderer, {suspect_accusation}, has the following characteristic: {random_attribute}. "
                    f"Keep this in mind as you investigate further!"
                )
            else:
                return f"Your accusation of {suspect_accusation} is incorrect. Keep searching for the murderer!"
