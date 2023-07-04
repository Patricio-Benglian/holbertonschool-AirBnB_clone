#!/usr/bin/python3
"""
base_model module
"""
from uuid import uuid4
from datetime import datetime


# I think it inherits Cmd?
class BaseModel():
    """ BaseModel Superclass """
    def __init__(self):
        """ Initialize values """
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """ returns string representation """
        return f"[{self.__class__}] ({self.id}) <{self.__dict__}>"
    
    def save(self):
        """ Updates updated_at with current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns dictionary with instance attributes """
        return (self().__dict__)
