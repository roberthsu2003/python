from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name/')
def name():
    return "<h1>RobertHsu</h1>"