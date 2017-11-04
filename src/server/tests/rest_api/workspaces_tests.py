import json
import unittest
from server.tests.rest_api.base_test_case import BaseTestCase


class WorkspacesTests(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.init_server()
        self.create_users()
        self.create_workspaces()

    def tearDown(self):
        self.finalize_server()

    def test_get(self):
        """
        * Test GET /workspaces
        """
        response = self.get('/workspaces')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.get('/workspaces')
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals(1, len(data))
        self.assertEquals('Workspace for user 1', data[0]['name'])
        self.logout()
        response = self.get('/workspaces')
        self.assertEquals('401 UNAUTHORIZED', response.status)

    def test_post(self):
        """
        * Test POST /workspaces
        """
        response = self.post('/workspaces')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.post('/workspaces', data_dict = dict(name='New Workspace'))
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals('New Workspace', data['name'])
        self.assertIsNotNone(data['id'])
        self.assertNotEquals('', data['id'])
        response = self.get('/workspaces')
        data = json.loads(response.data)
        self.assertEquals('200 OK', response.status)
        self.assertEquals(2, len(data))
