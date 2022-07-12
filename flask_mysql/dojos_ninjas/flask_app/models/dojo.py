from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.ninja import Ninja

DATABASE = 'Dojos_Ninjas'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        pprint(results[0])
        dojo = cls(results[0])
        for ninja in results:
            ninja_data = {
            'id': ninja['ninjas.id'],
            'first_name':ninja['first_name'],
            'last_name':ninja['last_name'],
            'age':ninja['age'],
            'dojo_id':ninja['dojo_id'],
            'created_at':ninja['ninjas.created_at'],
            'updated_at':ninja['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        print(dojo.name)
        return dojo

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        dojos = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            dojos.append( cls(dictionary) )
            # adding an instance of the dojo class to the dojos list
        return dojos
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE dojos SET column1=%(column1)s,column2=%(column2)s,column3=%(column3)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)