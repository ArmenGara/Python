from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint

DATABASE = 'thoughts'

class Thought:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.content = data['content']
        self.likes = data['likes']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO thoughts (content,likes,user_id) VALUES (%(content)s,%(likes)s,%(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM thoughts;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        thoughts = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            thoughts.append( cls(dictionary) )
            # adding an instance of the thought class to the thoughts list
        return thoughts

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all_with_user(cls) -> list:
        query = "SELECT users.first_name, thoughts.* FROM thoughts JOIN users ON users.id = thoughts.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        thoughts = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            thoughts.append( cls(dictionary) )
            # adding an instance of the thought class to the thoughts list
        pprint(thoughts[0].first_name)
        return thoughts
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM thoughts WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE thoughts SET likes=likes + 1 WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! UPDATE
    @classmethod
    def downdate(cls,data:dict) -> int:
        query = "UPDATE thoughts SET likes=likes - 1 WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM thoughts WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! VALIDATIONS
    @staticmethod
    def validate_thought(thought:dict) -> bool:
        is_valid = True # we assume this is true
        if len(thought['content']) < 5:
            flash("Tyler! Remember to change this.")
            is_valid = False
        return is_valid