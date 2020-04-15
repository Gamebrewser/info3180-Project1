#-----Student of The University of The West Indies, Mona Campus - ID number:620099854-----

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

app = Flask(__name__)
app.config['SECRET_KEY'] = "DontJustReadCodePracticeIt"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/photo'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]


from app import views

