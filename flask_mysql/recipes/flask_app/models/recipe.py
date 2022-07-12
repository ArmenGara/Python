from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint

DATABASE = 'recipes'

class Recipe:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30_minutes = data['under_30_minutes']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO recipes (name,description,date_made) VALUES (%(name)s,%(description)s,%(date_made)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        recipes = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            recipes.append( cls(dictionary) )
            # adding an instance of the recipe class to the recipes list
        return recipes
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM recipes WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! VALIDATIONS
    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True # we assume this is true
        if len(recipe['name']) < 3:
            flash("Tyler! Remember to change this.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Tyler! Remember to change this.")
            is_valid = False
        if len(recipe['date_made']) < 2:
            flash("Tyler! Remember to change this.")
            is_valid = False
        return is_valid