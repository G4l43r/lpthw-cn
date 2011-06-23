from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")

    resp = app.request("/game", method="GET")

    # test that we get expected values
    data = {'action': 'dodge!'}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, status="303")
    
