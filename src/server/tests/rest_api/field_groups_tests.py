import json
import unittest
from server.tests.rest_api.base_test_case import BaseTestCase
from server.db.workspace import Workspace
from server.db.user import User

class WorkspaceFieldGroupsAPITests(BaseTestCase, unittest.TestCase):
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
        response = self.get('/workspaces/123/field-groups')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.get('/workspaces/12315/field-groups')
        self.assertEquals('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertNotEquals('', data['message'])
        users = User.objects(id=self.login_user['id'])
        self.assertEquals(1, len(users))
        workspaces = Workspace.objects(users=users[0])
        self.assertEquals(1, len(workspaces))
        workspace = workspaces[0]
        response = self.get('/workspaces/'+ str(workspace.id)+'/field-groups')
        print response.data
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals(1, len(data))
        self.assertEquals(workspace.field_groups[0].name, data[0]['name'])
        self.assertEquals(len(workspace.field_groups[0].fields), len(data[0]['fields']))
        self.logout()
        #response = self.get('/workspaces')
        #self.assertEquals('401 UNAUTHORIZED', response.status)