#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test object creation with arguments
        obj = BaseModel(name='Test', value=42)
        self.assertEqual(obj.name, 'Test')
        self.assertEqual(obj.value, 42)

        # Test object creation without arguments
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel(name='Test', value=42)
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'Test')
        self.assertEqual(obj_dict['value'], 42)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

if __name__ == '__main__':
    unittest.main()
    