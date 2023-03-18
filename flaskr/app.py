# app.py
import time
from flask import Flask
app = Flask(__name__)

start_time = time.time()


@app.route("/")
def home():
    time_pass = time.time() - start_time
    if time_pass < 10:
        return f'''
            <h1>Home</h1>
            <p>Failed will ocurred after 10 seconds</p>
            <p>Seconds pass { time_pass }</p>
        ''', 200
    else:
        # Internal Server Error
        return 'Internal Server Error: (HTTP) 500', 500


@app.route('/hello')
def hello():
    return "Hello World! from Flask App :)", 200
