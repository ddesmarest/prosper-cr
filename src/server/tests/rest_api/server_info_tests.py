from server.tests.rest_api.base_test_case import BaseTestCase
import json
import unittest


class ServerInfoTests(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.init_server()

    def tearDown(self):
        self.finalize_server()

    def test_get(self):
        """
        * Test GET /
        """
        rv = self.app.get('/')
        data = json.loads(rv.data)
        self.assertEquals('prosper-cr', data['name'])
        self.assertEquals('0.1', data['version'])
