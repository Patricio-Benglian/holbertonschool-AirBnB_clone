#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class
    """
    state_id = ""  # will be State.id
    name = ""
