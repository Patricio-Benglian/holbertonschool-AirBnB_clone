#!/usr/bin/python3
"""
review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class
    """
    place_id = ""  # will be Place.id
    user_id = ""  # will be User.id
    text = ""
