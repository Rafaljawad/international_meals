from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
app.config["UPLOAD_FOLDER"]="C:/Users/rafal/Videos/python_folder/solo_project/flask_app/static/images"



