from flask import Blueprint
sqlApp = Blueprint("sql",__name__)

@sqlApp.route('/sqlalchemy')
def loto():
    return "<h1>SQLALCHEMY</h1>"