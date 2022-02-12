from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


# CREATE model

    @classmethod
    def create_ninjas(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        ;"""
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

# READ model

    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT *
        FROM ninjas;
        ;"""
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # print('LIST OF USERS', result)
        ninjas = []
        for row in result:
            ninjas.append(cls(row))
        # print("ninjas!!!!!!!!!!!", ninjas)
        return ninjas

    @classmethod
    def get_user_by_id(cls, id):
        data = { 'id' : id }
        query="""
        SELECT * 
        FROM ninjas
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print('********', result)

        the_row = result[0]
        print('********', the_row)

        instance_of_ninja = cls(the_row)
        print('********', instance_of_ninja)
        return instance_of_ninja 

# UPDATE model

    @classmethod
    def update_ninja(cls, data):
        query = """
        UPDATE ninjas
        SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id= %(dojo_id)s
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

# DELETE model

    @classmethod
    def delete_ninja(cls,id):
        data = { 'id' : id }
        query = """
        DELETE * FROM ninjascreate
        WHERE id = %(id)s
        ;"""
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)