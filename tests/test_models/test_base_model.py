#!/usr/bin/python3
"""
test module
"""
import sys
import unittest
from models.base_model import BaseModel #doesnt work for some reason

class test_BaseModel(unittest.TestCase):
    """tests"""
    def test_is_instance(self):
        """ Checks if creation works """
        instance = BaseModel()
        print (instance.id())
