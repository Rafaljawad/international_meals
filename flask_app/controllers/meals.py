

from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,meal
import os
from werkzeug.utils import secure_filename

@app.route("/show_all_meals")
def show_all_meals():
    all_meals=meal.Meal.get_all_meals()
    return render_template("all_meal.html",all_meals=all_meals)


# ADD MEAL ---------CONTROLLER

@app.route("/add/meal",methods=["POST","GET"])
def add_meall_to_user():
    if request.method=="GET":
        if 'user_id' not in session:
            return redirect("/sign_in")
        else:
            return render_template("add_meal.html")
    else:
        if('image' not in request.files or request.files['image'].filename==""):
            flash("please Insert an image")
            return redirect("/add/meal")
        image=request.files['image']
        filename=secure_filename(image.filename)
        print(filename)
        print(app.config["UPLOAD_FOLDER"])
        # basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))


        data={
            "meal_name" : request.form['meal_name'],
            "origin" :request.form['origin'],
            "recipe": request.form['recipe'],
            "direction": request.form['direction'],
            "calories_num": request.form['calories_num'],
            "image" :os.path.join("/static/images",filename),
            "user_id":request.form['user_id']
        }
        if  meal.Meal.create_meal(data):
            return redirect("/show_all_meals")
        else:
            return render_template("add_meal.html")



# sHOW MEAL ---------CONTROLLER
@app.route("/show/meal/<int:id>")
def show_single_meal(id):
    this_meal=meal.Meal.get_meal_by_id(id)
    return render_template("show_meal.html",this_meal=this_meal)




# EDIT  MEAL ---------CONTROLLER
@app.route("/edit/meal/<int:id>",methods=['POST','GET'])
def edit_meal(id):
    if request.method=="GET":
        if 'user_id' not in session:
            return redirect("/")
        else:
            this_meal=meal.Meal.get_meal_by_id(id)
            return render_template("edit_meal.html",this_meal=this_meal)

    else:
        if 'user_id' not in session:
            return redirect("/")
        else:
            meal_data={
            'id':id,
            'meal_name':request.form['meal_name'],
            'origin':request.form['origin'],
            'recipe':request.form['recipe'],
            'direction': request.form['direction'],
            'calories_num': request.form['calories_num']
        }
        if meal.Meal.update_meal_by_id(meal_data)==None:
            return redirect('/show_all_meals')
        else:
            this_meal=meal.Meal.get_meal_by_id(id)
            return render_template('edit_meal.html',this_meal=this_meal)







# DELETE MEAL ---------CONTROLLER
@app.route("/delete/meal/<int:id>")
def destroy_meal(id):
    if 'user_id' not in session:
            return redirect("/")
    else:
        filename=meal.Meal.get_meal_by_id(id).image.replace("/static/images\\","")
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        meal.Meal.delete_meal(id)
        return redirect('/show_all_meals')
