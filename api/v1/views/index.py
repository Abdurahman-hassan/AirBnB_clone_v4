#!/usr/bin/python3
"""Defines the basic routes and endpoints for the API.

This module contains the implementation of the basic routes and endpoints
for the API. It includes a route that returns a JSON response with the
status of the API.

Attributes:
    app_views: A Blueprint object for API views.
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON response with the status of the API

    Handler for the '/status' endpoint.

    Returns:
        Response: A JSON response containing the status of the API with
        HTTP status code 200 (OK).
    """
    return jsonify({"status": "OK"})
