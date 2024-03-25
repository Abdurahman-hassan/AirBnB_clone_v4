#!/usr/bin/python3

"""
Starts a Flask web application
"""

from flask import Flask, render_template

from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route to display HBNB data.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")

    return render_template(
        "100-hbnb.html",
        states=states,
        amenities=amenities,
        places=places
    )


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
