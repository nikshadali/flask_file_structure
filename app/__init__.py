from flask import Flask
from app.blueprints import home, user
from app.extentions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.register_blueprint(home.home)
app.register_blueprint(user.user)

db.init_app(app)