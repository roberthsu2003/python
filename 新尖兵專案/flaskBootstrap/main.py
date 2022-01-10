from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<div style="font-size:2rem;color:red"> Hello! World</div>'