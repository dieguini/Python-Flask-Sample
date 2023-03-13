# test_app.py
from flaskr.app import app


def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data


def test_hello():
    response = app.test_client().get("/hello")
    assert response.status_code == 200
    assert b"Hello World! from Flask App :)" in response.data
