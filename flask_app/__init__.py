from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
app.config["UPLOAD_FOLDER"]="flask_app/static/images"



