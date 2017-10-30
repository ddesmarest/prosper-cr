from pymongo import MongoClient
import datetime
import pprint
import unittest
import server.db.user
class UserTests(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.test_database
    def test_create_user(self):
        users = self.db.users
        user = server.db.user.User( 'David', users )
        print user.get_name()

