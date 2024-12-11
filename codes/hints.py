import random
import mysql.connector
import mysql
from codes.check_if_correct import check_if_correct_weapon, check_if_correct_suspect, check_if_correct_location
from database_connector import db_connection
from codes.get_from_sql import from_sql_suspects, from_sql_weapons

'''
EI OLE VIELÄ VALMIS
'''

class Hint:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_location_feedback(self, location_accusation):
        """
        Check if the location accusation is correct.
        """
        if check_if_correct_location(location_accusation):
            return f"Correct! {location_accusation} is the location where the murder occurred."
        else:
            return f"{location_accusation} is not the correct location of the murder."

    def hint_or_no_hint(self, weapon_accusation, suspect_accusation, location_accusation):
        """
        Always returns whether the accusation is correct or not and, by random chance, gives a clue.
        """
        # Get feedback for each accusation
        weapon_feedback = self.get_weapon_feedback(weapon_accusation)
        suspect_feedback = self.get_suspect_feedback(suspect_accusation)
        location_feedback = self.get_location_feedback(location_accusation)

        # Random chance for a clue
        clue = None
        if random.randint(1, 10) <= 2:  # Adjust chance as needed
            clue = self.get_random_hint(weapon_accusation, suspect_accusation)

        # Combine feedback and optionally include a clue
        return (
            f"{weapon_feedback}\n{suspect_feedback}\n{location_feedback}"
            + (f"\nAdditional clue: {clue}" if clue else "")
        )

    def get_accusation_feedback(self, weapon_accusation, suspect_accusation, location_accusation):
        """
        Get feedback for weapon, suspect, and location accusations.
        """
        return self.hint_or_no_hint(weapon_accusation, suspect_accusation, location_accusation)

    def get_weapon_feedback(self, weapon_accusation):
        """
        Check if the weapon accusation is correct. If incorrect, compare attributes.
        """
        cursor = self.db_connection.cursor()

        # Fetch the accused weapon's ID and attributes
        sql1 = f"SELECT id, attribute1, attribute2 FROM weapons WHERE weapon = ?"
        cursor.execute(sql1, (weapon_accusation,))
        accused_weapon = cursor.fetchone()
        is_correct_weapon = check_if_correct_weapon(weapon_accusation)

        if not accused_weapon:
            return f"No weapon named {weapon_accusation} exists in the database."

        accusation_id, accused_attr1, accused_attr2 = accused_weapon

        if is_correct_weapon:
            return f"Correct! {weapon_accusation} is the murder weapon."

        # Fetch attributes of the correct weapon
        sql2 = f"SELECT attribute1, attribute2 FROM weapons WHERE id = (SELECT id_weapons FROM right_answers)"
        cursor.execute(sql2)
        correct_attributes = cursor.fetchone()

        if correct_attributes:
            correct_attr1, correct_attr2 = correct_attributes
            matching_attributes = [
                attr for attr in [accused_attr1, accused_attr2]
                if attr in [correct_attr1, correct_attr2]
            ]

            if matching_attributes:
                revealed_attribute = random.choice(matching_attributes)
                return (
                    f"HINT: {weapon_accusation} is not the murder weapon, but it shares the attribute: '{revealed_attribute}' "
                    f"with the correct weapon."
                )

        return f"{weapon_accusation} is not the murder weapon. It shares no attributes with the correct weapon."

    def get_suspect_feedback(self, suspect_accusation):
        """
        Check if the suspect accusation is correct. If incorrect, compare attributes.
        """
        cursor = self.db_connection.cursor()

        # Fetch the accused suspect's ID and attributes
        sql1 = f"SELECT id, sex, age, glasses FROM suspects WHERE names = ?"
        cursor.execute(sql1, (suspect_accusation,))
        accused_suspect = cursor.fetchone()
        is_correct_suspect = check_if_correct_suspect(suspect_accusation)

        if not accused_suspect:
            return f"No suspect named {suspect_accusation} exists in the database."

        accusation_id, accused_sex, accused_age, accused_glasses = accused_suspect

        if is_correct_suspect:
            return f"Correct! {suspect_accusation} is the murderer."

        # Fetch attributes of the correct suspect
        sql2 = f"SELECT sex, age, glasses FROM suspects WHERE id = (SELECT id_suspects FROM right_answers)"
        cursor.execute(sql2)
        correct_attributes = cursor.fetchone()

        if correct_attributes:
            correct_sex, correct_age, correct_glasses = correct_attributes
            matching_attributes = [
                attr for attr in ["sex", "age", "glasses"]
                if locals()[f"accused_{attr}"] == locals()[f"correct_{attr}"]
            ]

            if matching_attributes:
                revealed_attribute = random.choice(matching_attributes)
                return (
                    f"{suspect_accusation} is not the murderer, but they share the attribute: '{revealed_attribute}' "
                    f"with the real suspect."
                )

        return f"{suspect_accusation} is not the murderer. They have no matching attributes with the real suspect."

    def get_random_hint(self, weapon_accusation, suspect_accusation):
        """
        Provides a random hint about either a weapon or a suspect.
        """
        if random.choice([True, False]):
            return self.get_random_weapon_hint()
        else:
            return self.get_random_suspect_hint()

    def get_random_weapon_hint(self):
        """
        Provide a hint by revealing an attribute of the correct weapon.
        """
        cursor = self.db_connection.cursor()

        # Fetch the correct weapon's attributes
        sql = "SELECT attribute1, attribute2 FROM weapons WHERE id = (SELECT id_weapons FROM right_answers)"
        cursor.execute(sql)
        attributes = cursor.fetchone()

        if attributes:
            return f"The correct weapon is associated with the attribute '{random.choice(attributes)}'."
        return "No hints available for the correct weapon."

    def get_random_suspect_hint(self):
        """
        Provide a hint by revealing an attribute of the correct suspect.
        """
        cursor = self.db_connection.cursor()

        # Fetch the correct suspect's attributes
        sql = "SELECT sex, age, glasses FROM suspects WHERE id = (SELECT id_suspects FROM right_answers)"
        cursor.execute(sql)
        attributes = cursor.fetchone()

        if attributes:
            attribute_names = ["sex", "age", "glasses"]
            attribute_hint = random.choice([
                f"{name}: {value}" for name, value in zip(attribute_names, attributes)
            ])
            return f"The murderer has the following attribute: '{attribute_hint}'."
        return "No hints available for the murderer."

    def generate_hints(self, weapon, suspect, location):
        """
        Generate hints for the weapon, suspect, and location.
        Returns a list with two paragraphs:
        1. Text for the game box.
        2. Text for the notebook.
        """
        feedback = self.get_accusation_feedback(weapon, suspect, location)

        game_box_text = f"Game Box:\n{feedback}"
        notebook_text = (
            f"Notebook Entry:\nWeapon: {weapon}\nSuspect: {suspect}\nLocation: {location}"
        )

        return [game_box_text.strip(), notebook_text.strip()]

# Assuming you have a SQLite database called "game.db"
db_connection = db_connection

# Initialize the Hint class
hint_system = Hint(db_connection)

# Example accusations
weapon_accusation = "Knife"  # Player's accused weapon
suspect_accusation = "Iida"  # Player's accused suspect

# Call the hint_or_no_hint method to evaluate accusations and possibly give a clue
result = hint_system.hint_or_no_hint(weapon_accusation, suspect_accusation, location_accusation)

# Display the result to the player
print(result)

# Close the database connection when done
db_connection.close()
