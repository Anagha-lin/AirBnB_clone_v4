#!/usr/bin/python3
"""Defines views for the Airbnb API."""
from flask import jsonify
from api.v1.views import app_views
from models import storage

# Define a route /status within the app_views blueprint
@app_views.route('/status', strict_slashes=False)
def api_status():
    """Returns a JSON response indicating the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_statistics():
    """
    Retrieves the count of each object type.
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)


if __name__ == "__main__":
    pass
