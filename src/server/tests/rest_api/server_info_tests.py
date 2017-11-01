import unittest
from server.prosper_cr_server import ProsperCR
import json
class ServerInfoTests(unittest.TestCase):
    def setUp(self):
        self.server = ProsperCR()
        self.app = self.server.test_client()

    def test_get(self):
        rv = self.app.get('/')
        data = json.loads(rv.data)
        self.assertEquals('prosper-cr', data['name'])
        self.assertEquals('0.1', data['version'])
        #assert b'No entries here so far' in rv.data