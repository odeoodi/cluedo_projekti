import random
import mysql.connector
import mysql
from app import thisgame
from codes.check_if_correct import check_if_correct_weapon, check_if_correct_suspect, check_if_correct_location
from database_connector import db_connection
from codes.get_from_sql import from_sql_suspects, from_sql_weapons

'''
EI OLE VIELÄ VALMIS
'''
class Hint:
    def __init__(self, connector):
        self.db_connection = connector

    def get_location_feedback(self, location_accusation):
        """
        Check if the location accusation is correct.
        """
        if check_if_correct_location(connector=self.db_connection,game_id=thisgame.id):
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
            clue = self.get_random_hint()

        # Combine feedback and optionally include a clue
        return (
            f"{weapon_feedback.capitalize()} {suspect_feedback.capitalize()} {location_feedback}"
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

        sql1 = f"SELECT id, attribute1, attribute2 FROM weapons WHERE weapon = %s"
        cursor.execute(sql1, (weapon_accusation,))
        accused_weapon = cursor.fetchone()
        is_correct_weapon = check_if_correct_weapon(weapon_accusation, connector=self.db_connection)

        if not accused_weapon:
            return f"No weapon named {weapon_accusation} exists in the database."

        accusation_id, accused_attr1, accused_attr2 = accused_weapon

        if is_correct_weapon:
            return f"Correct! {weapon_accusation} is the murder weapon."

        # Fetch attributes of the correct weapon
        sql2 = f"SELECT weapons.attribute1, weapons.attribute2 FROM weapons INNER JOIN right_answers ON weapons.id = right_answers.id_weapons"
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
                    f"HINT: {weapon_accusation} is not the murder weapon, but it shares the attribute: '{revealed_attribute.capitalize()}'. "
                    f"with the correct weapon."
                )

        return f"{weapon_accusation} is not the murder weapon, it shares no attributes with the correct weapon."

    def get_suspect_feedback(self, suspect_accusation):
        """
        Check if the suspect accusation is correct. If incorrect, compare attributes.
        """
        cursor = self.db_connection.cursor()

        # Fetch the accused suspect's ID and attributes
        sql1 = f"SELECT suspects.id, suspects.sex, suspects.age, suspects.glasses FROM suspects WHERE names = %s"
        cursor.execute(sql1, (suspect_accusation,))
        accused_suspect = cursor.fetchall()[0]
        accused_sex = accused_suspect[0]
        accused_age = accused_suspect[1]
        accused_glasses = accused_suspect[2]
        is_correct_suspect = check_if_correct_suspect(suspect_accusation,connector=self.db_connection)

        if not accused_suspect:
            return f"No suspect named {suspect_accusation} exists in the database."

        accusation_id, accused_sex, accused_age, accused_glasses = accused_suspect

        if is_correct_suspect:
            return f"Correct! {suspect_accusation} is the murderer."

        # Fetch attributes of the correct suspect
        sql2 = f"SELECT suspects.sex, suspects.age, suspects.glasses FROM suspects WHERE id = (SELECT id_suspects FROM right_answers)"
        cursor.execute(sql2)
        correct_attributes = cursor.fetchall()[0]

        matching_attributes = []
        if correct_attributes:
            correct_sex, correct_age, correct_glasses = correct_attributes
            if correct_sex == accused_sex:
                matching_attributes.append(accused_sex)
            if correct_age == accused_age:
                matching_attributes.append(accused_age)
            if correct_glasses == accused_glasses:
                if correct_glasses == 'true':
                    matching_attributes.append(accused_glasses)


            if matching_attributes:
                revealed_attribute = random.choice(matching_attributes)
                if revealed_attribute == accused_glasses:
                    revealed_attribute = 'has glasses'
                return (
                    f"{suspect_accusation} is not the murderer, but they share the attribute: '{revealed_attribute}' "
                    f"with the real suspect."
                )

        return f"{suspect_accusation} is not the murderer. They have no matching attributes with the real suspect."

    def get_random_hint(self):
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
        sql = "SELECT weapons.attribute1, weapons.attribute2 FROM weapons WHERE id = (SELECT id_weapons FROM right_answers)"
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
        sql = "SELECT suspects.sex, suspects.age, suspects.glasses FROM suspects WHERE id = (SELECT id_suspects FROM right_answers)"
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

        return feedback

# Assuming you have a SQLite database called "game.db"
#db_connection = db_connection

# Initialize the Hint class
'''
hint_system = Hint() # täällä oli parametrina db_connection

# Example accusations

weapon_accusation_test = "Knife"  # Player's accused weapon
suspect_accusation_test = "Iida"  # Player's accused suspect
location_accusation_test = "Tenerife Sur Airport"

# Call the hint_or_no_hint method to evaluate accusations and possibly give a clue
result = hint_system.hint_or_no_hint(weapon_accusation_test, suspect_accusation_test, location_accusation_test)

# Display the result to the player
print(result)

# Close the database connection when done
#db_connection.close()
'''