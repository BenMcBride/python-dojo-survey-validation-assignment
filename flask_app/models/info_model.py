from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash

class Info:
    DB = "dojo_survey_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.dojo_location = data['dojo_location']
        self.fav_language = data['fav_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ): 
        query = """
            INSERT INTO infos ( name, dojo_location, fav_language, comment, created_at, updated_at ) 
            VALUES ( %(name)s, %(dojo_location)s, %(fav_language)s, %(comment)s, NOW(), NOW() );
            """
        result = connectToMySQL(cls.DB).query_db( query, data )
        return result
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * 
            FROM infos;
            """
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        infos = []
        for i in results:
            infos.append(cls(i))
        return infos

    @staticmethod
    def validate_info(info):
        is_valid = True
        if len(info['name']) <= 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(info['dojo_location']) == 0:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(info['fav_language']) == 0:
            is_valid = False
            flash("Must choose a favorite language.")
        return is_valid