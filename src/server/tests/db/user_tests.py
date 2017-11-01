from pymongo import MongoClient
from mongoengine import *
import datetime
import pprint
import unittest
import server.db.user


class UserTests(unittest.TestCase):
    def setUp(self):
        self.db_ = connect('test_user')

    def tearDown(self):
        self.db_.drop_database('test_user_field_group')

    def test_create_user(self):
        user = server.db.user.User(
            email='john@example.com', first_name='John', last_name='Doo').save()
        self.assertEquals(user.email, 'john@example.com')
        server.db.user.User(email="user1@domain.com").save()
        user_1 = server.db.user.User.objects(email="user1@domain.com")
        self.assertEquals(1, len(user_1))
       
