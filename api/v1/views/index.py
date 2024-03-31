#!/usr/bin/python3
""" The basic route of the API """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON response with the status of the API"""
    return jsonify({"status": "OK"})
