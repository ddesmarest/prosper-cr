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
        * Test GET /workspaces/<workspace_id>
        """
        response = self.get('/workspaces/12315')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.get('/workspaces/12315')
        self.assertEquals('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertNotEquals('', data['message'])
        users = User.objects(id=self.login_user['id'])
        self.assertEquals(1, len(users))
        workspaces = Workspace.objects(users=users[0])
        self.assertEquals(1, len(workspaces))
        workspace = workspaces[0]
        response = self.get('/workspaces/'+ str(workspace.id))
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals(data['name'], workspace.name)
        self.assertEquals(data['id'], str(workspace.id))
        self.assertEquals(1,len(data['field_groups']))
        self.assertEquals('Group 1',data['field_groups'][0]['name'])
        self.logout()
        response = self.get('/workspaces/'+str(workspace.id))
        self.assertEquals('401 UNAUTHORIZED', response.status)

    def test_put(self):
        """
        * Test PUT /workspaces/<workspace_id>
        """
        response = self.put('/workspaces/12315')
        self.assertEquals('401 UNAUTHORIZED', response.status)
        self.login()
        response = self.put('/workspaces/12315')
        self.assertEquals('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertNotEquals('', data['message'])
        users = User.objects(id=self.login_user['id'])
        self.assertEquals(1, len(users))
        workspaces = Workspace.objects(users=users[0])
        self.assertEquals(1, len(workspaces))
        workspace = workspaces[0]
        new_name = 'New workspace name'
        response = self.put('/workspaces/'+ str(workspace.id), data_dict={'name':new_name})
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertEquals(data['name'], new_name)
        self.assertEquals(data['id'], str(workspace.id))
        self.logout()
        response = self.get('/workspaces',str(workspace.id))
        self.assertEquals('401 UNAUTHORIZED', response.status)
        
