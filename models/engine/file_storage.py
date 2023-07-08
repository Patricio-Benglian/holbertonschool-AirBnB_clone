#!/usr/bin/python3
"""
file_storage module
"""
import json


class FileStorage():
    """
    serializes and deserializes json
    """
    __file_path = "file.json"
    __objects = {}  # dict. empty at first

    def all(self):
        """
        returns __objects dict
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets obj with key in __objects
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to JSON file
        """
        jsonDict = {}
        for k, v in FileStorage.__objects.items():
            jsonDict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(jsonDict, f)

    def reload(self):
        """
        deserializes JSON to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                objects = json.load(f)
                for k, v in objects.items():
                    className = eval(v['__class__'])(**v)
                    FileStorage.__objects[k] = className
        except FileNotFoundError:
            pass
