from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash,session
from flask_app.models import user



class Meal:
    DB='international_meals'

    def __init__(self, data):
        self.id = data['id']
        self.meal_name = data['meal_name']
        self.origin = data['origin']
        self.recipe = data['recipe']
        self.direction = data['direction']
        self.calories_num = data['calories_num']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id=data['user_id']
        self.creator=None#this for create instance of user

    # #READ____MODEL____SQL
    #get show by id
    @classmethod
    def get_meal_by_id(cls,id):
        data={'id':id}
        query="""SELECT * FROM meals WHERE id=%(id)s
        ;"""
        result=connectToMySQL(cls.DB).query_db(query,data)
        if result:
            result=cls(result[0])
        return result


    #get all meals from db 
    @classmethod
    def get_all_meals(cls):
        query="""
        SELECT * FROM meals
        JOIN users
        ON meals.user_id=users.id
        ;"""
        result=connectToMySQL(cls.DB).query_db(query)
        print("//////////////////",result)#this will give me list of dictionary which has all users info and their adventurs
        meals_list=[]#create empty list to append all adventures and users info to it
        if not result:
            return result
        for this_meal in result:
            print(this_meal)
            new_meal=cls(this_meal)#create instance of reports and it will ignor user thats why we need to create dictionary for users table info
            user_data={
                'id':this_meal['users.id'],
                'first_name':this_meal['first_name'],
                'last_name':this_meal['last_name'],
                'email':this_meal['email'],
                'password':this_meal['password'],
                'created_at':this_meal['users.created_at'],
                'updated_at':this_meal['users.updated_at'],
            }
            new_meal.creator=user.User(user_data)#go to user class and pass users data to get instance of user and save it into new_show.creator
            meals_list.append(new_meal)
        print(meals_list)
        return meals_list



    #CREATE____MODEL____SQL
    @classmethod
    def create_meal(cls,data):
        if not cls.validate_meal(data):
            return False
        else:
            query="""
            INSERT INTO meals (meal_name,origin,recipe,direction,calories_num,image,user_id)
            VALUES (%(meal_name)s,%(origin)s,%(recipe)s,%(direction)s,%(calories_num)s,%(image)s,%(user_id)s)
            ;"""
            result=connectToMySQL(cls.DB).query_db(query,data)
            print("############## create query result",result)
            return result


    #UPDATE____MODEL____SQL
    @classmethod
    def update_meal_by_id(cls,data):
        if not cls.validate_meal(data):
            return False
        query="""
        UPDATE meals SET meal_name=%(meal_name)s,origin=%(origin)s,recipe=%(recipe)s,direction=%(direction)s,calories_num=%(calories_num)s
        WHERE id=%(id)s
        ;"""
        result= connectToMySQL(cls.DB).query_db(query,data)
        print("5555555555555555",result)
        return result

    #DELETE____MODEL____SQL
    @classmethod
    def delete_meal(cls,id):
        data={ 'id':id}
        query="""
        DELETE FROM meals WHERE id=%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db(query,data)


    #static method for VALIDATEING meals
    @staticmethod
    def validate_meal(data):
        is_valid=True
        if len(data['meal_name']) < 3:
            flash("meal name must be at least 3 or more characters.")
            is_valid = False
        if len(data['origin']) <2:
            flash("origin must at least 2 or more characters")
            is_valid=False
        if len(data['recipe']) <3:
            flash("recipe feiled must at least 3 or more characters")
            is_valid=False
        if len(data['direction']) <3:
            flash("direction must at least 3 or more characters")
            is_valid=False
        if len(data['calories_num']) <3:
            flash("calories_num  must at least 3 or more characters")
            is_valid=False
        return is_valid