"""
This module defines the ProsperCR server
"""

from flask_restful import Resource, Api
from flask_cors import CORS
from mongoengine import connect
from flask import Flask

from server.rest_api.workspace import WorkspacesAPI, WorkspaceAPI
from server.rest_api.field_group import WorkspaceFieldGroupsAPI
from server.rest_api.authentification import LoginAPI
from server.rest_api.user import UserAPI

class ProsperCR(Flask):
    """
    ProsperCR REST API server
    """

    def __init__(self, config):
        super(ProsperCR, self).__init__("prosper-cr")
        self.api_ = None
        self.db_ = None
        self.config_ = config
        self.__init_db__()
        self.__init_routes__()
        self.cors = CORS(self, resources={r"/*": {"origins": "*"}})

    def __init_routes__(self):
        "Initialize the routes"
        self.api_ = Api(self)
        self.api_.add_resource(ServerInfoAPI, '/api')
        self.api_.add_resource(WorkspacesAPI, '/api/workspaces')
        self.api_.add_resource(WorkspaceAPI, '/api/workspaces/<workspace_id>')
        self.api_.add_resource(WorkspaceFieldGroupsAPI, '/api/workspaces/<workspace_id>/field-groups')
        self.api_.add_resource(LoginAPI, '/api/login')
        self.api_.add_resource(UserAPI, '/api/user')

    def __init_db__(self):
        "Initialize the database according to the config parameters"
        self.db_ = connect(self.config_.get('db', 'name'))

    def get_db_connection(self):
        "return the current database"
        return self.db_


class ServerInfoAPI(Resource):
    """
    Root url handler
    """

    def get(self):
        """
        Return general server info
        """
        return {'name': 'prosper-cr',
                'version': '0.1'}
