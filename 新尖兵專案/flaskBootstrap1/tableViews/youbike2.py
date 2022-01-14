from flask import Blueprint,render_template

youbikeApp = Blueprint('youbike',__name__)

@youbikeApp.route('/table/youbike')
def youbike():
    return render_template('youbike.html')