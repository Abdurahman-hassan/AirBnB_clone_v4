#!/usr/bin/python3
""" Provides a simple storage system for managing and persisting
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON response """
    return jsonify({"status": "OK"})
