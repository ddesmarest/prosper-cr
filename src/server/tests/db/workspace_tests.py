import unittest
from mongoengine import connect
from server.db.workspace import Workspace
from server.db.user import User
from server.db.template.field import UserFieldGroup, UserField


class UserFieldTests(unittest.TestCase):
    """
    Basic types tests
    """

    def setUp(self):
        self.db_ = connect('test_user_field_group')

    def tearDown(self):
        self.db_.drop_database('test_user_field_group')

    def create_users(self):
        """
        Create users for the test
        """
        User(email="user1@domain.com").save()
        User(email="user2@domain.com").save()

    def create_field_group(self, workspace):
        """
        Create a field group for the test
        """
        group = UserFieldGroup(name='Group 1')
        group.fields = []
        group.fields.append(
            UserField(name='Int field', container='int').initialize())
        group.save()
        workspace.field_groups.append(group)

    def test_workspace(self):
        """
        Test the workspace
        """
        self.create_users()
        user_1 = User.objects(email="user1@domain.com")
        self.assertEquals(1, len(user_1))
        workspace = Workspace()
        workspace.users.append(user_1[0])
        self.create_field_group(workspace)
        workspace.save()

