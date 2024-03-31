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
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON response with the status of the API

    Handler for the '/status' endpoint.

    Returns:
        Response: A JSON response containing the status of the API with
        HTTP status code 200 (OK).
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieve statistics of all classes in the database.

    This function calculates and returns the number of objects for each class
    (User, Place, State, City, Amenity, Review) present in the database.

    Returns:
        Response: A JSON response containing the statistics of each class
        with HTTP status code 200 (OK).
    """
    classes = {"users": "User", "places": "Place", "states": "State",
               "cities": "City", "amenities": "Amenity", "reviews": "Review"}

    classes_stats = {}

    for key, cls in classes.items():
        classes_stats[key] = storage.count(cls)

    return jsonify(classes_stats)
