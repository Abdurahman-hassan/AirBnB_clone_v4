#!/usr/bin/python3

"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from uuid import uuid4

app = Flask(__name__)


@app.route("/2-hbnb/", strict_slashes=False)
def hbnb():
    """
    Route to display HBNB data.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    cache_id = str(uuid4())

    return render_template(
        "2-hbnb.html",
        states=states,
        amenities=amenities,
        places=places,
        cache_id=cache_id
    )


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
