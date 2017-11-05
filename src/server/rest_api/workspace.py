"""
This module contains all the handler for workspace
"""
from flask_restful import Resource, reqparse
from flask import g, request
from server.db.workspace import Workspace
from server.rest_api.authentification import AUTH


class WorkspacesAPI(Resource):
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
        return new_workspace.to_dict(), 201


class WorkspaceAPI(Resource):
    """
    /workspaces/<workspace id> handler
    """
    @AUTH.login_required
    def get(self, workspace_id):
        """
        Returns a workspace
        """
        try:
            workspace = Workspace.objects(users=g.user, id=workspace_id)[0]
            return workspace.to_dict()
        except Exception as e:
            return {'message': 'Workspace cannot be found for user ' + g.user.email,
                    'error': e.message}, 400

    @AUTH.login_required
    def put(self, workspace_id):
        """
        Update a workspace
        """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', required=True,
                                help="Workspace name missing", location='json')
            args = parser.parse_args()
            new_name = args['name']
            workspace = Workspace.objects(users=g.user, id=workspace_id)[0]
            if workspace.name != new_name:
                workspace.update(set__name=new_name)
                workspace.reload()
            return workspace.to_dict()
        except Exception as e:
            return {'message': 'Workspace ' + workspace_id + ' for user ' + g.user.email + 'cannot be updated',
                    'error': e.message}, 400
