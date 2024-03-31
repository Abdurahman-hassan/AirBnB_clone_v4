#!/usr/bin/python3
""" Provides a simple storage system for managing and persisting
"""
from flask import Flask

from api.v1.views import app_views
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
HOST = getenv('HBNB_API_HOST', default='0.0.0.0')
PORT = getenv('HBNB_API_PORT', default=5000)


@app.teardown_appcontext
def teardown(exception):
    """teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host=HOST,
            port=PORT,
            threaded=True)
