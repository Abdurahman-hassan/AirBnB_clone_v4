#!/usr/bin/python3

""" Amenity API endpoints """

from flask import jsonify, abort, request

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False)
def get_amenities():
    """ Retrieves the list of all Amenity objects """
    amenities = storage.all(Amenity).values()
    amenities_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False)
def get_amenity(amenity_id):
    """ Retrieves a specific Amenity object by ID """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(Amenity.to_dict(amenity)), 200


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ Deletes a specific Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """ Creates a new Amenity object """
    if request.is_json:
        json_data = request.get_json()
        if "name" in json_data:
            new_amenity = Amenity(**json_data)
            storage.new(new_amenity)
            storage.save()
            return jsonify(new_amenity.to_dict()), 201
        else:
            abort(400, "Missing name")
    else:
        abort(400, "Not a JSON")


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """Updates a specific Amenity object defined by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if request.is_json:
        json_data = request.get_json()
        for key, value in json_data.items():
            if key == "id" or key == "created_at" or key == "updated_at":
                continue
            setattr(amenity, key, value)
        storage.save()
        return jsonify(Amenity.to_dict(amenity)), 200
    else:
        abort(400, "Not a JSON")
