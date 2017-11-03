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
    def check_password(self, username, password, assert_function):
        user_1 = server.db.user.User.objects(email=username)
        self.assertEquals(1, len(user_1))
        assert_function(user_1[0].check_password(password))
    
    def test_create_user(self):
        """
        * Test user creation
        """
        user = server.db.user.User(email='john@domain.com')
        user.set_password('my_password')
        self.assertTrue(user.check_password('my_password'))
        user.save()
        self.check_password('john@domain.com','my_password',self.assertTrue )
        server.db.user.User(email='user2@domain.com').set_password('test2').save()
        self.check_password('user2@domain.com','test2',self.assertTrue )
        self.check_password('user2@domain.com','wrongpassword',self.assertFalse )
        self.assertFalse(server.db.user.User(email='user3@domain.com').check_password('none'))
