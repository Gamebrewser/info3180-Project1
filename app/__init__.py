#-----Student of The University of The West Indies, Mona Campus - ID number:620099854-----

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

app = Flask(__name__)
app.config['SECRET_KEY'] = "DontJustReadCodePracticeIt"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://blgcankvcgkgrj:5065cba8db3d49bb0c54e661f8bb1a9ee3c7d1dd0fc96b8b37d0ca2e384491e2@ec2-34-193-232-231.compute-1.amazonaws.com:5432/d204ebphoaom41"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/photo'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]


from app import views

