"""
This module contain all the classes that are needed to the REST API tests
"""
import ConfigParser
import uuid
from mongoengine import register_connection
from mongoengine.context_managers import switch_db
from server.prosper_cr_server import ProsperCR
from server.db.user import User
from server.db.workspace import Workspace
from server.db.template.field import UserFieldGroup, UserField


class BaseTestCase(object):
    """
    This class contains all the rest server initilization needed for
    the tests
    """

    def init_server(self):
        """
        create a configuration with a test database and start the server
        """
        self.TEST_DATABASE = str(uuid.uuid4())
        config = ConfigParser.RawConfigParser()
        config.add_section('db')
        config.set('db', 'name', self.TEST_DATABASE)
        self.server = ProsperCR(config)
        self.app = self.server.test_client()
        register_connection(self.TEST_DATABASE, self.TEST_DATABASE)

    def drop_db(self):
        """
        erase the test database
        """
        self.server.get_db_connection().drop_database(self.TEST_DATABASE)

    def finalize_server(self):
        """
        cleanup after tests
        """
        self.drop_db()

    def create_users(self):
        User(email='user1@testdomain.org').save()
        User(email='user2@testdomain.org').save()

    def create_workspaces(self):
        workspace1 = Workspace(name="Workspace for user 1")
        workspace1.users = User.objects(email='user1@testdomain.org')
        self.create_field_group(workspace1, 'Group 1')
        workspace1.save()

        workspace2 = Workspace(name="Workspace for user 2")
        workspace2.users = User.objects(email='user2@testdomain.org')
        workspace2.save()

    def create_field_group(self, workspace, name):
        group = UserFieldGroup(name=name)
        group.fields.append(
            UserField(name='Field 1', container='choice').initialize())
        group.save()
        workspace.field_groups.append(group)
