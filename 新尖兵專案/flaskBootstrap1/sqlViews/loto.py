from flask import Blueprint,render_template
sqlApp = Blueprint("sql",__name__)

@sqlApp.route('/sqlalchemy')
def loto():
    return render_template('loto.html')