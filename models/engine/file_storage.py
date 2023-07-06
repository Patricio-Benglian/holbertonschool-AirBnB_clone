#!/usr/bin/python3
"""
file_storage module
"""
import json


class FileStorage():
    """ serializes and deserializes json """
    __file_path = "file.json"
    __objects = {} # dict. empty at first

    def all(self):
        """ returns __objects dict """
        return FileStorage.__objects

    def new(self, obj):
        """ sets obj with key in __objects """
        key = obj.__class__.__name__ + obj.id
        FileStorage.__objects.append({key: obj})

    def save(self):
        """ serializes __objects to JSON file """
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
           print(f"Save\n======\n{self.__objects}")
            

    def reload(self):
        """ deserializes JSON to __objects """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                
        except FileNotFoundError:
            pass
