#!/usr/bin/python3

""" States API endpoints """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def get_states():
    """ Retrieves the list of all State objects """
    all_states = storage.all(State).values()
    states_list = []
    for state in all_states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(State.to_dict(state))


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Creates a State """
    if request.is_json:
        json_data = request.get_json()
        if "name" in json_data:
            new_state = State(**json_data)
            storage.new(new_state)
            storage.save()
            return jsonify(new_state.to_dict()), 201
        else:
            abort(400, "Missing name")
    else:
        abort(400, "Not a JSON")


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if request.is_json:
        json_data = request.get_json()
        for key, value in json_data.items():
            if key == "id" or key == "created_at" or key == "updated_at":
                continue
            setattr(state, key, value)
        storage.save()
        return jsonify(State.to_dict(state)), 200
    else:
        abort(400, "Not a JSON")
