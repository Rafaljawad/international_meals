from ast import Return
from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,meal



@app.route("/")
def show_page():
    return render_template("main_page.html")

#register
@app.route('/register',methods=['POST','GET'])
def user_sign_up():
    if request.method=="GET":
        return render_template("sign_up.html")
    else:
    #first check if create method came false so redirct to route / which has the form with flash messaeges
        if not user.User.create_new_user(request.form):
            return render_template('sign_up.html')
        else:# if create user function came true so will redirect to route that displays user on profile
            return redirect('/sign_in')

#login route
@app.route('/sign_in',methods=['POST','GET'])
def log_in():
    if request.method=="GET":
        return render_template("sign_in.html")
    else:
        if user.User.login(request.form):
            return redirect('/show_all_meals')
        #otherwise
        return render_template("sign_in.html")

@app.route('/sign_out')
def log_out():
    session.clear()#it will clear user_id from session
    return redirect('/')
