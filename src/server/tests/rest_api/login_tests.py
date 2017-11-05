import json
import unittest
import time

from server.tests.rest_api.base_test_case import BaseTestCase
from server.db.user import User


class LoginTests(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.init_server()
        self.create_users()

    def tearDown(self):
        self.finalize_server()

    def test_post(self):
        """
        * Test POST /login
        """
        response = self.post('/login')
        self.assertEquals('400 BAD REQUEST', response.status)
        response = self.post('/login',data_dict=dict(email=self.USER_EMAIL, password='dummy'))        
        self.assertEquals('401 UNAUTHORIZED', response.status)
        response = self.post('/login',data_dict=dict(email=self.USER_EMAIL, password=self.USER_PASSWORD))        
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertIsNotNone(data['id'])

    def test_get(self):
        """
        * Test GET /login
        """
        self.login()
        old_id = self.login_id
        time.sleep(1.1) # sleep 1.1 second to change the time stamp of the id
        response = self.get('/login')
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertIsNotNone(data['id'])
        self.assertNotEquals(old_id, data['id'])
        users = User.objects(email=self.USER_EMAIL)
        users[0].delete()
        response = self.get('/login') # Verify that after user deletion, id is not valid anymore
        self.assertEquals('401 UNAUTHORIZED', response.status)
        
