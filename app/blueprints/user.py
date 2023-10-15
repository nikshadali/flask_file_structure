from flask import Blueprint

user = Blueprint('user',__name__)

@user.route('/users')
def users():
    return "thsi is user page"