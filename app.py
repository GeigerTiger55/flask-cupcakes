"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, flash
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()