# app.py
import time
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Home</h1>', 200


@app.route('/hello')
def hello():
    return "Hello World! from Flask App :)", 200


START_TIME = time.time()
FAIL_SECONDS_STATE = 20


@app.route("/error")
def error():
    time_pass = time.time() - START_TIME
    if time_pass < FAIL_SECONDS_STATE:
        return f'''
            <h1>Error</h1>
            <p>Failed will ocurred after {FAIL_SECONDS_STATE} seconds</p>
            <p>Seconds pass {time_pass}</p>
        ''', 200
    else:
        # Internal Server Error
        return 'Internal Server Error: (HTTP) 500', 500
