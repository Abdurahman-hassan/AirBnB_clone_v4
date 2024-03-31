#!/usr/bin/python3
""" Blueprint for API

Defines the Blueprint for API views and imports the endpoint handlers.

This module creates a Flask Blueprint named 'app_views' for organizing and
structuring API endpoints under the '/api/v1' URL prefix. It also imports
the endpoint handlers from the 'index' module within the 'api.v1.views'
package.
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
