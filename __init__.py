from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')

#DB
db = SQLAlchemy(app)
db.create_all()

from blog import views
from author import views

# MVC Explaination

# Model - DB Ops
# Controllers - views.py
# View - Templates

