#!/usr/bin/python3
"""Creating a blueprint for the Api."""
from flask import Blueprint

# Creating a Blueprint instance with url prefix /api/v1
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

# import all views from index module
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
