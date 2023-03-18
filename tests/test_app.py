# test_app.py
from mock import patch
import time
from flaskr.app import app


def test_home_200_response():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data


def test_hello_200_response():
    response = app.test_client().get("/hello")
    assert response.status_code == 200
    assert b"Hello World! from Flask App :)" in response.data


def test_error_route_before_fail_time_expected_200_response():
    with app.test_client() as client:
        # Change the start time to 10 seconds ago
        app.START_TIME = time.time() - 10
        # Make a request to the error route
        response = client.get('/error')
        # Check that the response is a success and contains message
        assert response.status_code == 200
        assert b'Failed will ocurred after 20 seconds' in response.data


@patch('flaskr.app.FAIL_SECONDS_STATE', 0)
def test_error_route_after_fail_time_expected_500_response():
    response = app.test_client().get("/error")
    assert response.status_code == 500
    assert b"Internal Server Error: (HTTP) 500" in response.data
