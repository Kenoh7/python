from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Task:
    db = "tasks_schema"
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.due_date = data['due_date']
        self.description = data['description']
        self.completed_on = data['completed_on']
        self.completed = data['completed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tasks;"
        results =  connectToMySQL(cls.db).query_db(query)
        tasks = []
        for row in results:
            print(row['due_date'])
            tasks.append( cls(row) )
        return tasks
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO tasks(user_id, name, due_date,description,completed,created_at,updated_at) VALUES (%(user_id)s,%(name)s,%(due_date)s,%(description)s,0, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    

    @staticmethod
    def is_valid(task):
        is_valid = True
        if len(task['name']) < 2:
            is_valid = False
            flash("Task name must be at least 2 characters","task")
        if task['due_date'] == "":
            is_valid = False
            flash("Please input a date","task")
        if len(task['description']) < 2:
            is_valid = False
            flash("Task description must be at least 2 characters","task")
        return is_valid
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM tasks WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE tasks SET name=%(name)s,due_date=%(due_date)s,description=%(description)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update2(cls, data):
        query = "UPDATE tasks SET completed=1, completed_on=NOW(),updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_completed(cls):
        query = "SELECT * FROM tasks JOIN users ON users.id = tasks.user_id WHERE tasks.completed = 1;"
        results =  connectToMySQL(cls.db).query_db(query)
        if results:
            all_tasks = []
            for row in results:
                one_task = cls(row)
                user_data ={
                    **row,
                    "id" : row['users.id'],
                    "created_at" : row['users.created_at'],
                    "updated_at" : row['users.updated_at'],
                }
                one_task.holder = user.User(user_data)
                all_tasks.append(one_task)
            return all_tasks

    @classmethod
    def get_all_incomplete(cls):
        query = "SELECT * FROM tasks JOIN users ON users.id = tasks.user_id WHERE tasks.completed = 0;"
        results =  connectToMySQL(cls.db).query_db(query)
        if results:
            all_tasks = []
            for row in results:
                one_task = cls(row)
                user_data ={
                    **row,
                    "id" : row['users.id'],
                    "created_at" : row['users.created_at'],
                    "updated_at" : row['users.updated_at'],
                }
                one_task.holder = user.User(user_data)
                all_tasks.append(one_task)
            return all_tasks

    @classmethod
    def onetask_to_user(cls,data):
        query = "SELECT * FROM tasks JOIN users ON users.id = user_id WHERE tasks.id = %(id)s;"
        results =  connectToMySQL(cls.db).query_db(query,data)
        if results:
            row = results[0]
            one_task = cls(row)
            user_data = {
                **row,
                "id" : row['users.id'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
            }
            one_task.holder = user.User(user_data)
            return one_task