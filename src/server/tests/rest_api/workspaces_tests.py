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
        response = self.app.get('/workspaces')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        response = self.app.get(
            '/workspaces', headers=self.create_authentication_header(self.USER_EMAIL, self.USER_PASSWORD))
        data = json.loads(response.data)
        self.assertEquals('200 OK', response.status)
        self.assertEquals(1, len(data))
        self.assertEquals('Workspace for user 1', data[0]['name'])

    def test_post(self):
        """
        * Test POST /workspaces
        """
        response = self.app.post('/workspaces')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        header = self.create_authentication_header(
            self.USER_EMAIL, self.USER_PASSWORD)
        response = self.app.post(
            '/workspaces', headers=header,
            data=json.dumps(dict(name='New Workspace')),
            content_type='application/json')
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals('New Workspace', data['name'])
        self.assertIsNotNone(data['id'])
        self.assertNotEquals('', data['id'])
        response = self.app.get('/workspaces', headers=header)
        data = json.loads(response.data)
        self.assertEquals('200 OK', response.status)
        self.assertEquals(2, len(data))
