"""
User tests
"""
import unittest
import uuid
from mongoengine import connect
import server.db.user
import server.tests
class UserTests(unittest.TestCase):
    """
    UserTests
    """
    def setUp(self):
        self.db_name = server.tests.create_db(self.__class__.__name__)

    def tearDown(self):
        server.tests.drop_db(self.db_name)

    def test_create_user(self):
        """
        * Test user creation
        """
        user = server.db.user.User(
            email='john@example.com', first_name='John', last_name='Doo').save()
        self.assertEquals(user.email, 'john@example.com')
        server.db.user.User(email="user1@domain.com").save()
        user_1 = server.db.user.User.objects(email="user1@domain.com")
        self.assertEquals(1, len(user_1))
       
