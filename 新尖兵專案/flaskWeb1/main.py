from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello! World</h1>"