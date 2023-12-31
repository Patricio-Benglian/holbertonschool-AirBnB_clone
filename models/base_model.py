#!/usr/bin/python3
"""
base_model module
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """
    BaseModel Superclass
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize values
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)

        else:
            storage.new(self)

    def __str__(self):
        """
        returns string representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates updated_at with current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns dictionary with instance attributes
        """
        selfDict = self.__dict__.copy()
        selfDict["__class__"] = self.__class__.__name__
        selfDict['created_at'] = self.created_at.isoformat()
        selfDict['updated_at'] = self.updated_at.isoformat()
        return selfDict
