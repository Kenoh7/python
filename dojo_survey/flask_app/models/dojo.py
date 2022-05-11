from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.language = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        results = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , location , language, comment, created_at, updated_at ) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW() , NOW() );"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Comment must be at least 10 characters")
            is_valid = False
        return is_valid