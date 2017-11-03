"""
This module contains all the handler for workspace
"""
from flask_restful import Resource, reqparse
from flask import g, request
from server.db.workspace import Workspace
from server.rest_api.authentification import AUTH


class Workspaces(Resource):
    """
    /workspaces handler
    """
    @AUTH.login_required
    def get(self):
        """
        Returns the workspaces
        """
        workspaces = []
        for workspace in Workspace.objects(users=g.user):
            workspaces.append(workspace.to_dict())
        return workspaces

    """
    /workspaces handler
    """
    @AUTH.login_required
    def post(self):
        """
        Returns the workspaces
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True,
                            help="Workspace name missing", location='json')
        args = parser.parse_args()        
        new_workspace = Workspace(name=args['name'])
        new_workspace.users = [g.user]
        new_workspace.save()
        return new_workspace.to_dict()
