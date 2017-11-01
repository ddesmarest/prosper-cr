from server.tests.rest_api.base_test_case import BaseTestCase
import json
import unittest


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
        rv = self.app.get('/workspaces')
        data = json.loads(rv.data)
        #print data
        #self.assertEquals('prosper-cr', data['name'])
        #self.assertEquals('0.1', data['version'])
        #assert b'No entries here so far' in rv.data
