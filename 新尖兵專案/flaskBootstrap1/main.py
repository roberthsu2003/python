from flask import Flask,render_template
from tableViews.table import  tableApp
from tableViews.youbike2 import youbikeApp
from sqlViews.loto import sqlApp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'roberthsu-hero'
app.register_blueprint(tableApp)
app.register_blueprint(youbikeApp)
app.register_blueprint(sqlApp)

@app.errorhandler(404)
def error404(err):
    return render_template('error404.html'),404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
@app.route('/layout/box')
def layout():
    return render_template('layout.html',name='layout')

@app.route('/layout/container')
def container():
    return  render_template('container.html',name="container")

@app.route('/layout/columns')
def columns():
    return render_template('columns.html',name="columns")

@app.route('/price')
def price():
    return render_template('price.html')

