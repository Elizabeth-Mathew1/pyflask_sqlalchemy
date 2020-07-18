from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key='TRUE')
    name = db.Column(db.String(50))
    tag = db.Column(db.String(50))