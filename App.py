from flask import Flask,render_template
from Models.model import *
from sqlalchemy import or_

app=Flask(__name__)

app.config['SECRET_KEY']="EAST"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gs_store.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  #optional

db.init_app(app)


with app.app_context():
    db.create_all()

