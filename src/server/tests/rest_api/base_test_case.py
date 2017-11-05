"""
This module contain all the classes that are needed to the REST API tests
"""
import ConfigParser
import uuid
import base64
import json

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

    USER_EMAIL = 'user1@testdomain.org'
    USER_PASSWORD = 'test'

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
        self.login_token = None

    def drop_db(self):
        """
        erase the test database
        """
        UserFieldGroup.drop_collection()
        Workspace.drop_collection()
        User.drop_collection()
        self.server.get_db_connection().drop_database(self.TEST_DATABASE)

    def finalize_server(self):
        """
        cleanup after tests
        """
        self.drop_db()

    def create_users(self):
        User(email=self.USER_EMAIL).set_password(self.USER_PASSWORD).save()
        User(email='user2@testdomain.org').set_password('test2').save()

    def create_workspaces(self):
        workspace1 = Workspace(name="Workspace for user 1")
        workspace1.users = User.objects(email=self.USER_EMAIL)
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

    def create_authentication_header(self, username, password):
        """Return the header dictionary
        Create the authorization string for the given user
        """
        return {
            'Authorization': 'Basic ' + base64.b64encode(username + ":" + password)
        }

    def get_full_url(self, url_tail):
        """Return a full url by adding prefix '/api'        
        """
        return '/api' + url_tail

    def add_login_header(self, **kwargs):
        if self.login_token is not None:
            if 'headers' in kwargs:
                kwargs['headers']['Authorization'] = 'Basic ' + \
                    base64.b64encode(self.login_token + ":unused")
            else:
                kwargs['headers'] = {'Authorization': 'Basic ' +
                                     base64.b64encode(self.login_token + ":unused")}
        return kwargs

    def get(self, url_tail, *arg, **kwargs):
        """Return response to the HTTP GET method
        """
        kwargs = self.add_login_header(**kwargs)
        return self.app.get(self.get_full_url(url_tail), *arg, **kwargs)

    def post(self, url_tail, *arg, **kwargs):
        """Return response to the HTTP POST method
        """
        kwargs = self.add_login_header(**kwargs)
        if 'data_dict' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data_dict'])
            kwargs['content_type'] = 'application/json'
            del kwargs['data_dict']
        return self.app.post(self.get_full_url(url_tail), *arg, **kwargs)

    def put(self, url_tail, *arg, **kwargs):
        """Return response to the HTTP PUT method
        """
        kwargs = self.add_login_header(**kwargs)
        if 'data_dict' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data_dict'])
            kwargs['content_type'] = 'application/json'
            del kwargs['data_dict']
        return self.app.put(self.get_full_url(url_tail), *arg, **kwargs)

    def login(self):
        """Login using the test USER_MAIL/USER_PASSWORD and
        store the token/id for the next get/post/put operation
        """
        self.login_token = None
        self.login_user = None
        response = self.post(
            '/login', data_dict=dict(email=self.USER_EMAIL, password=self.USER_PASSWORD))
        self.assertEquals('200 OK', response.status)
        data = json.loads(response.data)
        self.assertIsNotNone(data['token'])
        self.login_token = data['token']
        self.assertIsNotNone(data['user'])
        self.login_user = data['user']

    def logout(self):
        """Clear then login_id
        """
        self.login_token = None
        self.login_user = None