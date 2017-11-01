"""
This module defines the ProsperCR server
"""
from flask import Flask
from flask_restful import Resource
from flask_restful import Api


class ProsperCR(Flask):
    """
    ProsperCR REST API server
    """

    def __init__(self):
        super(ProsperCR, self).__init__("prosper-cr")
        self.api = None
        self.__init_routes__()

    def __init_routes__(self):
        "Initialize the routes"
        self.api = Api(self)
        self.api.add_resource(ServerInfo, '/')


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
