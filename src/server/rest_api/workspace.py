"""
This module contains all the handler for workspace
"""
from flask_restful import Resource, reqparse
from flask import g, request
from server.db.workspace import Workspace
from server.rest_api.authentification import AUTH
from server.rest_api import create_error_data


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
            workspaces.append(workspace.to_dict(False))
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
        return new_workspace.to_dict(False), 201


class WorkspaceAPI(Resource):
    """
    /workspaces/<workspace id> handler
    """

    def get_workspace(self, workspace_id):
        """
        return the workspace given its id
        """
        return Workspace.objects(users=g.user, id=workspace_id)[0]

    @AUTH.login_required
    def get(self, workspace_id):
        """
        Returns a workspace
        """
        parser = reqparse.RequestParser()
        parser.add_argument('recursive', type=bool, default=False)
        args = parser.parse_args()
        try:
            workspace = self.get_workspace(workspace_id)
            return workspace.to_dict(args['recursive'])
        except Exception as e:
            return create_error_data('Workspace cannot be found for user ' + g.user.email, e), 400

    @AUTH.login_required
    def put(self, workspace_id):
        """
        Update a workspace
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True,
                            help="Workspace name missing", location='json')
        args = parser.parse_args()

        try:
            new_name = args['name']
            workspace = workspace = self.get_workspace(workspace_id)
            if workspace.name != new_name:
                workspace.update(set__name=new_name)
                workspace.reload()
            return workspace.to_dict(False)
        except Exception as e:
            return create_error_data('Workspace ' + workspace_id + ' for user ' + g.user.email + 'cannot be updated', e), 400

    @AUTH.login_required
    def delete(self, workspace_id):
        """
        Delete a workspace
        """
        try:
            workspace = workspace = self.get_workspace(workspace_id)
            workspace.delete()
            return {}, 204
        except Exception as e:
            return create_error_data('Workspace ' + workspace_id + ' for user ' + g.user.email + 'cannot be deleted', e), 400
