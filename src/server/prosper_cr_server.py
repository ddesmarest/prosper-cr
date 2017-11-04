"""
This module defines the ProsperCR server
"""

from flask_restful import Resource, Api
from mongoengine import connect
from flask import Flask

from server.rest_api.workspace import Workspaces
from server.rest_api.authentification import Login

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

    def __init_routes__(self):
        "Initialize the routes"
        self.api_ = Api(self)
        self.api_.add_resource(ServerInfo, '/')
        self.api_.add_resource(Workspaces, '/workspaces')
        self.api_.add_resource(Login, '/login')


    def __init_db__(self):
        "Initialize the database according to the config parameters"
        self.db_ = connect(self.config_.get('db', 'name'))

    def get_db_connection(self):
        "return the current database"
        return self.db_


class ServerInfo(Resource):
    """
    Root url handler
    """

    def get(self):
        """
        Return general server info
        """
        return {'name': 'prosper-cr',
                'version': '0.1'}
