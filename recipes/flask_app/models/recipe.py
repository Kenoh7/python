from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            print(row['date_made'])
            recipes.append( cls(row) )
        return recipes

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes(user_id, name, description, instructions, under_30, date_made, created_at,updated_at) VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,%(under_30)s,%(date_made)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def is_validate(recipe):
        is_valid = True
        if len(recipe['name']) < 2:
            is_valid = False
            flash("Recipe name must be at least 2 characters","recipe")
        if len(recipe['instructions']) < 2:
            is_valid = False
            flash("Recipe instructions must be at least 2 characters","recipe")
        if len(recipe['description']) < 2:
            is_valid = False
            flash("Recipe description must be at least 2 characters","recipe")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please input a date","recipe")
        if len(recipe['under_30']) < 2:
            is_valid = False
            flash("Please select Yes or No","recipe")
        return is_valid
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)