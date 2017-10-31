from pymongo import MongoClient
from mongoengine import *
import datetime
import pprint
import unittest
import server.db.user


class UserTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.test_database
        connect('test_user')

    def test_create_user(self):
        user = server.db.user.User(
            email='ross@example.com', first_name='Ross', last_name='Lawley').save()
        self.assertEquals(user.email, 'ross@example.com')
