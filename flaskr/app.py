# app.py
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Home</h1>'


@app.route('/hello')
def hello():
    return "Hello World! from Flask App :)"
