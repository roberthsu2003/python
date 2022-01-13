from flask import Blueprint,render_template

tableApp = Blueprint('table_page',__name__)
@tableApp.route('/table')
def table():
    return render_template('table.html',name='table')