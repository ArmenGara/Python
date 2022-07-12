from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint


DATABASE = 'magazines'

class Magazine:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.user_id = data['user_id']
        if "first_name" in data:
            self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO magazines (name,description,user_id) VALUES (%(name)s,%(description)s,%(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM magazines;"
        results = connectToMySQL(DATABASE).query_db(query)
        magazines = []
        for dictionary in results:
            magazines.append( cls(dictionary) )
        return magazines
    
        # ! READ/RETRIEVE ALL
    @classmethod
    def get_all_with_user(cls) -> list:
        query = "SELECT users.first_name, magazines.* FROM magazines LEFT JOIN users ON users.id = magazines.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        magazines = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            magazines.append( cls(dictionary) )
        return magazines

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM magazines WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE magazines SET name=%(name)s,description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! VALIDATIONS
    @staticmethod
    def validate_magazine(magazine:dict) -> bool:
        is_valid = True # we assume this is true
        if len(magazine['name']) < 3:
            flash("Name! Has to be 3 characters long.")
            is_valid = False
        if len(magazine['description']) < 8:
            flash("Description! Has to be 8 characters long.")
            is_valid = False
        return is_valid
