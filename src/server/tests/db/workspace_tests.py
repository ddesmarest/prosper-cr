"""
Workspace tests
"""
import unittest
import uuid
from mongoengine import connect, register_connection
from mongoengine.context_managers import switch_db
from server.db.workspace import Workspace
from server.db.user import User
from server.db.template.field import UserFieldGroup, UserField
import server.tests


class WorkspaceTests(unittest.TestCase):
    """
    Workspace tests
    """

    def setUp(self):
        self.db_name = server.tests.create_db(self.__class__.__name__)
        register_connection(self.db_name, self.db_name)

    def tearDown(self):
        server.tests.drop_db(self.db_name)

    def create_users(self):
        """
        Create users for the test
        """
        with switch_db(User, self.db_name) as user:
            user(email="user1@domain.com").save()
            user(email="user2@domain.com").save()

    def create_field_group(self, workspace):
        """
        Create a field group for the test
        """
        with switch_db(UserFieldGroup, self.db_name) as userFieldGroup:
            group = userFieldGroup(name='Group 1')
            group.fields = []
            group.fields.append(
                UserField(name='Int field', container='int').initialize())
            group.save()
            workspace.field_groups.append(group)

    def test_workspace(self):
        """
        * Test the workspace
        """
        self.create_users()
        with switch_db(User, self.db_name) as user:
            user_1 = user.objects(email="user1@domain.com")
        self.assertEquals(1, len(user_1))
        with switch_db(Workspace, self.db_name) as l_workspace:
            workspace = l_workspace(name='Workspace name')
        workspace.users.append(user_1[0])
        self.create_field_group(workspace)
        workspace.save()
        dict_1 = workspace.to_dict(False)
        dict_2 = workspace.to_dict(True)
        self.assertEquals(dict_1['id'], dict_2['id'])
        self.assertEquals(dict_1['name'], dict_2['name'])
        self.assertEquals([[x['id'], x['name']] for x in dict_1['field_groups']], [
                          [x['id'], x['name']] for x in dict_2['field_groups']])
        self.assertNotEquals(['fields' in x for x in dict_1['field_groups']], [
                          'fields' in x for x in dict_2['field_groups']])
