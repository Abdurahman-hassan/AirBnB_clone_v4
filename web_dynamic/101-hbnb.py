#!/usr/bin/python3

"""
Starts a Flask web application
"""

from uuid import uuid4

from flask import Flask, render_template

from models import storage

app = Flask(__name__)


@app.route("/101-hbnb/", strict_slashes=False)
def hbnb():
    """
    Route to display HBNB data.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    cache_id = str(uuid4())
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    reviews = storage.all("Review")

    return render_template(
        "101-hbnb.html",
        states=states,
        amenities=amenities,
        places=places,
        cache_id=cache_id,
        users=users,
        reviews=reviews
    )


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
