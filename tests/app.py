from moengage.app import App


def test_app():
    assert App().hello() == 'Hello, my col frien'
