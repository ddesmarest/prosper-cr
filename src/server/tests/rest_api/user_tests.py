import json
import unittest
from server.tests.rest_api.base_test_case import BaseTestCase
from server.db.workspace import Workspace
from server.db.user import User


class WorkspaceAPITests(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.init_server()
        self.create_users()
        self.create_workspaces()

    def tearDown(self):
        self.finalize_server()

    def test_get(self):
        """
        * Test GET /user
        """
        response = self.get('/user')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.get('/user')
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals(self.USER_FIRST_NAME, data['first_name'])
        self.assertEquals(self.USER_LAST_NAME, data['last_name'])
        self.logout()
        response = self.get('/user')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        

    def test_put(self):
        """
        * Test PUT /user
        """
        response = self.put('/user')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.put('/user')
        self.assertEquals('400 BAD REQUEST', response.status)
        response = self.put('/user', data_dict=dict(first_name='New First', last_name='New Last'))
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals('New First', data['first_name'])
        self.assertEquals('New Last', data['last_name'])
