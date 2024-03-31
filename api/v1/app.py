#!/usr/bin/python3
""" Main file of the API

This module serves as the main file for the API application, initializing
the Flask application, registering blueprints, and defining teardown
functions for closing the database connection.
"""

from os import getenv
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Close process

    Close the database connection when the application context is torn down.

    Args:
        exception: An optional exception that occurred.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors

    Returns a JSON-formatted 404 status code response with a message.

    Args:
        error: The error that occurred.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = int(getenv('HBNB_API_PORT', default=5000))
    app.run(host=host, port=port, threaded=True)
