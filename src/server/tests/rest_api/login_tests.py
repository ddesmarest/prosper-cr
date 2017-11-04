import json
import unittest
from server.tests.rest_api.base_test_case import BaseTestCase


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
        self.assertEquals('401 UNAUTHORIZED', response.status)
        response = self.post(
            '/login', headers=self.create_authentication_header(self.USER_EMAIL, self.USER_PASSWORD))        
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertIsNotNone(data['id'])
