from cams import create_app
from flask import Flask

def test_app_creation():
    app = create_app()
    assert app is not None
    assert isinstance(app, Flask)
